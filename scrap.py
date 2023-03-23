from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import io
from PIL import Image

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(chrome_options=options)

driver.get("https://gvs.moe.gov.my/qr/ACD96A047DD64E9A91D133960E92AE022A643F99CA")
driver.maximize_window() # For maximizing window
driver.implicitly_wait(20) # gives an implicit wait for 20 seconds

wait = WebDriverWait(driver, 10)
inp=driver.find_element("id", "ag") #input examination number

inp.click()
inp.send_keys("WB004A101")
submit = driver.find_element(By.XPATH, '//button[text()="Semak"]')
submit.click()
elem = driver.find_element("id", "rec")
# Get data after submit at the website
response = {
    "statusCode": 200,
    "body": elem.text
}
print(response)
driver.close()
driver.quit()

# return response