from selenium import webdriver
from selenium.webdriver.common.by import By
# Keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.python.org/')
#
# price = driver.find_element(By.CLASS_NAME,value='a-price-whole')
# price_cents = driver.find_element(By.CLASS_NAME,value='a-price-fraction')
# print(price.text,'.',price_cents.text)
# button=driver.find_element(By.ID,value='submit')
# print(button.size)
# doc_link = driver.find_element(By.CSS_SELECTOR,value='.documentation-widget a')
# driver.find_element(By.XPATH,value='/html/body/div[1]/div/div[9]/div[3]/div[4]/div[2]/div/a')
# # closes tab
# driver.close()
# # quit entire browser
events={}
events_pos_dates = driver.find_elements(By.CSS_SELECTOR,value='.event-widget time')

events_names = driver.find_elements(By.CSS_SELECTOR,value='.event-widget li a')

for i in range (0,len(events_names)-1):
    events[i] = {events_pos_dates[i].text: events_names[i].text}

print(events)
driver.quit()