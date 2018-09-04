# -*- coding: utf-8 -*-
import appex
import unicodedata
import clipboard


def erase_dakuten(char: chr) -> chr:
    myDict = {
        'が': 'か', 'ぎ': 'き', 'ぐ': 'く', 'げ': 'け', 'ご': 'こ',
        'ざ': 'さ', 'じ': 'し', 'ず': 'す', 'ぜ': 'せ', 'ぞ': 'そ',
        'だ': 'た', 'ぢ': 'ち', 'づ': 'つ', 'で': 'て', 'ど': 'と',
        'ば': 'は', 'び': 'ひ', 'ぶ': 'ふ', 'べ': 'へ', 'ぼ': 'ほ',
        'ガ': 'カ', 'ギ': 'キ', 'グ': 'ク', 'ゲ': 'ケ', 'ゴ': 'コ',
        'ザ': 'サ', 'ジ': 'シ', 'ズ': 'ス', 'ゼ': 'セ', 'ゾ': 'ソ',
        'ダ': 'タ', 'ヂ': 'チ', 'ヅ': 'ツ', 'デ': 'テ', 'ド': 'ト',
        'バ': 'ハ', 'ビ': 'ヒ', 'ブ': 'フ', 'ベ': 'ヘ', 'ボ': 'ホ',
    }

    if char in myDict.keys():
        return myDict[char]
    else:
        return char


def cnv_mr_fujiwara(str: str) -> str:
    cnvStr = ''

    for char in str:
        cnvStr += erase_dakuten(char)

        if char not in ['、', '。', '！', '？', '!', '?', 'ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ', 'っ', 'パ', 'ピ', 'プ', 'ペ', 'ポ', 'ッ']:
            cnvStr += '゛'

    return cnvStr


if __name__ == "__main__":
    input = appex.get_text()
    chars = list(input)
    output = cnv_mr_fujiwara(chars)

    print(output)
    clipboard.set(output)
