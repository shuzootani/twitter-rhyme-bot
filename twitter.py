#!/usr/bin/python
# -*- coding: utf-8 -*-
import MeCab
import tweepy
import sys
sys.path.append('./kana2boin.py')
import kana2boin
import urllib
import urllib2
import json
import random
import time

# 読みのみを抽出するためのMecabTaggerインスタンスの生成
mecab = MeCab.Tagger('-Oyomi')

# TWITTER API AUTH CLIENT
def get_oauth():
	consumer_key        = ''
	consumer_secret     = ''
	access_key          = ''
	access_secret       = ''
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	return auth

def client_with_auth():
    auth = get_oauth()
    client = tweepy.API(auth_handler=auth)
    return client

# Twitterのトレンドワードを１０件取得
def get_trends(api, woeid):
	place = api.trends_place(id=woeid)
	value = place[0][u'trends']
        trends = []
	for word in value:
		result = word[u'query'] #ワードの抽出
		result = urllib2.unquote(result).encode('raw_unicode_escape').decode('utf-8') #日本語にデコード
		result = result.replace("#","") #ハッシュタグ記号の削除
		
		result = mecab.parse(result.encode("utf-8"))
		trends.append(result)

	return trends
	
TEXT = "Im Rhyme Bot n Vegitarian!! I eat salad n it\'s Better than Ramadan. バーガーばっかのお前はバーカー？ なら俺たちはラッパーサーバー　YEAH"
def tweet(text=TEXT):
    client = client_with_auth()
    try:
        client.update_status(text)
    except tweepy.error.TweepError as e:
        print e
        exit()


f = open('/home/s14178so/twitter_bot/dict.json', 'r')
dic = json.load(f)

wd = open('/home/s14178so/twitter_bot/word_dic.json', 'r')
word_dic = json.load(wd)

def search_index(boin):
    ids = []
    cuts = []
    rest = boin
    length = len(boin)

    while length > 0:
        if rest in dic:
            random_i = random_index(dic[rest])
            ids.append(random_i)

            if len(cuts) > 0:
                rest = ''.join(cuts)
                length = len(rest)
                cuts = []
            else:
                break
        else:
            cuts.insert(0, rest[len(rest)-1])
            rest = rest[0:len(rest)-1]
            length = len(rest)
    return ids

def search_words(ids):
    words = []
    for i in ids:
	words.append(word_dic[i]["word"])

    text = ('').join(words)
    return text

def random_index(arr_index):
    i = random.choice(arr_index)
    return i

def main():
    auth = get_oauth()
    api = tweepy.API(auth_handler=auth)
    if len(sys.argv) >= 2:
        woeid = int(sys.argv[1])
    else:
        woeid = 23424856
    try:
        trends = get_trends(api, woeid)
        boins = kana2boin.boin_boin(trends)
        for i, boin in enumerate(boins):
            if len(boin) >= 1 :
                ids = search_index(boin)
                rhyme_word = search_words(ids)           
	        text = '{0}と{1}で踏もうとする。やっちゃってる！？'.format(trends[i].strip(), rhyme_word.encode("utf-8"))
	        tweet(text)
                time.sleep(1)
    except tweepy.error.TweepError as e:
        print e
        exit()

main()
