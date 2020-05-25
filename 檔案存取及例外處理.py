# -*- coding: utf-8 -*-
"""
Created on Mon May 25 09:16:12 2020

@author: ASUS
"""

'''
檔案存取及例外處理

檔案運作流程:1.使用open函式開啟檔案及設定模式
          2.使用write()寫入函式寫入檔案，read()讀取函式讀取資料
          3.使用關閉函式close()關閉檔案

開啟檔案:open()函式  格式open(開啟檔案的完整路徑 ,開啟模式'r' 'w' 'a')
開啟模式:r(讀取):檔案指標指向檔案開頭，如檔案不存在，會發生錯誤
       w(寫入):檔案指標指向檔案開頭，並會清除原本檔案的內容，如檔案不存在，w會建立新檔
       a(附加):檔案指標在原檔案的結尾，寫入的檔案會加在原檔後面，如檔案不存在，w會建立新檔
       #若存取的是二進位檔案，則將開啟模式參數後加個b('rb' 'wb' 'ab')
檔案的路徑:檔案路徑若未指定，則以當時執行的系統預設路徑作為存取依據
         若未給路徑，只給檔案名稱，自訂路徑程程式碼撰寫時路徑分隔符號以\\為主
       
讀取與寫入:
寫入模式:write('寫入的字串')
讀取模式:read():讀取所有的內容
        read(n):讀取n個字元
        readlines():也是讀取所有的內容，也就是所有的行
        readline():讀一行
       
        




'''







