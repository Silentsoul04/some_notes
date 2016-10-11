示例代码
```
html_doc=
"""
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
```

######find_all() == findAll()

* 用法:
```
find_all(tag, attributes, recursive, text, limit, keywords)
```
* 标签参数 tag 前面已经介绍过——你可以传一个标签的名称或多个标签名称组成的 Python列表做标签参数。
* 属性参数 attributes 是用一个 Python字典封装一个标签的若干属性和对应的属性值。
* 递归参数 recursive 是一个布尔变量。你想抓取 HTML 文档标签结构里多少层的信息？如果recursive 设置为 True ， findAll 就会根据你的要求去查找标签参数的所有子标签，以及子标签的子标签。如果 recursive 设置为 False ， findAll 就只查找文档的一级标签。默认是支持递归查找的
* 文本参数 text 有点不同，它是用标签的文本内容去匹配，而不是用标签的属性。
* 范围限制参数 limit ，显然只用于 findAll 方法。 find 其实等价于 findAll 的 limit 等于1 时的情形。如果你只对网页中获取的前 x 项结果感兴趣，就可以设置它。但是要注意，这个参数设置之后，获得的前几项结果是按照网页上的顺序排序的，未必是你想要的那前几项。
* 关键词参数 keyword ，可以让你选择那些具有指定属性的标签。

* 示例:
```
#返回一个包含 HTML 文档中所有标题标签的列表
.find_all({"h1","h2","h3","h4","h5","h6"})

# 下面这个函数会返回 HTML 文档里红色与绿色两种颜色的 span 标签：
.find_all("span", {"class":{"green", "red"}})

#查找前面网页中包含“the prince”内容的标签数量
.findAll(text="the prince")
print(len(nameList))

```

* 注：

>虽然关键词参数 keyword 在一些场景中很有用，但是，它是 BeautifulSoup 在
技术上做的一个冗余功能。

#####find()
* 用法
    * find(tag, attributes, recursive, text, keywords)