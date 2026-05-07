---
title: "Feature Showcase — Markdown · Prism · KaTeX · Mermaid · Shortcodes"
slug: feature-showcase
date: '2026-05-06T00:00:00+02:00'
weight: 999
postId: _draft-feature-test
i18nKey: post.draft-feature-test.title
categoryI18n: cat.notes
dateDisplay: 2026·05·06
bylineDate: 2026 · 05 · 06
kickers:
  en: DRAFT · 2026
  zh: 草稿 · 2026
  tw: 草稿 · 2026
readTimes:
  en: 3 min read
  zh: 阅读约 3 分钟
  tw: 閱讀約 3 分鐘
heroCaption: F · 999 · DRAFT · FEATURE TEST
titles:
  en: "Feature Showcase — every block on one page"
  zh: "特性大全 — 一页跑完所有 block"
  tw: "特性大全 — 一頁跑完所有 block"
decks:
  en: A draft page that exercises Markdown, Prism syntax highlighting, KaTeX, Mermaid, and every Hugo shortcode the theme ships. Useful as a pixel-level smoke test before shipping new chrome.
  zh: 一篇草稿，把 Markdown / Prism 语法高亮 / KaTeX / Mermaid / 主题自带的所有 Hugo shortcode 全部跑一遍。每次改主题前用作像素级回归。
  tw: 一篇草稿，把 Markdown / Prism 語法高亮 / KaTeX / Mermaid / 主題自帶的所有 Hugo shortcode 全部跑一遍。每次改主題前用作像素級回歸。
prev:
  href: /posts/hello-world.html
  title: ← Hello, World
next:
  href: /posts.html
  title: Browse all writing →
lastmod: '2026-05-06T00:00:00+02:00'
---

<div class="lang-block" data-lang="en" data-active="true">

## 1 · Markdown

