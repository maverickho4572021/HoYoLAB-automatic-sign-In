# chrome driver url: "https://sites.google.com/chromium.org/driver/"
# pyinstaller -F --icon=D:\Coding\Python39\AutoSignIn\as1k9-f4nla-001.ico .\main.py
import os
import pickle
# import schedule
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By  # 用法 drive.find_element_by_id(By.ID, "YourID")
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

if os.path.exists("./data/cookies.pkl") is False:
    os.system(r'"{}\data\adpre.exe"'.format(os.getcwd()))
    while os.path.exists("./data/cookies.pkl") is False:
        pass
if os.path.exists("./data/lastsignindate.txt") is False:
    with open(f"./data/lastsignindate.txt", mode="w+", encoding="utf8") as txt_file:
        txt_file.write("0")

def sign_in():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # options.add_argument("--incognito") # 無痕
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    website = "https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481"
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(website)

    cookies = pickle.load(open("./data/cookies.pkl", "rb")) # 載入已經存取的cookie
    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.get(website)
    WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located)

    time.sleep(1)
    try:
        item = driver.find_element(By.CLASS_NAME, "components-home-assets-__sign-content_---active---36unD3")
        time.sleep(1)
        item.click()
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "components-common-common-dialog-__index_---title---xH8wpC"))
        )
        time.sleep(1)
    except NoSuchElementException:
        time.sleep(3)
        pass

    driver.quit()

# schedule.every().day.at("00:05").do(sign_in)

with open(f"./data/lastsignindate.txt", mode="r", encoding="utf8") as txt_file:
    date = txt_file.read()

while True:
    if str(time.localtime().tm_mday) != date:
        # schedule.run_pending()
        sign_in()
        with open(f"./data/lastsignindate.txt", mode="w", encoding="utf8") as txt_file:
            date = str(time.localtime().tm_mday)
            txt_file.write(date)
    time.sleep(1)