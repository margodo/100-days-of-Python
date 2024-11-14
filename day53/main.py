from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('')

links_elements = driver.find_elements(By.CSS_SELECTOR,value='.StyledPropertyCardDataWrapper a')
links = [element.get_attribute('href') for element in links_elements]

price_elements = driver.find_elements(By.CSS_SELECTOR,value='.PropertyCardWrapper span')
prices = [price.text.split('+')[0].split('/')[0] for price in price_elements]

addr_elements = driver.find_elements(By.CSS_SELECTOR,value='address')
addresses = [address.text.strip().replace('|','') for address in addr_elements]

driver.quit()

driver = webdriver.Chrome(options=chrome_options)

for i in range(len(links_elements)):
    driver.get('')
    addr_input = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    addr_input.send_keys(addresses[i])
    price_input.send_keys(prices[i])
    link_input.send_keys(links[i])
    submit_button.click()

driver.quit()
