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
    word_list=[]
    for (index, article) in enumerate(article_list):
        a=split_words(article)
        b=scrub_words(a)
        for i in b:
            if i not in word_list:
                word_list.append(i)
        word_list.sort()
        for j in word_list:
            if j not in not_sort:
                not_sort[j]={index+1}
            elif j in not_sort and j in article:
                not_sort[j].add(index+1)
            else:
                continue
    article_index=dict(sorted(not_sort.items()))
    return article_index
