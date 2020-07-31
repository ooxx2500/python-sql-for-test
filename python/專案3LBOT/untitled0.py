# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:24:32 2020

@author: ASUS
"""

import requests , bs4 , os

url = 'https://www.mmkk.me/xinggan/4986.html'
moviehtml = requests.get(url)
objSoup = bs4.BeautifulSoup(moviehtml.text,'lxml')

photos = []
items = objSoup.find_all('div','post-item col-xs-6 col-sm-4 col-md-3 col-lg-2')
for item in items:
    photo = item.img['data-original']
    photos.append(photo)
    
destDir = r'‪C:\Users\莫再提\Desktop\new01'
if os.path.exists(destDir) == False:
    os.mkdir(destDir)
print('搜尋到的圖片數量 ＝',len(photos))
for photo in photos:
    picture = requests.get(photo)
    picture.raise_for_status()
    print('%s 圖片下載成功' % photo)
#先開啟檔案, 在儲存檔案
    pictFile = open(os.path.join(destDir,os.path.basename(photo)),'wb')
    for diskStorage in picture.iter_content(10240):
        pictFile.write(diskStorage)
    pictFile.close()