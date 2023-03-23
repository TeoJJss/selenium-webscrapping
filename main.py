from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import io
from pyzbar.pyzbar import decode
from PIL import Image

# CHANGE THIS
path="SPM scan.png" #put your image file path here
ag="WB004A101" #put the student's examniation number

img = Image.open(path)
qr = decode(img)
url=""
for d in qr:
    if d.type == "QRCODE":
        url = d.data.decode()
        break

print("url: https://"+url)

options = Options()
options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--single-process')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(chrome_options=options)

driver.get("https://"+url)
driver.maximize_window() # For maximizing window
driver.implicitly_wait(20) # gives an implicit wait for 20 seconds

wait = WebDriverWait(driver, 10)
inp=driver.find_element("id", "ag") #input examination number

inp.click()
inp.send_keys(ag)
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