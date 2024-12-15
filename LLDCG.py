# -*- coding: utf-8 -*-

import random
import time
from selenium.webdriver.common.by import By
from cyberKimi import response
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess
import re
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")


for c in range(3):
    try:
        cmd_path = 'C:\\Program Files\\Google\\Chrome\\Application'#找到自己电脑上的Chrome.exe所在的地址
        cmd = f'cmd /k "cd {cmd_path} && start chrome.exe --remote-debugging-port=9222"'
        subprocess.Popen(cmd, shell=True)
        driver = webdriver.Chrome(options=chrome_options)
        time.sleep(random.uniform(1, 3))
        driver.get ("http://mapp.nudt.edu.cn/home/index.do")
        time.sleep(random.uniform(1, 3))
        # 刷新当前页面，后面再考虑必要性，用来消除网络异常
        # driver.refresh()
        driver.find_element (By.NAME,"name").clear()
        driver.find_element (By.NAME,"name").send_keys ("woshishabi")    #"woshishabi"换为自己的用户名
        time.sleep(random.uniform(1, 3))
        driver.find_element (By.XPATH,'//input[@type="password"]').send_keys("123456") #"123456"换为自己的密码
        time.sleep(random.uniform(1, 3))
        driver.find_element(By.ID,"loginButtonId").click()
        time.sleep(random.uniform(5, 7))
        driver.find_element (By.XPATH,'/html/body/div[4]/div[2]/a').click()
        time.sleep(random.uniform(5, 7))
        driver.find_element (By.XPATH,'//*[@id="loginButtonId"]').click()
        time.sleep(random.uniform(5, 7))
        driver.find_element (By.XPATH,'//*[@id="402881ec703338ab017033400c3d0005"]/div/div/div/div/div[4]/div/div/button').click()
        
        
        for i in range(10):
            Ques = driver.find_element(By.XPATH,'/html/body/div[2]/div')
            answer = response(Ques.text)
            if("多选" in Ques.text ):
                choices = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
                if("A" in answer):
                    choices[0].click()
                if("B" in answer):
                    choices[1].click()
                if("C" in answer):
                    choices[2].click()
                if("D" in answer):
                    choices[3].click()
        
            elif("填空" in Ques.text):
                kongs = driver.find_elements(By.XPATH, '//input[@type="text"]')
                lens = len(kongs)
                if ("答案" in answer):
                    pattern = r'：([^；]+)'
                    answer = re.findall(pattern, answer)
                if("“" in answer):
                    answer= answer.replace("“", "").replace("”", "")
                if (lens > 1):
                    an_list =answer.split('；')
                    for j in range(lens):
                        kongs[j].send_keys(an_list[j])
                else:
                    kongs[0].send_keys(answer)
            elif("单选" in Ques.text):
                choices = driver.find_elements(By.XPATH, '//input[@type="radio"]')
                if("A" in answer):
                    choices[0].click()
                if("B" in answer):
                    choices[1].click()
                if("C" in answer):
                    choices[2].click()
                if("D" in answer):
                    choices[3].click()
            elif("判断" in Ques.text):
                choices = driver.find_elements(By.XPATH, '//input[@type="radio"]')
                if ("对" in answer):
                    choices[0].click()
                else:
                    choices[1].click()
        
            time.sleep(random.uniform(1, 3))#充值了五十才有这个频率，要不然很慢，一分钟只能写两题
            driver.find_element(By.ID,"submitBtnId").click()
            time.sleep(random.uniform(5, 10))
        driver.close()
    except Exception as e:
        print(f"发生错误：{e}")
        driver.close()