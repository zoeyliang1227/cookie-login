import json
import time
import yaml
import platform
import os
import datetime
import random
import sched

from threading import Timer
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

credentials = yaml.load(open('config.yml'))

hour = random.randint(7,12)
minute = random.randint(0,60)

def doSth():
    shoppee()
    print(u'這個程式要開始瘋狂的運轉啦')

def main(h=hour,m=minute):
    while True:
        now = datetime.datetime.now()
        # print(now.hour, now.minute)
        # print(h,m)
        if now.hour == h and now.minute == m:
            break
    
    doSth()

    # 每86400秒（1天），傳送1次
    t = Timer(86400, main)
    t.start()

    

def shoppee():
    # # 定時任務
    # num = random.randrange(1, 60)
    # now = datetime.datetime.now()
    # year = int(now.strftime('%Y'))
    # month = int(now.strftime('%m'))
    # day = int(now.strftime('%d'))
    # hour = int(now.strftime('%H'))
    # minute = int(now.strftime('%M'))
    # # sched_Timer=datetime.datetime(year,month,day,hour,num,num)
    # sched_Timer=datetime.datetime(year,month,day,hour,minute,10)
    # print(sched_Timer)
    # if now == sched_Timer:        
    chrome_options = Options()
    # # 關閉通知(是否顯示通知)
    prefs = {
        'profile.default_content_setting_values':
        {
            'notifications':2
        }
    }
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("window-size=1024,768")
    chrome_options.add_argument('headless')                 # 瀏覽器不提供可視化頁面
    chrome_options.add_argument('no-sandbox')               # 以最高權限運行
    chrome_options.add_argument('--start-maximized')        # 縮放縮放（全屏窗口）設置元素比較準確
    chrome_options.add_argument('--disable-gpu')            # 谷歌文檔說明需要加上這個屬性來規避bug
    chrome_options.add_argument('--window-size=1920,1080')  # 設置瀏覽器按鈕（窗口大小）
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path = 'chromedriver')
    wait = WebDriverWait(driver, 1)
    ##登入蝦皮
    url = credentials['url']
    login_url = url
    #登入前清楚所有cookie
    driver.delete_all_cookies()
    driver.get(login_url)
    # #點選登入按鈕
    # driver.find_element_by_xpath('//*[@id="modal"]/div/div/div[2]/div').click()
    # driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/div[1]/div/ul/a[3]').click()
    # time.sleep(2)
    # username = credentials['login']['username']
    # user = driver.find_element_by_name('loginKey').send_keys(username)
    # password = credentials['login']['password']
    # pwd = driver.find_element_by_name('password').send_keys(password)
    # time.sleep(2)
    # submit = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/form/div/div[2]/button').click()
    # time.sleep(30)
    ### 獲取cookie
    # cookie = driver.get_cookies()
    # print(cookie)
    # print('獲取cookie')
    # jsonCookies = json.dumps(cookie)
    # with open('cookie.json', 'w') as f:
    #     f.write(jsonCookies)
    # time.sleep(30)
    with open('cookie.json', 'r') as f:
        data = json.loads(f.read())
    for c in data:
        driver.add_cookie(c)
    # # 重新整理頁面
    driver.refresh()
    print('登入成功')
    time.sleep(5)
    # #點選登入按鈕
    # driver.find_element_by_xpath('//*[@id="modal"]/div/div/div[2]/div').click()
    #按每日登入
    if url == login_url:
        # elem = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/div[1]/div/ul/li[2]/div/div/div/div[2]')
        # ActionChains(driver).move_to_element(elem).perform()
        # elem.click()
        # driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/div[1]/div/ul/li[2]/div/div/div').click()
        driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[1]/div[2]/div[5]/div[1]/a/div[2]/span').click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, '_2PrmO9')))
        driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div/div[1]/a').click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'pcmall-coinsrewardpage_3-cfpb')))
        driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/div/main/section[1]/div[1]/button').click()
    else:
        raise TypeError('wrong')
        
def wartering():
    driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div/div[1]/a').click()

main()