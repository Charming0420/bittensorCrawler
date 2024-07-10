import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--disable-gpu")

os.makedirs("CSVData", exist_ok=True)
download_path = os.path.join(os.getcwd(), "CSVData")

chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_path,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

#目標網站
url = "https://x.taostats.io/account/5GBnPzvPghS8AuCoo6bfnK7JUFHuyUhWSFD4woBNsKnPiEUi#transfers"
driver.get(url)

def click_element(selector):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
        )
        element.click()
        print(f"成功點擊元素: {selector}")
    except Exception as e:
        print(f"點擊元素失敗: {selector}, 錯誤: {e}")

def download_csv(page_number):
    try:
        button = driver.find_element(By.CSS_SELECTOR, "#root > div > div.css-fivcs8 > div > div:nth-child(3) > div > div:nth-child(2) > div.css-9czysj > button")
        driver.execute_script("arguments[0].scrollIntoView(true);", button)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(5)  
        print(f"下載 CSV 檔案: taoBinanceData{page_number}.csv")
    except Exception as e:
        print(f"下載檔案失敗: {e}")

def go_to_next_page(page_number):
    try:
        if page_number == 1:
            next_button_selector = "#root > div > div.css-fivcs8 > div > div:nth-child(3) > div > div:nth-child(2) > div.css-o6y4ip > div.css-132z9ia > div.css-19ype9z"
        else:
            next_button_selector = "#root > div > div.css-fivcs8 > div > div:nth-child(3) > div > div:nth-child(2) > div.css-o6y4ip > div.css-132z9ia > div:nth-child(2)"
        
        next_button = driver.find_element(By.CSS_SELECTOR, next_button_selector)
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
        driver.execute_script("arguments[0].click();", next_button)
        print(f"前往下一頁，頁數: {page_number + 1}")
    except Exception as e:
        print(f"前往下一頁失敗: {e}")

try:
    page_number = 1
    time.sleep(5) 
    click_element("#root > div > div.css-fivcs8 > div > div:nth-child(3) > div > div:nth-child(2) > div.css-1j0nwho > div > div > div > div:nth-child(5)")
    time.sleep(2)  

    while True:
        download_csv(page_number)
        time.sleep(5)  

        expected_page_number = page_number + 1
        go_to_next_page(page_number)
        time.sleep(5)  
        
        page_number += 1
except KeyboardInterrupt:
    print("停止爬蟲")
except Exception as e:
    print(f"發生錯誤: {e}")
finally:
    driver.quit()
    print("瀏覽器已關閉")