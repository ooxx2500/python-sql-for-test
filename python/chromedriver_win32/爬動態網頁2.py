# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 16:31:25 2020

@author: ASUS
"""



from selenium import webdriver
from bs4 import BeautifulSoup
driver_path = r'chromedriver.exe'
driver = webdriver.Chrome(driver_path)
driver.implicitly_wait(1)


driver.get('https://hahow.in/courses')
items=driver.find_elements_by_css_selector('h4.title')
driver.implicitly_wait(3)



for item in items:
    print(item.text)
driver.quit()









