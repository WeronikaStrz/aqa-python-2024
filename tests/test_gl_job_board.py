# Test - GlobalLogic jobboard website'.


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.globallogic.com/pl/")

title = driver.title
url = driver.current_url
print(title, url)