This paragraph mixes **bold**, *italic*, ~~strikethrough~~, inline `code`, a [link](https://gohugo.io), and a <mark>highlighted phrase</mark>. The footnote marker[^1] points to a footnote at the end.

> Blockquotes carry the brand left-rule. They wrap multiple lines without choking, and you can nest **emphasis** inside them.

### 1.1 Lists

Unordered:

- First bullet — short and punchy
- Second bullet with *italic* and `code`
- Third bullet, nested:
  - Nested bullet a
  - Nested bullet b

Ordered:

1. Step one
2. Step two
3. Step three

### 1.2 Tables

| Feature   | Engine        | Loaded     |
|-----------|---------------|------------|
| Highlight | Prism.js      | on demand  |
| Math      | KaTeX 0.16    | on demand  |
| Diagrams  | Mermaid 10.9  | on demand  |

### 1.3 Horizontal rule

---

## 2 · Syntax highlighting (Prism client-side)

JavaScript:

```javascript
// Lazy-load mermaid only when a .mermaid block exists.
const blocks = document.querySelectorAll('.body pre.mermaid');
if (blocks.length) {
  import('https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.esm.min.mjs')
    .then(({ default: m }) => m.run({ querySelector: '.body pre.mermaid' }));
}
```

Python:

```python
def attention(q, k, v, mask=None):
    """Single-head dot-product attention."""
    d_k = q.size(-1)
    scores = (q @ k.transpose(-2, -1)) / d_k ** 0.5
    if mask is not None:
        scores = scores.masked_fill(mask == 0, -1e9)
    return torch.softmax(scores, dim=-1) @ v
```

Swift (closure args `$0` / `$1` must NOT trigger KaTeX — guarded against this collision):

```swift
let nums = [1, 2, 3, 4, 5]
let doubled = nums.map { $0 * 2 }
let summed  = nums.reduce(0) { $0 + $1 }
print("doubled=\(doubled), sum=\(summed)")
```

Bash:

```bash
hugo --gc --minify
rsync -avz public/ deploy@example.com:/var/www/site/
```

JSON:

```json
{
  "name": "xpage",
  "version": "1.0.0",
  "features": ["markdown", "prism", "katex", "mermaid", "shortcodes"]
}
```

## 3 · KaTeX (math)

Inline math: the gradient of cross-entropy loss is \\(\nabla_\theta \mathcal{L} = -\sum_i y_i \nabla_\theta \log \hat{y}_i\\), and softmax is defined as \\(\sigma(z)_j = e^{z_j} / \sum_k e^{z_k}\\).

Display block — scaled dot-product attention:

$$
\text{Attention}(Q, K, V) = \text{softmax}\!\left( \frac{Q K^\top}{\sqrt{d_k}} \right) V
$$

Bracket form — Bayes' rule:

$$
P(A \mid B) = \frac{P(B \mid A)\, P(A)}{P(B)}
$$

Multi-line aligned:

$$
\begin{aligned}
  \mathcal{L}_\text{recon} &= \lVert x - \hat{x} \rVert_2^2 \\
  \mathcal{L}_\text{kl}    &= D_\text{KL}\!\left(q_\phi(z \mid x)\,\|\,p(z)\right) \\
  \mathcal{L}_\text{vae}   &= \mathcal{L}_\text{recon} + \beta \mathcal{L}_\text{kl}
\end{aligned}
$$

## 4 · Mermaid diagrams

Flowchart:

{{< mermaid caption="On-demand loader decision tree." >}}
graph TD
  A[Page loads] --> B{Has pre.mermaid?}
  B -- no --> C[Skip - zero cost]
  B -- yes --> D[Fetch mermaid ESM]
  D --> E[Initialize w/ brand theme]
  E --> F[Render diagrams]
{{< /mermaid >}}

Sequence diagram:

{{< mermaid caption="A round-trip through the article lightbox." >}}
sequenceDiagram
  participant U as User
  participant I as Image
  participant L as Lightbox
  U->>I: click
  I->>L: open(src, caption)
  L-->>U: zoom in
  U->>L: ESC
  L-->>U: close
{{< /mermaid >}}

State diagram:

{{< mermaid caption="Live Photo state machine." >}}
stateDiagram-v2
  [*] --> Idle
  Idle --> Ready: hover
  Ready --> Playing: video.play()
  Playing --> Idle: mouseleave
{{< /mermaid >}}

## 5 · Hugo shortcodes

### 5.1 image-size

{{< image-size src="https://picsum.photos/seed/demoSingle/800/500" alt="Sample diagram alt text" caption="image-size shortcode — single figure with caption + click-to-lightbox." center="true" >}}

### 5.2 image-grid

{{< image-grid columns="2" gap="1rem" images="https://picsum.photos/seed/demoGridA/800/500||Sample image A, https://picsum.photos/seed/demoGridB/800/500||Sample image B" >}}

### 5.3 image-carousel

{{< image-carousel
    width="90%"
    center="true"
    autoplay="false"
    caption="image-carousel shortcode — manual navigation, lightbox-aware."
    images="https://picsum.photos/seed/demoCarA/800/500, https://picsum.photos/seed/demoCarB/800/500, https://picsum.photos/seed/demoCarC/800/500" >}}

### 5.4 live-photo

{{< live-photo src="/assets/live/disc-rotate.jpg" video="/assets/live/disc-rotate.mov" width="60%" center="true" caption="live-photo shortcode — hover to play, lightbox shows LIVE badge." >}}

[^1]: Footnote text — Goldmark renders this as a back-linked block at the bottom of the article.

</div>

<div class="lang-block" data-lang="zh">

## 1 · Markdown

这一段混合 **粗体**、*斜体*、~~删除线~~、行内 `code`、一个 [链接](https://gohugo.io)，以及一段 <mark>黄色高亮</mark>。脚注标记[^1]指向文末脚注。

> 引用块带左侧品牌竖条。多行内容不会断，里面也可以嵌套 **强调**。

### 1.1 列表

无序：

- 第一条
- 第二条带 *斜体* 和 `code`
- 第三条，嵌套：
  - 嵌套 a
  - 嵌套 b

有序：

1. 第一步
2. 第二步
3. 第三步

### 1.2 表格

| 特性     | 引擎          | 加载方式 |
|---------|---------------|---------|
| 高亮     | Prism.js      | 按需    |
| 数学     | KaTeX 0.16    | 按需    |
| 图表     | Mermaid 10.9  | 按需    |

### 1.3 分隔线

---

## 2 · 语法高亮（Prism 客户端）

JavaScript：

```javascript
// 仅当页面存在 .mermaid 块时才加载 mermaid
const blocks = document.querySelectorAll('.body pre.mermaid');
if (blocks.length) {
  import('https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.esm.min.mjs')
    .then(({ default: m }) => m.run({ querySelector: '.body pre.mermaid' }));
}
```

Python：

```python
def attention(q, k, v, mask=None):
    """单头点积注意力。"""
    d_k = q.size(-1)
    scores = (q @ k.transpose(-2, -1)) / d_k ** 0.5
    if mask is not None:
        scores = scores.masked_fill(mask == 0, -1e9)
    return torch.softmax(scores, dim=-1) @ v
```

Swift（闭包参数 `$0` / `$1` 不能误触发 KaTeX）：

```swift
let nums = [1, 2, 3, 4, 5]
let doubled = nums.map { $0 * 2 }
let summed  = nums.reduce(0) { $0 + $1 }
print("doubled=\(doubled), sum=\(summed)")
```

## 3 · KaTeX（数学公式）

行内：交叉熵的梯度为 \\(\nabla_\theta \mathcal{L} = -\sum_i y_i \nabla_\theta \log \hat{y}_i\\)，softmax 定义为 \\(\sigma(z)_j = e^{z_j} / \sum_k e^{z_k}\\)。

行间 — 缩放点积注意力：

$$
\text{Attention}(Q, K, V) = \text{softmax}\!\left( \frac{Q K^\top}{\sqrt{d_k}} \right) V
$$

方括号 — 贝叶斯：

$$
P(A \mid B) = \frac{P(B \mid A)\, P(A)}{P(B)}
$$

多行对齐：

$$
\begin{aligned}
  \mathcal{L}_\text{recon} &= \lVert x - \hat{x} \rVert_2^2 \\
  \mathcal{L}_\text{kl}    &= D_\text{KL}\!\left(q_\phi(z \mid x)\,\|\,p(z)\right) \\
  \mathcal{L}_\text{vae}   &= \mathcal{L}_\text{recon} + \beta \mathcal{L}_\text{kl}
\end{aligned}
$$

## 4 · Mermaid 图表

流程图：

{{< mermaid caption="按需加载决策树。" >}}
graph TD
  A[页面加载] --> B{有 pre.mermaid?}
  B -- 没有 --> C[跳过 - 零成本]
  B -- 有 --> D[加载 mermaid ESM]
  D --> E[品牌主题初始化]
  E --> F[渲染图表]
{{< /mermaid >}}

时序图：

{{< mermaid caption="文章大图模式的一次往返。" >}}
sequenceDiagram
  participant U as 用户
  participant I as 图片
  participant L as 大图模式
  U->>I: 点击
  I->>L: open(src, caption)
  L-->>U: 放大
  U->>L: ESC
  L-->>U: 关闭
{{< /mermaid >}}

状态图：

{{< mermaid caption="Live Photo 状态机。" >}}
stateDiagram-v2
  [*] --> Idle
  Idle --> Ready: hover
  Ready --> Playing: video.play()
  Playing --> Idle: mouseleave
{{< /mermaid >}}

## 5 · Hugo Shortcodes

### 5.1 image-size

{{< image-size src="https://picsum.photos/seed/demoSingle/800/500" alt="示例图替换文本" caption="image-size — 单图 + caption + 点击进入大图模式。" center="true" >}}

### 5.2 image-grid

{{< image-grid columns="2" gap="1rem" images="https://picsum.photos/seed/demoGridA/800/500||示例图 A, https://picsum.photos/seed/demoGridB/800/500||示例图 B" >}}

### 5.3 image-carousel

{{< image-carousel
    width="90%"
    center="true"
    autoplay="false"
    caption="image-carousel — 手动切换，与大图模式联动。"
    images="https://picsum.photos/seed/demoCarA/800/500, https://picsum.photos/seed/demoCarB/800/500, https://picsum.photos/seed/demoCarC/800/500" >}}

### 5.4 live-photo

{{< live-photo src="/assets/live/disc-rotate.jpg" video="/assets/live/disc-rotate.mov" width="60%" center="true" caption="live-photo — hover 播放，大图模式带 LIVE 徽章。" >}}

[^1]: 脚注内容 — Goldmark 会在文末渲染为带回链的块。

</div>

<div class="lang-block" data-lang="tw">

## 1 · Markdown

這一段混合 **粗體**、*斜體*、~~刪除線~~、行內 `code`、一個 [連結](https://gohugo.io)，以及一段 <mark>黃色高亮</mark>。腳註標記[^1]指向文末腳註。

> 引用塊帶左側品牌豎條。多行內容不會斷，裡面也可以嵌套 **強調**。

### 1.1 列表

無序：

- 第一條
- 第二條帶 *斜體* 和 `code`
- 第三條，嵌套：
  - 嵌套 a
  - 嵌套 b

有序：

1. 第一步
2. 第二步
3. 第三步

### 1.2 表格

| 特性     | 引擎          | 載入方式 |
|---------|---------------|---------|
| 高亮     | Prism.js      | 按需    |
| 數學     | KaTeX 0.16    | 按需    |
| 圖表     | Mermaid 10.9  | 按需    |

### 1.3 分隔線

---

## 2 · 語法高亮（Prism 客戶端）

JavaScript：

```javascript
// 僅當頁面存在 .mermaid 區塊時才載入 mermaid
const blocks = document.querySelectorAll('.body pre.mermaid');
if (blocks.length) {
  import('https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.esm.min.mjs')
    .then(({ default: m }) => m.run({ querySelector: '.body pre.mermaid' }));
}
```

Python：

```python
def attention(q, k, v, mask=None):
    """單頭點積注意力。"""
    d_k = q.size(-1)
    scores = (q @ k.transpose(-2, -1)) / d_k ** 0.5
    if mask is not None:
        scores = scores.masked_fill(mask == 0, -1e9)
    return torch.softmax(scores, dim=-1) @ v
```

Swift（閉包參數 `$0` / `$1` 不能誤觸發 KaTeX）：

```swift
let nums = [1, 2, 3, 4, 5]
let doubled = nums.map { $0 * 2 }
let summed  = nums.reduce(0) { $0 + $1 }
print("doubled=\(doubled), sum=\(summed)")
```

## 3 · KaTeX（數學公式）

行內：交叉熵的梯度為 \\(\nabla_\theta \mathcal{L} = -\sum_i y_i \nabla_\theta \log \hat{y}_i\\)，softmax 定義為 \\(\sigma(z)_j = e^{z_j} / \sum_k e^{z_k}\\)。

行間 — 縮放點積注意力：

$$
\text{Attention}(Q, K, V) = \text{softmax}\!\left( \frac{Q K^\top}{\sqrt{d_k}} \right) V
$$

方括號 — 貝氏：

$$
P(A \mid B) = \frac{P(B \mid A)\, P(A)}{P(B)}
$$

多行對齊：

$$
\begin{aligned}
  \mathcal{L}_\text{recon} &= \lVert x - \hat{x} \rVert_2^2 \\
  \mathcal{L}_\text{kl}    &= D_\text{KL}\!\left(q_\phi(z \mid x)\,\|\,p(z)\right) \\
  \mathcal{L}_\text{vae}   &= \mathcal{L}_\text{recon} + \beta \mathcal{L}_\text{kl}
\end{aligned}
$$

## 4 · Mermaid 圖表

流程圖：

{{< mermaid caption="按需載入決策樹。" >}}
graph TD
  A[頁面載入] --> B{有 pre.mermaid?}
  B -- 沒有 --> C[跳過 - 零成本]
  B -- 有 --> D[載入 mermaid ESM]
  D --> E[品牌主題初始化]
  E --> F[渲染圖表]
{{< /mermaid >}}

時序圖：

{{< mermaid caption="文章大圖模式的一次往返。" >}}
sequenceDiagram
  participant U as 使用者
  participant I as 圖片
  participant L as 大圖模式
  U->>I: 點擊
  I->>L: open(src, caption)
  L-->>U: 放大
  U->>L: ESC
  L-->>U: 關閉
{{< /mermaid >}}

狀態圖：

{{< mermaid caption="Live Photo 狀態機。" >}}
stateDiagram-v2
  [*] --> Idle
  Idle --> Ready: hover
  Ready --> Playing: video.play()
  Playing --> Idle: mouseleave
{{< /mermaid >}}

## 5 · Hugo Shortcodes

### 5.1 image-size

{{< image-size src="https://picsum.photos/seed/demoSingle/800/500" alt="範例圖替換文字" caption="image-size — 單圖 + caption + 點擊進入大圖模式。" center="true" >}}

### 5.2 image-grid

{{< image-grid columns="2" gap="1rem" images="https://picsum.photos/seed/demoGridA/800/500||範例圖 A, https://picsum.photos/seed/demoGridB/800/500||範例圖 B" >}}

### 5.3 image-carousel

{{< image-carousel
    width="90%"
    center="true"
    autoplay="false"
    caption="image-carousel — 手動切換，與大圖模式聯動。"
    images="https://picsum.photos/seed/demoCarA/800/500, https://picsum.photos/seed/demoCarB/800/500, https://picsum.photos/seed/demoCarC/800/500" >}}

### 5.4 live-photo

{{< live-photo src="/assets/live/disc-rotate.jpg" video="/assets/live/disc-rotate.mov" width="60%" center="true" caption="live-photo — hover 播放，大圖模式帶 LIVE 徽章。" >}}

[^1]: 腳註內容 — Goldmark 會在文末渲染為帶回連結的塊。

</div>
