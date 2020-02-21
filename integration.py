from selenium import webdriver
from selenium.webdriver.common.by import By


# driver = Chrome(executable_path='./chromedriver.exe')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)
driver.get('http://127.0.0.1:5000')
val = driver.find_element(By.ID, 'value')
assert val.text == '15'
print('Test Complete')

driver.quit()
