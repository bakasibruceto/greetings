from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()

driver.get("https://www.messenger.com")

email_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "email"))
)




# Type the email
email_field.send_keys('abla09027@gmail.com')

# Wait for the password input field to become visible
password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "pass"))
)

# Type the password
password_field.send_keys('pogisibruce69')

password_field.submit()




driver.get('https://www.messenger.com/t/7127472443947705/')

WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, "some-id-on-the-next-page"))
)