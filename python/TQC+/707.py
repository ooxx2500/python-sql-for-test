# -*- coding: utf-8 -*-
"""
Created on Thu May 28 20:44:29 2020

@author: 莫再提
"""
'''
 設計說明：

請撰寫一程式，輸入X組和Y組各自的科目至集合中，以字串"end"作為結束點（集合中不包含字串"end"）。請依序分行顯示(1) X組和Y組的所有科目、(2)X組和Y組的共同科目、(3)Y組有但X組沒有的科目，以及(4) X組和Y組彼此沒有的科目（不包含相同科目）。

    提示：科目須參考範例輸出樣本，依字母由小至大進行排序。

3. 輸入輸出：
輸入說明

輸入X組和Y組各自的科目至集合，直至end結束輸入
輸出說明

X組和Y組的所有科目
X組和Y組的共同科目
Y組有但X組沒有的科目
X組和Y組彼此沒有的科目（不包含相同科目）
輸入輸出範例
輸入與輸出會交雜如下，輸出的部份以粗體字表示

Enter group X's subjects:
Math
Literature
English
History
Geography
end
Enter group Y's subjects:
Math
Literature
Chinese
Physical
Chemistry
end
['Chemistry', 'Chinese', 'English', 'Geography', 'History', 'Literature', 'Math', 'Physical']
['Literature', 'Math']
['Chemistry', 'Chinese', 'Physical']
['Chemistry', 'Chinese', 'English', 'Geography', 'History', 'Physical']
'''


s1=set()
s2=set()


print("Enter group X's subjects:")
# TODO
x = input()
while x != 'end':
    s1.add(x)
    x = input()



print("Enter group Y's subjects:")
# TODO
y = input()
while y != 'end':
    s2.add(y)
    y = input()


a = s1|s2
b =s1&s2
c = s2-s1
d =s1^s2
a1=list(a)
b1=list(b)
c1=list(c)
d1=list(d)

a1.sort()
b1.sort()
c1.sort()
d1.sort()

print(a1)
print(b1)
print(c1)
print(d1)


















