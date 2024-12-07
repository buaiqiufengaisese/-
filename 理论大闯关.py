# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 00:07:35 2024

@author: n
"""
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
def count_parentheses(s):
    count = 0
    for char in s:
        if char == "（":
            count += 1
    return count

for j in range(10):                         #"10"是刷题的次数，可改，一般一次能的两分以上，十次大概率足够
    try:
        driver = webdriver.Edge()           #'Edge'可换为其他浏览器，如'Chrome'
        driver.get ("http://mapp.nudt.edu.cn/login/webPage.html")
        driver.find_element (By.NAME,"name").send_keys ("sunjiawei")    #"sunjiawei"换为自己的用户名
        driver.find_element (By.XPATH,'//input[@type="password"]').send_keys("123456") #"123456"换为自己的密码
        driver.find_element(By.ID,"loginButtonId").click()
        driver.find_element (By.XPATH,'/html/body/div[4]/div[2]/a').click()
        time.sleep(1)
        driver.find_element (By.XPATH,'//*[@id="loginButtonId"]').click()
        time.sleep(1)
        driver.find_element (By.XPATH,'//*[@id="402881ec703338ab017033400c3d0005"]/div/div/div/div/div[4]/div/div/button').click()
        for i in range(10):
            info = driver.find_element(By.CLASS_NAME, "side_unit_info")
            if("多选" in info.text):
                info2 = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]')
                text = info2.text
                c= count_parentheses(text)
                choices = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
                if(c == 2):
                    numbers = [0, 1, 2, 3]
                    random_numbers = random.sample(numbers, 2)
                    result_list = list(random_numbers)
                    for num in result_list:
                        choices[num].click()
                        time.sleep(1)
                elif(c == 3):
                    numbers = [0, 1, 2, 3]
                    random_numbers = random.sample(numbers, 3)
                    result_list = list(random_numbers)
                    for num in result_list:
                        choices[num].click()
                        time.sleep(1)
                else:
                    
                    for choice in choices:
                        choice.click()
                        time.sleep(1)

            elif("填空" in info.text):
                pass
            else:
                choices = driver.find_elements(By.XPATH, '//input[@type="radio"]')
                if len(choices) == 2:
                    choices[0].click()
                else:
                    random_number = random.randint(0, 3)
                    choices[random_number].click()
                
            time.sleep(1)
            driver.find_element(By.ID,"submitBtnId").click()
            time.sleep(1)
        driver.quit()
        time.sleep(1)
    except Exception as e:
        print(f"发生错误：{e}")
        driver.quit()