from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

s=Service("D:/Download/chromedriver-win32/chromedriver-win32/chromedriver.exe")

o=Options()
o.add_experimental_option(name="detach",value=True)

driver=webdriver.Chrome(service=s,options=o)

driver.get("https://www.smartprix.com/mobiles")

#Click on the exclude out of stock fitler in availability section
time.sleep(1)
driver.find_element(By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()

#Click on the Exclude Upcoming fitler in availability section
time.sleep(1)
driver.find_element(By.XPATH,value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()
time.sleep(2)

old_height=driver.execute_script('return document.body.scrollHeight')
while True:
    #Clicking on the load more button
    driver.find_element(By.CLASS_NAME,value='sm-load-more').click()
    time.sleep(1)

    new_height=driver.execute_script('return document.body.scrollHeight')

    print(old_height,new_height)
    if old_height == new_height:
        break
    old_height=new_height


#Getting the html content of the fully loaded page
html=driver.page_source

with open('smartBricks.html','w', encoding='utf-8') as f:  #encoding is defined as they me be corrector jo normly na smhj aye
    f.write(html)

#Now we can browse this html
#In jupiter