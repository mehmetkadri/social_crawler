import imp
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
import csv
from datetime import datetime

New_Chat_Bin = '/html/body/div[1]/div/div/div[3]/div/header/div[2]/div/span/div[2]/div/span'

Input_Txt_Box = '/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/div/div[2]/div/div[2]'

Online_Status_Label = '/html/body/div[1]/div/div/div[4]/div/header/div[2]/div[2]/span'

Targets = {'"Person"': '+90 xxx xxx xx xx'}

browser = webdriver.Chrome('chromedriver.exe')
 
browser.get("https://web.whatsapp.com/")
wait = WebDriverWait(browser, 600)

new_chat_title = wait.until(EC.presence_of_element_located((By.XPATH, New_Chat_Bin)))
new_chat_title.click()


while True:
    for target in Targets:
        tryAgain = True
        time.sleep(2)
        while (tryAgain):
            try:
                # Click on new chat button
                new_chat_title.click()
                # Wait untill input text box is visible
                input_box = wait.until(EC.presence_of_element_located((By.XPATH, Input_Txt_Box)))
                time.sleep(0.5)
                # Write phone number
                input_box.send_keys(Targets[target])
                time.sleep(1)
                # Press enter to confirm the phone number
                input_box.send_keys(Keys.ENTER)
                time.sleep(5)
                tryAgain = False
                try:
                    try:
                        browser.find_element_by_xpath(Online_Status_Label)
                        with open('berke.csv', 'a', encoding='UTF8', newline='') as f:
                            csv.writer(f).writerow(["Berke",datetime.now().strftime("%d/%m/%Y %H:%M:%S"),"online"])
                        time.sleep(1)
                        print(target + ' is online')
                    except:
                        with open('berke.csv', 'a', encoding='UTF8', newline='') as f:
                            csv.writer(f).writerow(["Berke",datetime.now().strftime("%d/%m/%Y %H:%M:%S"),"offline"])
                        time.sleep(1)
                        print(target + ' is offline')
                    time.sleep(1)
                except:
                    print('Exception 1')
                    time.sleep(10)
            except:
                print('Exception 2')
                time.sleep(4)