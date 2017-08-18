#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Karl.Lv@outlook.com, KarlLv@126.com
# 18 August, 2017
#
from bs4 import BeautifulSoup
import bs4
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>

"""

soup = BeautifulSoup(html_doc, "lxml")
#soup = BeautifulSoup(open('index.html'), "lxml")

print(soup.name)
print(soup.title)
print(soup.title.attrs)
print("========================================")
print(soup.head)
print(soup.head.attrs)
print(soup.head.contents)
print(soup.head.contents[0])
print(soup.head.children)
print("========================================")
print("child")
for child in soup.body.children:
    print(child)
print("========================================")
print("descendants")
print("========================================")
for child in soup.descendants:
    print(child)
print("========================================")

print("========================================")
print("string")
print(soup.html.string)
print(soup.head.string)
print(soup.title.string)
print(soup.a)
print(type(soup.a))
print("========================================")
print("Comment")
if type(soup.a.string)==bs4.element.Comment:
    print(soup.a.string)
print("========================================")
#print(soup.a)
#print(soup.a)
print(soup.p)
print(soup.p.string)
print(type(soup.p.string))
print("========================================")
for string in soup.strings:
    print(repr(string))
print("========================================")
for string in soup.stripped_strings:
    print(repr(string))

print("========================================")
print("parent")
p = soup.p
print(p.parent.name)
print("========================================")
print("parents")
content = soup.head.title.string
for parent in content.parents:
    print(parent.name)
print("========================================")
print("next_sibling prev_sibling")
print(soup.p.next_sibling)
print("========================================")
print(soup.p.prev_sibling)
print("========================================")
print(soup.p.next_sibling.next_sibling)
print("========================================")
for sibling in soup.a.next_siblings:
    print(repr(sibling))
print("========================================")
print(soup.html.next_element)
print(soup.head.next_element)
print(soup.title.next_element)
print("========================================")
last_a_tag = soup.find("a", id="link3")
for element in last_a_tag.next_elements:
    print(repr(element))
print("========================================")
print("find_all")
print(soup.find_all('b'))
print(soup.find_all('a'))
print("========================================")
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
print(soup.find_all(["a", "b"]))
print("========================================")
for tag in soup.find_all(True):
    print(tag.name)
print("========================================")
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
print(soup.find_all(has_class_but_no_id))
print("========================================")
print(soup.find_all(id='link2'))
print("========================================")
print(soup.find_all(href=re.compile("elsie")))
print("========================================")
print(soup.find_all(href=re.compile("elsie"), id='link1'))
print("========================================")
print(soup.find_all("a", class_="sister"))
print("========================================")
print(soup.find_all(attrs={"data-foo": "value"}))
print("========================================")
print(soup.find_all(text="Elsie"))
print("========================================")
print(soup.find_all(text=["Tillie", "Elsie", "Lacie"]))
print("========================================")
print(soup.find_all(text=re.compile("Dormouse")))
print("========================================")
print(soup.find_all("a", limit=2))
print("========================================")
print(soup.select('.sister'))
print("========================================")
print(soup.select('#link1'))
print("========================================")
print(soup.select("head > title"))
print("========================================")
print(soup.select('a[href="http://example.com/elsie"]'))
print("========================================")
print(soup.select('p a[href="http://example.com/elsie"]'))
print("========================================")
print("========================================")
print(soup.p.attrs)
print(soup.p['class'])
print(soup.p.get('class'))
print("========================================")
soup.p['class']="newClass"
print(soup.p)
print(soup.prettify())
print("========================================")
del soup.p['class']
print(soup.p)
print("========================================")
print(soup.prettify())
print("========================================")
print(soup.html.string)
