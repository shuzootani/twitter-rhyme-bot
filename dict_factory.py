#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append('./kana2boin.py')
import kana2boin
# import urllib
# import urllib2
# import MeCab
from os import system
import codecs
import re
import json

# Read files and Load data
f = open('dict.json', 'r')
boindex = json.load(f)

wd = open('word_dic.json', 'r')
dicts_with_boin = json.load(wd)

# chasen text file
system('chasen < ' + sys.argv[1] + ' > output.txt.chasen')

# 母音key付きの単語情報オブジェクトを配列にしてファイルに書き込む
for line in codecs.open('output.txt.chasen','r', 'utf-8'):
    line = line.rstrip('\r\n')
    if line == "EOS":
        pass
    else:
	try:
        lis = line.split("\t")
	    boin = kana2boin.convert2boin(lis[0].encode("utf-8"))
            if len(boin) > 0:
	            dicts_with_boin.append({"word": lis[0], "hinshi": lis[3], "boin": boin})
	except:
	    pass


# 母音と単語辞書のインデックスを格納したオブジェクトをファイルに書き込む
count = 0

for obj in dicts_with_boin:
    if obj["boin"]:
        boin = obj["boin"]
        if boin in boindex:
	    boindex[boin].append(count)
        else:
            boindex[boin] = []
            boindex[boin].append(count)
    else:
	pass

    count += 1

# Write into files
wd = open('word_dic.json', 'w')
json.dump(dicts_with_boin, wd)

f = open('dict.json', 'w')
json.dump(boindex, f)
