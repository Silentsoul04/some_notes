近乎完美的 Markdown 写作体验
=============================
## 什么是 Markdown
    Markdown 是一种轻量级标记语言，创始人为约翰·格鲁伯（John Gruber）。它允许人们“使用易读易写的纯文本格式编写文档，然后转换成有效的XHTML(或者HTML)文档”。 —— 来自维基百科

Markdown 创立的宗旨是实现「易读易写」。其语法简洁直观，你可以使用任何喜爱的文本编辑器来阅读和写作，更专注于书写的文字内容而不是排版样式。编辑完毕可轻松地导出成 HTML、PDF 等其它格式。

语法学习参考 : [Markdown 语法说明(简体中文版)](http://wowubuntu.com/markdown/)
## Sublime Text 3 以及 OmniMarkupPreviewer
    Sublime Text 是一套跨平台的文字編輯器，支持基於Python的外掛程式。Sublime Text 是專有軟體，可透過套件（Package）擴充本身的功能。大多數的套件使用自由軟體授權釋出，並由社群建置維護。 —— 来自维基百科 2

**Sublime Text** 作为近些年迅速崛起的后起之秀，凭借其精美的 UI 交互、完备的特色功能俘虏了一大批忠实用户。其风靡之势刺激了一些新老文本编辑器的重新思考和开发，开源实现 [Lime Text Editor](http://limetext.org/) 无需多说，Github 主导的 [Atom](http://limetext.org/) 以及号称下一代 Vim 编辑器的 neovim 都明确受到 Sublime Text 的影响。

而 **OmniMarkupPreviewer** 作为 Sublime Text 的一款强大插件，支持将标记语言渲染为 HTML 并在浏览器上实时预览，同时支持导出 HTML 源码文件。

* 支持的标记类语言:
    * Markdown
    * reStructuredText
    * WikiCreole
    * Textile
    * Pod (Requires Perl >= 5.10)
    * RDoc (Requires ruby in your PATH)
    * Org Mode (Requires ruby, and gem org-ruby should be installed)
    * MediaWiki (Requires ruby, as well as gem wikicloth)
    * AsciiDoc (Requires ruby, as well as gem asciidoctor)
    * Literate Haskell
## OmniMarkupPreviewer 设置详解
文章仅提供了简单的安装使用说明，以及个人较为关注的设置选项。

想了解更多相关信息，请点击文档内链接并参考脚注部分。
#### 安装和使用

**使用方法**: Sublime Text 内 Markdown 标签页点击鼠标右键 - 选择*Preview Current Markup in Browser*。 或者使用快捷键 (Ctrl+Alt+O) 来预览。

**详细设置**
OmniMarkupPreviewer 默认配置基本够用，但详细设置后才能将其特色功能充分发挥。

分享一下 *${packages}/User/OmniMarkupPreviewer.sublime-settings* 文件:

    ${packages} 路径为 */Users/ashfinal/Library/Application Support/Sublime Text 3/Packages/*
    注意用户账号替换。可通过点击菜单栏 Preferences - Browse Packages 打开其 Finder 窗口

```python
{
 "server_host": "192.168.1.100",
 "browser_command": ["open", "-a", "Google Chrome", "{url}"],
 // User public static files should be placed into
 // ${packages}/User/OmniMarkupPreviewer/public/
 // User templates should be placed into:
 // ${packages}/User/OmniMarkupPreviewer/templates/
 // Requires browser reload
 "html_template_name": "Evolution Yellow",
 // list of renderers to be ignored, case sensitive.
 // Valid renderers are: "CreoleRenderer", "MarkdownRenderer", "PodRenderer",
 // "RDocRenderer", "RstRenderer", "TextitleRenderer"
 // for example, to disable Textile and Pod renderer:
 // "ignored_renderers": ["TextitleRenderer", "PodRenderer"]
 "ignored_renderers": ["CreoleRenderer", "PodRenderer", "RDocRenderer", "TextitleRenderer", "LiterateHaskellRenderer"],
 "mathjax_enabled": false,
 // MarkdownRenderer options
 "renderer_options-MarkdownRenderer": {
 // Valid extensions:
 // - OFFICIAL (Python Markdown) -
 // "extra": Combines ["abbr", "attr_list", "def_list", "fenced_code", "footnotes", "tables", "smart_strong"]
 // For PHP Markdown Extra(http://michelf.ca/projects/php-markdown/extra/)
 // "abbr": http://packages.python.org/Markdown/extensions/abbreviations.html
 // "attr_list": http://packages.python.org/Markdown/extensions/attr_list.html
 // "def_list": http://packages.python.org/Markdown/extensions/definition_lists.html
 // "fenced_code": http://packages.python.org/Markdown/extensions/fenced_code_blocks.html
 // "footnotes": http://packages.python.org/Markdown/extensions/footnotes.html
 // "tables": http://packages.python.org/Markdown/extensions/tables.html
 // "smart_strong": http://packages.python.org/Markdown/extensions/smart_strong.html
 // "codehilite": http://packages.python.org/Markdown/extensions/code_hilite.html
 // "meta": http://packages.python.org/Markdown/extensions/meta_data.html
 // "toc": http://packages.python.org/Markdown/extensions/toc.html
 // "nl2br": http://packages.python.org/Markdown/extensions/nl2br.html
 // - 3RD PARTY -
 // "strikeout": Strikeout extension syntax - `This ~~is deleted text.~~`
 // "subscript": Subscript extension syntax - `This is water: H~2~O`
 // "superscript": Superscript extension syntax 0 `2^10^ = 1024`
 // "smarty" or "smartypants": Python-Markdown extension using smartypants to emit
 // typographically nicer ("curly") quotes, proper
 // ("em" and "en") dashes, etc.
 // See: http://daringfireball.net/projects/smartypants/
 // And: https://github.com/waylan/Python-Markdown/blob/master/docs/extensions/smarty.txt
 "extensions": ["extra", "codehilite", "toc", "strikeout", "smarty", "subscript", "superscript"]
 }
}
```
结合配置文件注释，来一起看下让 OmniMarkupPreviewer 更好用的诸多选项:
    "server_host": "192.168.1.100",
开启预览服务的 IP 地址, 默认为 localhost.

此处建议设置为本机固定 IP. 其好处在于：从局域网内的任意一台设备均可访问，可多设备同时在线，实现 一处编辑、多端预览 的效果。

你完全可以在 Mac 上编辑 Markdown 文档，而把 iPad 当作外接显示器来实时预览。

实际效果堪称完美，搞得我开始分外怀念已出手的 iPad ~ （；￣ェ￣）
    "browser_command": ["open", "-a", "Google Chrome", "{url}"],
预览默认为 Safari 浏览器，但一段时间下来发现最好使用 Google Chrome.
    "html_template_name": "Evolution Yellow",
预览使用的模板名称，默认为 Github.

此处为自定义模版 *Evolution Yellow*. 所谓模板其实就是非常简单的 CSS + HTML 文件，你可以修改背景、行宽、字体、边距 …… 等等样式相关的所有东西，甚至引入一些花哨的动画效果(你确定要这么做？)。

你可以在内置模板 Github 的基础上进行自定义，其路径为 *${packages}/OmniMarkupPreviewer/public/github.css, ${packages}/OmniMarkupPreviewer/templates/github.tpl*. 修改完毕后依据注释提示分别放到相关路径即可。
    "ignored_renderers": ["CreoleRenderer", "PodRenderer", "RDocRenderer", "TextitleRenderer", "LiterateHaskellRenderer"],
忽略/关闭的标记语言渲染器。

如前文介绍，OmniMarkupPreviewer 

支持的标记语言非常多，但是笔者接触的种类比较有限，所以此处只开启了 MarkdownRenderer 和 RstRenderer 渲染器。

    "mathjax_enabled": false,

强大的 JavaScript 引擎, 支持 LaTeX 编辑显示数学公式。

访问 MathJax 查看介绍及使用方法。不过笔者暂用不到这么高级的功能，所以此处禁用掉。

    "renderer_options-MarkdownRenderer": {
     "extensions": ["extra", "codehilite", "toc", "strikeout", "smarty", "subscript", "superscript"]
     }

Markdown 渲染扩展选项。

对比某些功能缺失的 Markdown 编辑器就知道 OmniMarkupPreviewer 的强大之处，简单说下：

