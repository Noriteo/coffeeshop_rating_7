#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests # 크롤링에 사용하는 패키지
from bs4 import BeautifulSoup # html 변환에 사용함

from selenium import webdriver
import time
from datetime import datetime


# In[12]:


driver = webdriver.Chrome('./chromedriver')


# In[13]:


url = 'https://naver.com'
driver.get(url)


# In[5]:


data = pd.read_csv('./data/Starbucks_t.csv')
data.head(20)


# In[6]:


data["keyword"] = "스타벅스" + " " + data['지점명']

data["keyword"][:20]


# In[6]:


data['별점'] = 0


# In[ ]:


star_starbucks = []

for i in enumerate()


# In[16]:


star_starbucks = []

for i in range(10):
    keyword = data['keyword'][i]
    seed = np.random.randint(100)
    np.random.seed(seed)
    a = np.random.randint(5)
    time.sleep(a)
    #스타벅스 무슨지점
    driver.find_element_by_xpath('//*[@id="query"]').send_keys(keyword)
    #클릭해
    driver.find_element_by_xpath('//*[@id="search_btn"]').click()
    #별가져와
    rate = driver.find_element_by_css_selector('span.rating').text
    data['별점'][i] = rate
    #네이버 클릭
    driver.find_element_by_xpath('//*[@id="header_wrap"]/div/div[1]/div[1]/div/h1/a/i').click()
    


# In[17]:


data


# In[ ]:




