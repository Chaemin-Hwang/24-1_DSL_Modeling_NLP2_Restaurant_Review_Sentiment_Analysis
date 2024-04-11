#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install webdriver_manager')


# In[2]:


import pandas as pd 

df = pd.read_csv('링크.csv')


# In[61]:





# In[3]:


from selenium.webdriver.common.by import By
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from openpyxl import Workbook
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import datetime
from selenium.webdriver.chrome.service import Service
import requests

# Webdriver headless mode setting
options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

# BS4 setting for secondary access
session = requests.Session()
headers = {
    "User-Agent": "user value"}

retries = Retry(total=5,
                backoff_factor=0.1,
                status_forcelist=[500, 502, 503, 504])

session.mount('http://', HTTPAdapter(max_retries=retries))

# New xlsx file
now = datetime.datetime.now()
xlsx = Workbook()
list_sheet = xlsx.create_sheet('output')
list_sheet.append(['name','nickname', 'content', 'date', 'revisit'])

    #service=Service()
    #driver = webdriver.Chrome(service=service, options=options)


# In[22]:


def crwaling2(name,url):
    temp = []
    
    try:
        service=Service()
        driver = webdriver.Chrome(service=service, options=options)
        res = driver.get(url)
        driver.implicitly_wait(30)

    # Pagedown
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)

        try:
            while True:
                driver.find_element(By.CLASS_NAME, 'fvwqf').click()
                time.sleep(0.4)
        except Exception as e:
            print('finish')

        time.sleep(10)
        html = driver.page_source
        bs = BeautifulSoup(html, 'lxml')
        reviews = bs.select('li.owAeM')
        count = len(reviews)
        
        for i in range(count):
            r = reviews[i]
            content = r.select('.zPfVt')
            nickname = r.select('.P9EZi')
            name = name
            time.sleep(0.06)
            temp.append([name, nickname, content])
            
            time.sleep(0.06)
            
            if i == 500:
                print('500')
                tempdf = pd.DataFrame(temp, columns=['가게', '작성자', '리뷰'])
                df.to_csv('장만옥_500.csv', index=False, encoding='utf-8')
                
            if i == 700:
                print('700')
                tempdf = pd.DataFrame(temp, columns=['가게', '작성자', '리뷰'])
                df.to_csv('장만옥_700.csv', index=False, encoding='utf-8')

    except Exception as e:
        print(e)
        
    return temp
    
a = crwaling2('정통집 신촌점','https://m.place.naver.com/restaurant/1071728472/home?entry=pll')

