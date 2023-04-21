#!/usr/bin/env python
# coding: utf-8

# # Web Scraping

# In[97]:


from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime
import csv 
import pandas as pd


# In[73]:


#connect to the website

url = 'https://www.pioneerdj.com/en-us/product/all-in-one-system/xdj-xz/black/overview/'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9"}

page = requests.get(url, headers = headers)

#parse the html

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

#find the product name and price based on id and class

title = soup2.find(id='product_name').get_text()
price = soup2.find(class_='hero-product__price').get_text()

print(title)
print(price)



# In[74]:


#strip the price and title to remove uneccessary spaces

price = price.strip()[1:]
title = title.strip()

print(title)
print(price)


# In[76]:


#get todays date when the script runs

today = datetime.date.today()

print(today)


# In[77]:


#create the dataset header and data

header = ['Title', 'Price', 'Date']
data = [title, price, today]

#create the initial csv file with header and data

#with open('WebScrapingDataset.csv', 'w', newline='', encoding='UTF8') as f:
    #writer = csv.writer(f)
    #writer.writerow(header)
    #writer.writerow(data)


# In[83]:


#use pandas to read the csv

df = pd.read_csv(r'C:\Users\kalde\WebScrapingDataset.csv')

print(df)


# In[82]:


#Append data to the csv

with open('WebScrapingDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[98]:


#put the script into a function

def check_price():
    url = 'https://www.pioneerdj.com/en-us/product/all-in-one-system/xdj-xz/black/overview/'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9"}

    page = requests.get(url, headers = headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

    title = soup2.find(id='product_name').get_text()
    
    price = soup2.find(class_='hero-product__price').get_text()
    
    price = price.strip()[1:]
    
    title = title.strip()
    
    today = datetime.date.today()

    header = ['Title', 'Price', 'Date']
    
    data = [title, price, today]
    
    with open('WebScrapingDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)


# In[113]:


#create a loop to run the function daily with time.sleep

while(True):
    check_price()
    time.sleep(86400)


# In[114]:


#read csv file

df = pd.read_csv(r'C:\Users\kalde\WebScrapingDataset.csv')

print(df)

