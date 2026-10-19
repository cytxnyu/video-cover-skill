# 双版提示词

先读 `editorial-style.md`，再把花括号槽位换成本条视频的真实信息。正式生图调用必须全部填实。用户只要提示词时也交付两份已填好的提示词。

## 共用内容与风格

这段在两版保持一致。文字字段必须是希望真正上图的定稿，不把素材说明当文案。

```text
Create ONE finished editorial collage video cover, not a mockup or a two-panel comparison.
Video meaning: {本条视频讲解内容与可证实结果的一句话}.
Visual metaphor: {原版主题映射中的具体隐喻}. Composition system: {原版构图系统}.
Use 1–3 visual anchors in total: {真实主角、主题物件或真实演示截图}.
Reference roles: {逐一列出 Image 1 / Image 2；区分人物参考、界面素材、风格参考}.
Preserve the SAME recognizable person from the original video reference: facial structure,
hairstyle, age appearance, clothing, and distinctive details. Treat the person as a real
photographic magazine cutout with torn paper edges, not an invented face or cartoon.
{无人物视频删除保脸段，明确以真实演示界面或产品作为主角}.

Exact visible text, in Chinese unless otherwise requested:
A-layer giant main title: "{主标题}".
B-layer supporting title: "{完整信息短句}".
C-layer minimal microcopy: "{经核实的关键词；没有则明确不添加}".
Render only approved strings. Keep every Chinese character and brand spelling exact.
Make the main title bold, dominant and readable at feed-thumbnail size.

Style: torn-paper collage, handmade magazine cover layout, punk zine aesthetic,
vintage print texture, mixed media poster, irregular ripped paper edges, bold typography,
retro offset printing, risograph grain, photocopy texture, halftone dots,
scanned magazine cutouts, analog street-poster collage with refined editorial balance.
Build four layers: title skeleton; photographic anchors; purposeful paper strips/tape/
labels/handwritten annotations; textured paper or photocopy background with fibers,
folds and scan marks. Let image and type interact while preserving readability.
Color palette: {取自原版色盘方向，并按这条视频选择}. Mood: {视频情绪}.
Keep at least one memorable saturated accent and strong contrast.

Avoid: generic ecommerce cover, PPT slide layout, flat infographic, clean rectangles only,
all-gray low contrast, cheap cyber neon, generic robot face, unrelated visual anchors,
unreadable or invented text, fabricated dates/statistics, facial identity drift,
extra fingers, duplicate person, dirty chaotic clutter, watermark, mockup borders,
black bars, contact sheet, multiple covers within one image.
```

## 3:4 竖版前后缀

共用段前添加：

```text
VERTICAL PORTRAIT 3:4 CANVAS, target 1536x2048 pixels. Exact width:height = 3:4.
Design a full-bleed vertical video cover, not a horizontal image inside a vertical frame.
Build a vertical reading flow. {根据人物视线与主题确定标题、人物和纸带的上下错层关系}.
Keep the person large and recognizable; adapt the crop to the original pose without changing identity.
Protect face and main title with about 5% edge inset and keep critical content above the bottom 10%.
Paper textures and deliberate collage fragments reach the edges.
```

共用段后添加：

```text
Deliver ONE vertical image at exact 3:4. Avoid square, 4:5, 9:16, horizontal composition,
or a wide poster padded above and below. This is a native 3:4 composition.
```

不要继承原版横幅提示词里的 `avoid vertical poster`。

## 16:10 横版前后缀

共用段前添加：

```text
WIDE HORIZONTAL 16:10 CANVAS, target 2304x1440 pixels. Exact width:height = 16:10 (8:5).
Design a full-bleed horizontal video cover, not 16:9, not 5:2, not a centered vertical poster.
Build a horizontal reading flow. {按人物朝向、动作和隐喻确定人物与标题的左右区域}.
Reflow the headline, scale photographic anchors and move torn-paper layers for this width.
Use the whole horizontal canvas with deliberate collage material at both sides.
Preserve the same title, original person, metaphor, palette and print texture as the portrait edition.
The portrait edition, if supplied, is ONLY a style reference. Recompose instead of cropping it.
Protect face and main title with about 5% edge inset and keep critical content above the bottom 10%.
```

共用段后添加：

```text
Deliver ONE horizontal image at exact 16:10 (8:5). Avoid 16:9, 3:2, 5:2, square,
vertical poster, empty side margins, stretching, padding, or cropping the portrait cover.
This is a native 16:10 composition with the same visual identity.
```

## 定点修正

- 字错：引用当前封面为编辑目标，逐字给正确文字；锁定人物、版式、色盘与纸张细节。
- 人物变样：重新附原始视频帧，标明该帧才是身份参考；只修正人物特征。
- 比例不符：用图像工具按本版画幅重新布局并重申精确宽高比；重新检测文件，不只看工具回话。
- 两版像裁切：重定标题分区、人物大小、纸带方向，生成专门横版／竖版，主题与人物不变。
- 风格漂移：补回原版撕纸轮廓、照片剪贴、网点套印、背景纸纹和粗标题层次，不叠加其他风格。
