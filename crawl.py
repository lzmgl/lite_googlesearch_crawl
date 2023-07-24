from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os
from selenium.webdriver.common.by import By

def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")

def crawling_img(name):
    driver=webdriver.Chrome('C://chromedriver.exe') #크롬 드라이버
    # driver = webdriver.Chrome()
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
    elem = driver.find_element(By.NAME,"q")
    elem.send_keys(name)
    elem.send_keys(Keys.RETURN)

    #
    SCROLL_PAUSE_TIME = 1
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")  # 브라우저의 높이를 자바스크립트로 찾음
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 브라우저 끝까지 스크롤을 내림
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_elements(By.CSS_SELECTOR,".mye4qd").click()
            except:
                break
        last_height = new_height

    imgs = driver.find_elements(By.CSS_SELECTOR,".rg_i.Q4LuWd") 
    dir = ".\idols" + "\\" + name

    createDirectory(dir) #폴더 생성
    count = 1
    for img in imgs:
        try:
            img.click()
            time.sleep(2)
            imgUrl = driver.find_element(By.XPATH,'/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]').get_attribute(
                "src")
            path = "C:\ITStudy\crawl\idols\\" + name + "\\"
            urllib.request.urlretrieve(imgUrl, path + name + str(count) + ".jpg")
            count = count + 1
            if count >= 260:
                break
        except:
            pass
    driver.close()
idols = ["이준혁 얼굴", "차서원 얼굴"]

for idol in idols:
    crawling_img(idol)