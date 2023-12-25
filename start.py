
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from dotenv import load_dotenv
import pyautogui
import time
import os

message = 'insert message here.'

convo = [
    #add convo id's here,
]

load_dotenv()
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

driver = webdriver.Edge()
driver.get("https://www.messenger.com")

email_field = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.ID, "email"))
)
time.sleep(3)
email_field.send_keys(email)
password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "pass"))
)
password_field.send_keys(password)
password_field.submit()

for i in convo:
    driver.get('https://www.messenger.com/t/' + i)
    time.sleep(3)
    pyautogui.write(message)
    pyautogui.press('enter')
    time.sleep(3)