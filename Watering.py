import yaml

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


credentials = yaml.load(open('config.yml'))
url_water = credentials['url_water']
url_water = url_water

def wartering():
    chrome_options = Options()
    chrome_options.add_argument("window-size=1024,768")
    chrome_options.add_argument('headless')                 # 瀏覽器不提供可視化頁面
    chrome_options.add_argument('no-sandbox')               # 以最高權限運行
    chrome_options.add_argument('--start-maximized')        # 縮放縮放（全屏窗口）設置元素比較準確
    chrome_options.add_argument('--disable-gpu')            # 谷歌文檔說明需要加上這個屬性來規避bug
    chrome_options.add_argument('--window-size=1920,1080')  # 設置瀏覽器按鈕（窗口大小）
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path = 'chromedriver')
    wait = WebDriverWait(driver, 1)
    
    # # 澆花 
    url_water = credentials['url_water']
    url_water = url_water

    driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div/div[1]/a').click()