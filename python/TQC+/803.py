# -*- coding: utf-8 -*-
"""
803
請撰寫一程式，讓使用者輸入一個句子（至少有五個詞，以空白隔開），並輸出該句子倒數三個詞。

3. 輸入輸出：
輸入說明
一個句子（至少五個詞，以空白隔開）

輸出說明
該句子倒數三個詞

輸入輸出範例
範例輸入
Many foreign students study in FJU
範例輸出
study in FJU
"""
a = input()

b = a.split(' ')


print(' '.join(b[len(b)-3:]))
