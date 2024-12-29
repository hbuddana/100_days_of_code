from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys



# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window() # maximize window, because the search bar is not visible in the default window size 
driver.get("http://secure-retreat-92358.herokuapp.com")

# Find the "First Name" input element and type "John" in it
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("John")

# Find the "Last Name" input element and type "Doe" in it   
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Doe")

# Find the "Email" input element and type "
email = driver.find_element(By.NAME, "email")
email.send_keys("johndoe@gmail.com")

# Find the "Sign Up" button and click on it
sign_up = driver.find_element(By.CSS_SELECTOR, value="form button")

sign_up.click()

