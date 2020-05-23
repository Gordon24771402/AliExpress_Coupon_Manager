from selenium import webdriver
from selenium.webdriver import ChromeOptions, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)


def login(driver):
    time.sleep(3)
    driver.switch_to.frame(driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/iframe'))
    username = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'fm-login-id')))
    username.send_keys('USERNAME')
    password = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'fm-login-password')))
    password.send_keys('PASSWORD')
    submit = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'fm-login-submit')))
    submit.click()
    time.sleep(3)


driver.get('https://login.aliexpress.com/seller.htm?flag=1&return_url=http%3A%2F%2Fgsp.aliexpress.com%2F')
login(driver)
