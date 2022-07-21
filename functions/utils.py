"""
defaultdict:
    ある関数に従ってdictを定義できる辞書型. 
    例えば, 
    a = defaultdict(list)
    とすれば,いちいち初期化することなく新しい要素keyについてa[key] = somethingとすることができる.
"""
from collections import defaultdict