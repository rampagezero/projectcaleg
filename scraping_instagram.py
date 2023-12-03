from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
options=webdriver.ChromeOptions()
options.add_argument('user-data-dir=C:\\Users\\Dikadalin\\AppData\\Local\\Google\\Chrome\\User Data')
# options.add_argument('--headless=new')
driver=webdriver.Chrome(options=options)
driver.get('https://www.instagram.com/dolor_aksinyata')
ActionChains(driver).scroll_by_amount(0,200)
time.sleep(5)
post_1=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div[1]')
post_1.click()
time.sleep(3)
list_comment={}
for i in range(0,3):
    comments=driver.find_elements(By.CLASS_NAME,"_a9ym")
    pack_comment=[]
    for com in comments:
        pack_comment.append(com.text.replace('\n',' '))
    if i==0:
        next=driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button')
    else:
        next=driver.find_element(By.XPATH,'/html/body/div[5]/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button')
    list_comment[i]=pack_comment
    next.click()
    time.sleep(3)
print(list_comment)
import pandas as pd
print(list_comment)