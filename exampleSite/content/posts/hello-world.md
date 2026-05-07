---
title: "Hello, World"
slug: hello-world
date: '2026-01-01T00:00:00+00:00'
weight: 1
postId: hello
i18nKey: post.hello.title
categoryI18n: cat.notes
dateDisplay: 2026·01·01
bylineDate: 2026 · 01 · 01
kickers:
  en: NOTES · 2026
  zh: 笔记 · 2026
  tw: 筆記 · 2026
readTimes:
  en: 1 min read
  zh: 阅读约 1 分钟
  tw: 閱讀約 1 分鐘
heroCaption: F · 001 · HELLO
titles:
  en: "Hello, World"
  zh: "你好，世界"
  tw: "你好，世界"
decks:
  en: A minimal post that shows the multilingual lang-block convention. Replace the wrapper text and start writing.
  zh: 一篇最简的范文，展示多语言 lang-block 写法。替换里面的文字就能开写。
  tw: 一篇最簡的範文，展示多語言 lang-block 寫法。替換裡面的文字就能開寫。
prev:
  href: /posts.html
  title: ← All writing
next:
  href: /posts/feature-showcase.html
  title: Feature Showcase →
lastmod: '2026-01-01T00:00:00+00:00'
---

<div class="lang-block" data-lang="en" data-active="true">

## Welcome

Each post body must be wrapped in three `<div class="lang-block" data-lang="en|zh|tw">` containers. Mark exactly one as `data-active="true"` to be the default. The runtime in `_base.html` flips visibility on language switch.

Inline things work as expected: **bold**, *italic*, `code`, [links](https://gohugo.io), and <mark>highlights</mark>.

## Next

See `_draft-feature-test.md` for a one-page demo of every block this theme supports — Markdown, Prism syntax highlighting, KaTeX math, Mermaid diagrams, and all five image shortcodes.

</div>

<div class="lang-block" data-lang="zh">

## 欢迎

每篇文章正文必须包裹在三个 `<div class="lang-block" data-lang="en|zh|tw">` 容器里。仅在其中一个上标 `data-active="true"`，那个就是默认语言。运行时由 `_base.html` 处理语言切换。

行内格式如常：**粗体**、*斜体*、`code`、[链接](https://gohugo.io)、以及 <mark>高亮</mark>。

## 下一步

参见 `_draft-feature-test.md`——一页跑完主题支持的所有 block：Markdown、Prism 语法高亮、KaTeX 数学、Mermaid 图表，以及全部五个图片 shortcode。

</div>

<div class="lang-block" data-lang="tw">

## 歡迎

每篇文章正文必須包裹在三個 `<div class="lang-block" data-lang="en|zh|tw">` 容器裡。僅在其中一個上標 `data-active="true"`，那個就是預設語言。執行時由 `_base.html` 處理語言切換。

行內格式如常：**粗體**、*斜體*、`code`、[連結](https://gohugo.io)、以及 <mark>高亮</mark>。

## 下一步

參見 `_draft-feature-test.md`——一頁跑完主題支援的所有 block：Markdown、Prism 語法高亮、KaTeX 數學、Mermaid 圖表，以及全部五個圖片 shortcode。

</div>
