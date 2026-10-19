# 视频封面

根据视频内容和真实人物素材，使用 `cover-editorial-collage` 的撕纸杂志拼贴风格，生成两张独立构图的视频封面。

## 默认产出

| 版本 | 精确比例 | 建议工作尺寸 |
| --- | --- | --- |
| 竖版 | 3:4 | 1536 × 2048 |
| 横版 | 16:10 | 2304 × 1440 |

两版共用人物、标题、隐喻和色盘，但分别排版，不靠拉伸或裁切转换。实际文件会进行比例检测，并检查人物一致性、文字和视觉风格。

## 安装到 Codex

Skill 名称和 Codex 显示名均为 **视频封面**。推荐复制安装，以保留中文目录名。

先下载 ZIP，或克隆：

```bash
git clone https://github.com/cytxnyu/video-cover-skill.git
```

将仓库中的 `skills/视频封面` 整个文件夹放入 Codex 的 `skills` 目录。默认位置为 `~/.codex/skills/视频封面`；设置了 `CODEX_HOME` 时使用其下的 `skills` 目录。

Windows PowerShell 示例（在包含已克隆仓库的目录执行）：

```powershell
$skillHome = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME 'skills' } else { Join-Path $HOME '.codex/skills' }
$target = Join-Path $skillHome '视频封面'
if (Test-Path -LiteralPath $target) { throw '目标技能已存在，请先检查现有版本。' }
New-Item -ItemType Directory -Path $skillHome -Force | Out-Null
Copy-Item -LiteralPath './video-cover-skill/skills/视频封面' -Destination $target -Recurse
```

也可以通过 Skills CLI 安装：

```bash
npx -y skills add cytxnyu/video-cover-skill -g -a codex --skill "视频封面" -y
```

安装器当前会把全中文名称对应的文件夹写成 `unnamed-skill`，文件里的名称仍是「视频封面」。为了保留中文目录并避免与其他中文 Skill 的目录重名，优先使用上面的复制安装方式。

## 使用

上传视频，或提供逐字稿／字幕与人物照片，然后输入：

```text
使用 $视频封面，根据我上传的视频内容和人物制作封面。
完全沿用 cover-editorial-collage 风格，生成 3:4 和 16:10 两张独立构图的成品。
自动提炼准确标题，保留人物辨识度，检查实际比例后展示并保存图片。
```

只有口播稿而缺少人物素材时，会索取照片或视频截图；无人出镜的录屏可用真实界面或产品作为主体。默认直接生成图片，明确要求提示词时才只输出提示词。

## 运行依赖

- 支持本 Skill 及图像查看、图像生成工具的 Codex 环境；默认使用内置图像生成工具。
- Python 3.9+，用于运行辅助脚本。
- Pillow，用于只读图片尺寸与解码检查：`python -m pip install Pillow`。
- FFmpeg 和 FFprobe，供视频抽帧使用；两者需在 PATH 中。
- 仅有视频且没有字幕时，还需要环境中的音频／视频理解能力，或由用户提供字幕；抽帧脚本本身不转写语音。

## 文件

- `skills/视频封面/SKILL.md`：完整工作流。
- `agents/openai.yaml`：Codex 显示名与默认调用。
- `references/`：原版风格摘录、双比例提示词与尺寸配置。
- `scripts/inspect_video.py`：抽帧及时间戳记录。
- `scripts/check_covers.py`：检查两张图片的实际比例与格式，不修改图片。

后四项位于 `skills/视频封面/` 内。公开仓库不包含本地评测样本、预期答案、运行记录或个人视频。

## 风格来源与许可

原版 `cover-editorial-collage` 的五节核心视觉规则保存在 `references/editorial-style.md`，原始 SHA-256 随文记录。该风格摘录随 Skill 一起提供，不需要额外安装原版才能读取这些规则。原版 MIT 许可证保留在仓库及 Skill 目录中。

图片内容始终取自用户提供的视频、人物参考及经确认的文案；本仓库交付的是工作流与辅助脚本。
