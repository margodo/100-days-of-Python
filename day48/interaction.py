from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('')

stats = driver.find_element(By.XPATH,value='/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[1]/div/div[3]/a[1]')
stats.click()
# all_portals = driver.find_element(By.LINK_TEXT,value='Pages')
# all_portals.click()

search = driver.find_element(By.NAME,value='search')
search.send_keys('bird', Keys.ENTER)

# driver.quit()