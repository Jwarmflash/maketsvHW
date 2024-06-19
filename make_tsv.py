# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 19:02:12 2024

@author: Jake Warmflash
"""
import os, hashlib, base64, requests
import urllib.request




PREFIX = 'https://raw.githubusercontent.com/Jwarmflash/books/main/'
BK_DIR = 'C:\\Users\\Jake Warmflash\\books'

books = []

for filename in os.listdir(BK_DIR):
  books.append(filename)


#build url[], get lengths content_len[]
url = []
content_len = []
base64_string = []
for i in books:
    file = PREFIX + i
    url.append(file)
    
    site = urllib.request.urlopen(file)
    meta = site.info()
    content_len.append(meta.get('Content-Length'))
    
    content = requests.get(file)
    hash = hashlib.md5(content.text.encode("utf-8")).digest()
    base64_string.append(base64.b64encode(hash))
    


#print(url)
#print(content_len)
#print(base64_string)

tsv = "TsvHttpData-1.0"
for i in range(len(url)):
    tsv = tsv + "\n" + url[i] + "\t" + content_len[i] + "\t" + str(base64_string[i])

with open("books.tsv", "w") as file:
  file.write(tsv)









