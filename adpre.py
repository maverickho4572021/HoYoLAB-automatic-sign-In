# pip install webdriver-manager
import pickle
import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


print("\n請先在Google Chrome上登入此網站:\nhttps://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481")
print("\n然後輸入你的電腦帳戶使用者名稱（假設你桌面路徑是 C:\\Users\\Eula\\Desktop ，就輸入Eula）:")

user = input()

while os.path.exists(r"C:/Users/{}".format(user)) is False:
    print("\n錯誤，請重新輸入你的電腦帳戶使用者名稱（假設你桌面路徑是 C:\\Users\\Eula\\Desktop ，就輸入Eula）:")
    user = input()

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument(r"user-data-dir=C:/Users/{}/AppData/Local/Google/Chrome/User Data".format(user))
driver = webdriver.Chrome(service=service, options=options)

website = "https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481"
driver.get(website)
WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located)

pickle.dump(driver.get_cookies(), open("./data/cookies.pkl","wb")) # 第一次就抓cookie來存，之後就讀取cookie免登入了
time.sleep(1)

driver.quit()