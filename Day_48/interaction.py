from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys



# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window() # maximize window, because the search bar is not visible in the default window size 
driver.get("https://en.wikipedia.org/wiki/Main_Page")


# Click on the article count
#article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
#article_count.click()

# Find element by link text
#all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
#all_portals.click()

# Find the "Search" input element and type "Python" in it and press Enter
search = driver.find_element(By.NAME, "search")
search.send_keys("Python", Keys.ENTER)


