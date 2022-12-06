# Author: Phuong Le
# Email: ptle@umass.edu
# Spire ID: 33596966
import string
import urllib.request
import re

def read_article_file(url):
    req = urllib.request.urlopen(url)
    text = req.read()
    text = text.decode('UTF-8')
    return text

def text_to_article_list(text):
    article_list = re.split('<NEW ARTICLE>', text)
    article_list.pop(0)
    return article_list

def split_words(text):
    each = text.splitlines()
    a=[]
    for i in each:
        b=i.split()
        for j in b:
            a.append(j)
    return a

def scrub_word(text):
    return text.strip(string.punctuation)

def scrub_words(words):
    a=[]
    if words=="":
        return
    else:
        b=words.lower()
        c=b.strip()
        d=scrub_word(c)
        return d
