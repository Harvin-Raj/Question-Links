import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Selenium Webdriver
s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)

url = "https://leetcode.com/problemset/all/?page="

def get_all_links(url2):
    driver.get(url2)
    time.sleep(7)

    arr = driver.find_elements(By.TAG_NAME, "a")

    links = []
    pattern = "/problems"

    

    for i in arr:
        try:
            href = i.get_attribute('href')
            if href and pattern in href:
                links.append(href)
        except Exception:
            pass

    links = list(set(links))
    return links

# Calling get links for all 55 pages
final_links = []

for page_number in range(1, 60):
    url1 = url + str(page_number)
    print(url1)
    final_links += get_all_links(url1)
final_links = list(set(final_links))

# Now we can store these links in a txt file

# Open txt file lc.txt in write mode with UTF-8 encoding
# print(len(final_links))
with open('lc.txt', 'a', encoding='utf-8') as file:
    for link in final_links:
        file.write(link)
        file.write('\n')
driver.quit()
