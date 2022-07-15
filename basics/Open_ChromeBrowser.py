from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service(executable_path='D:\\SeleniumDrivers\\chromedriver_win32\\chromedriver.exe')
driver=webdriver.Chrome(service=s)
driver.get("http://www.fb.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.close()