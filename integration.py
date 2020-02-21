from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

# driver = Chrome(executable_path='./chromedriver.exe')
driver = Chrome('/usr/bin/chromedriver')
driver.get('http://127.0.0.1:5000')
val = driver.find_element(By.ID, 'value')
assert val.text == '15'
print('Test Complete')

driver.quit()
