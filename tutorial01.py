from bs4 import BeautifulSoup
html_doc = """
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

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
#操作文檔樹最簡單的方法就是告訴它你想獲取的tag的name.如果想獲取 <head> 標籤,只要用 soup.head :
print(soup.head)
print(soup.title)
#如果想要得到所有的<a>標籤,或是通過名字得到比一個tag更多的內容的時候,
# 就需要用到 Searching the tree 中描述的方法,比如: find_all()
# print(soup.body.find_all('a'))
p=soup.findAll('p')
print(p[0])
