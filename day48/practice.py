from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://orteil.dashnet.org/experiments/cookie/')

timeout = time.time() + 5
five_mins = time.time() + 60*10

cookie = driver.find_element(By.ID, value='cookie')
cookie.click()

items = driver.find_elements(By.CSS_SELECTOR, value='#store div')
ids = [item.get_attribute('id') for item in items]

while True:
    cookie.click()
    if time.time() > timeout:
        all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store div b")
        prices = []
        for price in all_prices:
            price_value = price.text
            if price_value != "":
                cost = int(price_value.split("-")[1].strip().replace(",", ""))
                prices.append(cost)
        upgrades = {}
        for i in range(len(prices)):
            upgrades[prices[i]] = ids[i]
        cookie_balance = driver.find_element(by=By.ID, value="money").text
        if "," in cookie_balance:
            cookie_balance = cookie_balance.replace(",", "")
        cookies_amount = int(cookie_balance)
        available_upgrades = {}
        for price, id in upgrades.items():
            if cookies_amount > price:
                available_upgrades[price] = id
        if not available_upgrades:
            print('Not enough cookies for purchase')
            continue
        highest_price_affordable_upgrade = max(available_upgrades)
        purchase = available_upgrades[highest_price_affordable_upgrade]
        driver.find_element(by=By.ID, value=purchase).click()
        timeout = time.time() + 5
    if time.time() > five_mins:
        per_second = driver.find_element(by=By.ID, value="cps").text
        break
driver.quit()