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
    a = []
    for i in words:
        b = i.lower()
        c = b.strip()
        d = scrub_word(c)
        if d=="":
            continue
        else:
            a.append(d)
    return a

def build_article_index(article_list):
    not_sort={}
    for (index, article) in enumerate(article_list):
        a=split_words(article)
        b=scrub_words(a)
        for j in b:
            if j not in not_sort:
                not_sort[j]=set()
            not_sort[j].add(index)
    return not_sort

def find_words(keywords, index):
    intersect_docs = set()
    a=[]
    for i in keywords:
        for j in index[i]:
            if j not in a:
                a.append(j)
            else:
                intersect_docs.add(j)
    return intersect_docs
