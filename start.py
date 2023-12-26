from datetime import datetime
import os
import time
import json

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui

# Load the data from the JSON file
with open('data.json', 'r') as f:
    data = json.load(f)
    
message = data['messages']
persons = data['persons']

# .env file
load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

# Initialize the WebDriver
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options)
delay = WebDriverWait(driver, 10)

# Log in to Messenger
driver.get("https://www.messenger.com")
email_field = delay.until(EC.presence_of_element_located((By.ID, "email")))
time.sleep(1)
email_field.send_keys(email)
password_field = delay.until(EC.presence_of_element_located((By.ID, "pass")))
password_field.send_keys(password)
password_field.submit()

# Send the message
for person in persons:
    id = person['id']
    name= person['name']
    driver.get("https://www.messenger.com/t/" + id)
    time.sleep(1)
    chat_box_css = "div[aria-describedby]"
    chat_box = delay.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, chat_box_css))
    )
    chat_box.click()
    chat_box.send_keys(message[0])
    chat_box.send_keys(Keys.RETURN)
    print("Message sent to " + str(name))
    time.sleep(1)
