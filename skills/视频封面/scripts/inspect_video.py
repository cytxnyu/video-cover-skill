#!/usr/bin/env python3
"""Extract timestamped video frames; no speech or person inference."""
from __future__ import annotations

import argparse
import json
import math
import shutil
import subprocess
import sys
from pathlib import Path


def run(command: list[str]) -> subprocess.CompletedProcess:
    result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if result.returncode:
        raise ValueError(f"{Path(command[0]).stem} failed: {result.stderr.strip()}")
    return result


def sample_times(duration: float, count: int) -> list[float]:
    if not math.isfinite(duration) or duration <= 0:
        raise ValueError("Video duration must be finite and positive")
    if not 2 <= count <= 24:
        raise ValueError("Frame count must be between 2 and 24")
    return [round(duration * (0.08 + 0.84 * index / (count - 1)), 6) for index in range(count)]


def extract(video: Path, out: Path, count: int) -> dict:
    video = video.expanduser().resolve()
    out = out.expanduser().resolve()
    if not video.is_file():
        raise ValueError(f"Video does not exist: {video}")
    if out.exists():
        raise ValueError(f"Output directory already exists; choose a new directory: {out}")
    sample_times(1.0, count)
    ffprobe, ffmpeg = shutil.which("ffprobe"), shutil.which("ffmpeg")
    if not ffprobe or not ffmpeg:
        raise ValueError("FFmpeg and FFprobe must both be available on PATH")
    meta = json.loads(run([
        ffprobe, "-v", "error", "-show_streams", "-show_format", "-of", "json", str(video)
    ]).stdout)
    streams = [s for s in meta.get("streams", []) if s.get("codec_type") == "video"
               and not s.get("disposition", {}).get("attached_pic", 0)]
    if not streams:
        raise ValueError("Input has no video stream")
    stream = streams[0]
    duration = None
    for raw in (stream.get("duration"), meta.get("format", {}).get("duration")):
        try:
            candidate = float(raw)
        except (TypeError, ValueError):
            continue
        if math.isfinite(candidate) and candidate > 0:
            duration = candidate
            break
    if duration is None:
        raise ValueError("A finite positive video duration is required")
    times = sample_times(duration, count)
    out.mkdir(parents=True, exist_ok=False)
    frames = []
    for index, seconds in enumerate(times, 1):
        path = out / f"frame-{index:02d}-{seconds:010.3f}s.png"
        run([
            ffmpeg, "-nostdin", "-hide_banner", "-loglevel", "error", "-n",
            "-ss", f"{seconds:.6f}", "-i", str(video), "-map", f"0:{stream['index']}",
            "-frames:v", "1", str(path),
        ])
        if not path.is_file() or path.stat().st_size == 0:
            raise ValueError(f"No decoded frame at {seconds}s; inspect video timing")
        frames.append({"seconds": seconds, "path": str(path)})
    captions = [str(video.with_suffix(ext)) for ext in (".srt", ".vtt", ".txt")
                if video.with_suffix(ext).is_file()]
    result = {
        "source": str(video), "duration_seconds": duration,
        "video_stream_index": stream["index"],
        "encoded_width": stream.get("width"), "encoded_height": stream.get("height"),
        "has_audio": any(s.get("codec_type") == "audio" for s in meta.get("streams", [])),
        "frames": frames, "caption_candidates": captions,
        "speech_transcribed": False, "person_selected": False,
        "note": "View frames and read or transcribe speech before deciding content or protagonist.",
    }
    (out / "video-evidence.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--count", type=int, default=8)
    args = parser.parse_args()
    try:
        result = extract(args.video, args.out, args.count)
    except (OSError, ValueError, KeyError) as error:
        print(json.dumps({"ok": False, "error": str(error)}, ensure_ascii=False))
        return 2
    print(json.dumps({"ok": True, **result}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
