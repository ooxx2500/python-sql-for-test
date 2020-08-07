from bs4 import BeautifulSoup
from selenium import webdriver
import time
driver_path = r'chromedriver.exe'
driver = webdriver.Chrome(driver_path)
driver.implicitly_wait(5)
driver.get('https://hahow.in/courses')

print(driver.title)

soup=BeautifulSoup(driver.page_source, 'lxml')

with open('hahow.html','w',encoding='utf-8')as fp:
    fp.write(soup.prettify())
    print("寫入檔案中....")
driver.quit()

#-------------------
#打開HTML刪除script直到能嫌上網不出線404
