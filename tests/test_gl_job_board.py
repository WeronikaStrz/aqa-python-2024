# Test - GlobalLogic jobboard website'.


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.globallogic.com/pl/")

title = driver.title
url = driver.current_url
print(title, url)
assert 1 == 2
# driver.implicitly_wait(1)
# title = driver.find_element(By.xpath, '//h1[@class="hero-content"]')
# print(title)
# offers_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Wszystkie oferty")
# offers_button.click()
# driver.implicitly_wait(1)
# title = driver.find_element_by_xpath('//h1[@class="hero-content"]').text
# driver.quit()
