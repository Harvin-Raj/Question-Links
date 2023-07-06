import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup


# Define the chromedriver service
s = Service('chromedriver.exe')
# Instantiate the webdriver
driver = webdriver.Chrome(service=s)

HEADING_CLASS=".mr-2.text-label-1"
BODY_CLASS=".px-5.pt-4"
INDEX=1
QDATA_FOLDER = "Qdata"


def get_array_of_links():
    arr = []  # Array to store the lines of the file
    # Open the file
    with open("lc_problems.txt", "r",encoding='utf-8') as file:
        # Read each line one by one
        for line in file:
            arr.append(line)
    return arr


def add_text_to_index_file(text):
    index_file_path = os.path.join(QDATA_FOLDER, "index.txt")
    with open(index_file_path, "a",encoding='utf-8') as index_file:
        index_file.write(text + "\n")

def add_link_to_Qlink_file(text):
    index_file_path = os.path.join(QDATA_FOLDER, "Qlink.txt")
    with open(index_file_path, "a", encoding="utf-8", errors="ignore") as Qlink_file:
        Qlink_file.write(text)


def create_and_add_text_to_file(file_name, text):
    folder_path = os.path.join(QDATA_FOLDER, file_name)
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, file_name + ".txt")
    with open(file_path, "w", encoding="utf-8", errors="ignore") as new_file:
        new_file.write(text)


def getPageData(url,link_index):
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, BODY_CLASS)))
        time.sleep(1)
        heading = driver.find_element(By.CSS_SELECTOR, HEADING_CLASS)
        body = driver.find_element(By.CSS_SELECTOR, BODY_CLASS)
        print(heading.text)
        if heading.text:
            add_text_to_index_file(heading.text)
            add_link_to_Qlink_file(url)
            create_and_add_text_to_file(str(link_index), body.text)
        time.sleep(1)
        return True
    except Exception as e:
        print(e)
        return False


links= get_array_of_links()
for link in links:
    SUCCESS = getPageData(link, INDEX)
    if SUCCESS:
        INDEX = INDEX + 1


driver.quit()
