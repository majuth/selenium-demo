from selenium import webdriver
url = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
driver = webdriver.Chrome()
driver.get(url)
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys("liverpool")
showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click()