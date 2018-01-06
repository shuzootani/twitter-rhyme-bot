#!/usr/bin/python
# -*- coding: utf-8 -*-
import tweepy
import sys
import urllib
import urllib2

def get_oauth():
	consumer_key        = '9NbyzoGoAaew04IbBOPCZvvAG'
	consumer_secret     = 'J8u6yBBivKsZEnGocUZtl13UF43oGtYkuOj69CIMRhKMSxALWc'
	access_key          = '944885976194629632-u8359IoO1EWI60AaoypjuUnxeXCFjt5'
	access_secret       = '7aRxLnOWeQyuyPViXvHX91C3w9TNU8ViDDAcAukJ8PRrb'
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	return auth


def get_trends(api, woeid):
	place = api.trends_place(id=woeid)
	value = place[0][u'trends']
	for word in value:
		result = word[u'query'] #ワードの抽出
		result = urllib2.unquote(result).encode('raw_unicode_escape').decode('utf-8') #日本語にデコード
		result = result.replace("#","") #ハッシュタグ記号の削除
		print(result)
		

def main():
    auth = get_oauth()
    api = tweepy.API(auth_handler=auth)
    if len(sys.argv) >= 2:
        woeid = int(sys.argv[1])
    else:
        woeid = 23424856
    try:
        get_trends(api, woeid)
    except tweepy.error.TweepError:
        print('おそらく指定された場所のデータはありません。')
        exit()

main()

