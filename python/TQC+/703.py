# -*- coding: utf-8 -*-
"""
703
請撰寫一程式，輸入一些字串至數組（至少輸入五個字串），以字串"end"為結束點（數組中不包含
字串"end"）。接著輸出該數組，再分別顯示該數組的第一個元素到第三個元素和倒數三個元素。

3. 輸入輸出：
輸入說明
至少輸入五個字串至數組，直至end結束輸入

輸出說明
數組
該數組的前三個元素
該數組最後三個元素

輸入輸出範例
範例輸入
president
dean
chair
staff
teacher
student
end
範例輸出
('president', 'dean', 'chair', 'staff', 'teacher', 'student')
('president', 'dean', 'chair')
('staff', 'teacher', 'student')
"""


t=()
while True:
    n = input()
    if n =='end':
        break
    t+=(n,)
    
print(t)
print(t[0:3]) 
print(t[len(t)-3:]) 





