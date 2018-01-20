#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import sys
import urllib
import urllib2
# output
# ５文字以上のトレンドを配列に入れる。
# 母音と出力ワードのセット

def boin_boin(trends):
    rhymes = []
    for word in trends:
        if word:
            result = convert2boin(word)
            rhymes.append(result)
    return rhymes

def convert2boin(input_text):
    # 母音変換表
    kana2boin = {
        u'ア' :'a', u'イ' :'i', u'ウ' :'u', u'エ' :'e', u'オ' :'o',
        u'ァ' :'a', u'ィ' :'i', u'ゥ' :'u', u'ェ' :'e', u'ォ' :'o',
        u'カ' :'a', u'キ' :'i', u'ク' :'u', u'ケ' :'e', u'コ' :'o',
        u'サ' :'a', u'シ' :'i', u'ス' :'u', u'セ' :'e', u'ソ' :'o',
        u'タ' :'a', u'チ' :'i', u'ツ' :'u', u'テ' :'e', u'ト' :'o',
        u'ナ' :'a', u'ニ' :'i', u'ヌ' :'u', u'ネ' :'e', u'ノ' :'o',
        u'ハ' :'a', u'ヒ' :'i', u'フ' :'u', u'ヘ' :'e', u'ホ' :'o',
        u'マ' :'a', u'ミ' :'i', u'ム' :'u', u'メ' :'e', u'モ' :'o',
        u'ヤ' :'a', u'ユ' :'u', u'ヨ' :'o',
        u'ャ' :'a', u'ュ' :'u', u'ョ' :'o',
        u'ラ' :'a', u'リ' :'i', u'ル' :'u', u'レ' :'e', u'ロ' :'o',
        u'ワ' :'a', u'ヲ' :'o', u'ン' :'n', u'ヴ' :'u',
        u'ガ' :'a', u'ギ' :'i', u'グ' :'u', u'ゲ' :'e', u'ゴ' :'o',
        u'ザ' :'a', u'ジ' :'i', u'ズ' :'u', u'ゼ' :'e', u'ゾ' :'o',
        u'ダ' :'a', u'ヂ' :'i', u'ヅ' :'u', u'デ' :'e', u'ド' :'o',
        u'バ' :'a', u'ビ' :'i', u'ブ' :'u', u'ベ' :'e', u'ボ' :'o',
        u'パ' :'a', u'ピ' :'i', u'プ' :'u', u'ペ' :'e', u'ポ' :'o',
        u'ッ' :'ts'
    }

    #小文字は一つ前の文字とセットで一つの母音に変換する ex) シャ(シ+ャ) -> a
    little = [
		u"ぁ", u"ぃ", u"ぅ", u"ぇ", u"ぉ",
            	u"っ", u"ゃ", u"ゅ", u"ょ", u"ゎ",
            	u"ァ", u"ィ", u"ゥ", u"ェ", u"ォ",
            	u"ャ", u"ュ", u"ョ", u"ヮ",
    ]

    #伸ばし棒を前の言葉に置換（アー→アア）
    long_vowels = [u"ー", u"-", u"〜", u"~"]

    boins = []

    text = input_text.rstrip()
	
    print text
    for cut in unicode(text, "utf-8"):
	try:
	    if cut in little:
                boins.pop(len(boins)-1)
                boins.append(kana2boin[cut])

            elif cut in long_vowels: 
                last = boins[len(boins)-1]
                boins.append(last)

            else:
                boins.append(kana2boin[cut])
        except:
            pass

    boin = ('').join(boins)
    print boin
    return boin
