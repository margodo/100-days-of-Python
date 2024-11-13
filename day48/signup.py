from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('')

first_name = driver.find_element(By.NAME,value='fName')
last_name =driver.find_element(By.NAME,value='lName')
email = driver.find_element(By.NAME,value='email')

button = driver.find_element(By.CSS_SELECTOR,value='button')

first_name.send_keys('T')
last_name.send_keys('D')
email.send_keys('test@email.com')
button.click()