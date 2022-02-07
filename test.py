from selenium import webdriver
from selenium.webdriver.common.by import By
from getpass import getpass
import time


input_username = input('Username: ')
input_password = getpass('Password: ')

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(r'D:\chromedriver.exe', options=options)
driver.get('https://www.linkedin.com')
time.sleep(2)

username = driver.find_element(By.XPATH, "//input[@name='session_key']")
password = driver.find_element(By.XPATH, "//input[@name='session_password']")

username.send_keys(input_username)
password.send_keys(input_password)
time.sleep(2)

submit = driver.find_element(By.XPATH,"//button[@type='submit']").click()

for page in range(1,100):
	url = f'https://www.linkedin.com/search/results/people/?keywords=recruitment&origin=CLUSTER_EXPANSION&page={page}&position=2&searchId=d85c9635-d7a9-4cc8-867d-9d723ede8faa&sid=%2Ci9'
	driver.get(url)
	time.sleep(2)

	all_buttons = driver.find_elements(By.TAG_NAME,"button")
	connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]

	if connect_buttons:
		for btn in connect_buttons:
			driver.execute_script("arguments[0].click();", btn)
			time.sleep(2)
			send = driver.find_element(By.XPATH, "//button[@aria-label='Send now']")
			driver.execute_script("arguments[0].click();", send)
			close = driver.find_element(By.XPATH, "//button[@aria-label='Dismiss']")
			driver.execute_script("arguments[0].click();", close)
			time.sleep(2)
