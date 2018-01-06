import re
import jaconv
import sys

def j2v_convert(text = sys.argv[1]):
    text = jaconv.hira2kata(text) #textをカタカナに
    text = list(text) #textを分解して配列に

    count = 0
    little =["ぁ", "ぃ", "ぅ", "ぇ", "ぉ",
            "っ", "ゃ", "ゅ", "ょ", "ゎ",
            "ァ", "ィ", "ゥ", "ェ", "ォ",
            "ッ", "ャ", "ュ", "ョ", "ヮ",
            ]

    for cut in text:        #ギャ→ャのような変換
        if cut in little:
            del text[count-1]
        count = count + 1

    count = 0
    for cut in text:        #伸ばし棒を前の言葉に置換（アー→アア）
        if cut in 'ー':
            text[count] = text[count-1]
        count = count + 1

    text = ''.join(text)        #配列を結合

    def multiple_replace(text, adict):

        rx = re.compile('|'.join(adict))
        def dedictkey(text):
            # マッチした文字列の元であるkeyを返す
            for key in adict.keys():
                if re.search(key, text):
                    return key

        def one_xlat(match):
            return adict[dedictkey(match.group(0))]

        return rx.sub(one_xlat, text)


    trans_tone = {
            'ア' :'a', 'イ' :'i', 'ウ' :'u', 'エ' :'e', 'オ' :'o',
            'ァ' :'a', 'ィ' :'i', 'ゥ' :'u', 'ェ' :'e', 'ォ' :'o',
            'カ' :'a', 'キ' :'i', 'ク' :'u', 'ケ' :'e', 'コ' :'o',
            'サ' :'a', 'シ' :'i', 'ス' :'u', 'セ' :'e', 'ソ' :'o',
            'タ' :'a', 'チ' :'i', 'ツ' :'u', 'テ' :'e', 'ト' :'o',
            'ナ' :'a', 'ニ' :'i', 'ヌ' :'u', 'ネ' :'e', 'ノ' :'o',
            'ハ' :'a', 'ヒ' :'i', 'フ' :'u', 'ヘ' :'e', 'ホ' :'o',
            'マ' :'a', 'ミ' :'i', 'ム' :'u', 'メ' :'e', 'モ' :'o',
            'ヤ' :'a', 'ユ' :'u', 'ヨ' :'o',
            'ャ' :'a', 'ュ' :'u', 'ョ' :'o',
            'ラ' :'a', 'リ' :'i', 'ル' :'u', 'レ' :'e', 'ロ' :'o',
            'ワ' :'a', 'ヲ' :'o', 'ン' :'n', 'ヴ' :'u',
            'ガ' :'a', 'ギ' :'i', 'グ' :'u', 'ゲ' :'e', 'ゴ' :'o',
            'ザ' :'a', 'ジ' :'i', 'ズ' :'u', 'ゼ' :'e', 'ゾ' :'o',
            'ダ' :'a', 'ヂ' :'i', 'ヅ' :'u', 'デ' :'e', 'ド' :'o',
            'バ' :'a', 'ビ' :'i', 'ブ' :'u', 'ベ' :'e', 'ボ' :'o',
            'パ' :'a', 'ピ' :'i', 'プ' :'u', 'ペ' :'e', 'ポ' :'o'
    }

    after = multiple_replace(text, trans_tone)
    return after
