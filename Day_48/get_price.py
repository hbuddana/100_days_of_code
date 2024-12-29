# Description: This script will scrape the price of Item from a website 

from selenium import webdriver
from selenium.webdriver.common.by import By

# Set the path to the chromedriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Open Chrome browser
driver = webdriver.Chrome(options=chrome_options)    
driver.get("https://appbrewery.github.io/instant_pot/")

price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")

print(f"{price_dollar.text}.{price_cents.text}")