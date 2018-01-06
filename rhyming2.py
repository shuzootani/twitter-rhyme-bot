import csv
import pandas as pd
from  pykakasi import kakasi


kakasi = kakasi()
kakasi.setMode('H', 'a')
kakasi.setMode('K', 'a')
kakasi.setMode('J', 'a')
conv = kakasi.getConverter()

clist = ['a', 'i', 'u', 'e', 'o', 'n']
keyc = []

df = pd.read_csv('dict_test.csv', encoding='SHIFT-JIS')

keyword = input('韻を踏みたいワードを入力してください。')
keyalf = conv.do(keyword) #ローマ字に変換
chars = list(keyalf) #1文字ずつにしてlistに格納
for n in chars:
    if n in clist:
        keyc.append(n)
    if n == '-':
        keyc.append(nlog)
    nlog = n

joined_keyc = ''.join(keyc) #配列を結合

count = 0
1stNum = 2

1stNum 
1stTxt = joined_keyc[0:1stNum-1]
print(1sttxt)
1stNum = 1stNum + 1

for n in df.ix[:, 1]:
    if

for n in df.ix[:, 1]:
    if n == joined_keyc:
        #print('「' + df.ix[count, 0] + '」と「' + keyword + '」で踏める')
        print('「{0}」と「{1}」で踏める'.format(keyword, df.ix[count, 0]))
    count = count + 1


print(joined_keyc)

