from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#open chrome
driver = webdriver.Chrome()

#open instagram
driver.get("https://www.instagram.com/")
time.sleep(2)


############################# LOGIN #############################

username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")

username.send_keys("mehmt_kadri")
password.send_keys("simonvsthehomosapienagenda2015")

login = driver.find_element_by_xpath("//button[@type='submit']")
login.click()
time.sleep(5)

############################# FOLLOWERS #############################

#look at profile
driver.get("https://www.instagram.com/mehmt_kadri/")
time.sleep(2)

#look at followers
followers = driver.find_element_by_xpath("//a[@href='/mehmt_kadri/followers/']")
followers.click()
time.sleep(2)

#find the div with class named "_aano"
followers_div_or = driver.find_element_by_class_name("_aano")
#get inside the div inside followers div
followers_div = followers_div_or.find_element_by_tag_name("div")
#get inside the div inside followers div
followers_div = followers_div.find_element_by_tag_name("div")


#scroll down to load all followers
break_cond = 0
while True:
    break_cond=len(followers_div.text)
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_div_or)

    time.sleep(1)

    if len(followers_div.text)==break_cond:
        time.sleep(1)
        if len(followers_div.text)==break_cond:
            break


all_info_on_followers = followers_div.text.split("Remove\n")
followers = []
for info in all_info_on_followers:
    followers.append(info.split("\n")[0])

time.sleep(2)

############################# FOLLOWING #############################


#look at profile
driver.get("https://www.instagram.com/mehmt_kadri/")
time.sleep(2)

#look at following
following = driver.find_element_by_xpath("//a[@href='/mehmt_kadri/following/']")
following.click()
time.sleep(2)

#find the div with class named "_aano"
following_div_or = driver.find_element_by_class_name("_aano")
#get inside the div inside following div
following_div = following_div_or.find_element_by_tag_name("div")
#get inside the div inside following div
following_div = following_div.find_element_by_tag_name("div")

#scroll down to load all following
break_cond_2 = 0
while True:
    break_cond_2=len(following_div.text)
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", following_div_or)

    time.sleep(1)

    if len(following_div.text)==break_cond_2:
        time.sleep(1)
        if len(following_div.text)==break_cond_2:
            break


all_info_on_following = following_div.text.split("Following\n")
following = []
for info in all_info_on_following:
    following.append(info.split("\n")[0])

time.sleep(2)

############################# NOT FOLLOWING BACK #############################

#find people you follow but they don't follow you back
not_following_back = []
for person in following:
    if person not in followers:
        not_following_back.append(person)

print("People you follow but they don't follow you back:")
for person in not_following_back:
    print(person)

#close chrome
driver.close()
