#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 22:26:53 2018

@author: root
"""


import bs4 as bs
import urllib.request

# Getting the data
source = urllib.request.urlopen("https://en.wikipedia.org/wiki/Global_warming").read()

soup = bs.BeautifulSoup(source,"lxml")

text = "" 

for paragraph in soup.find_all("p"):
    text += paragraph.text

f = open("input.txt","w")
f.write(text)