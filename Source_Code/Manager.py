from selenium import webdriver
from selenium.webdriver import ChromeOptions, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime


def login_account_1(driver):
    driver.get('https://login.aliexpress.com/seller.htm?flag=1&return_url=http%3A%2F%2Fgsp.aliexpress.com%2F')
    time.sleep(5)
    driver.switch_to.frame(driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/iframe'))
    username = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'fm-login-id')))
    username.send_keys('USERNAME_1')
    password = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'fm-login-password')))
    password.send_keys('PASSWORD_1)
    submit = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'fm-login-submit')))
    submit.click()


def login_account_2(driver):
    driver.get('https://login.aliexpress.com/seller.htm?flag=1&return_url=http%3A%2F%2Fgsp.aliexpress.com%2F')
    time.sleep(5)
    driver.switch_to.frame(driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/iframe'))
    username = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'fm-login-id')))
    username.send_keys('USERNAME_2')
    password = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'fm-login-password')))
    password.send_keys('PASSWORD_2')
    submit = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'fm-login-submit')))
    submit.click()


def one_day_customer_management(driver):
    time.sleep(5)
    driver.get('https://gsp.aliexpress.com/apps/crm/index')
    visited_days = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div/div[3]/div/div[2]/div[1]/span[2]')))
    visited_days.click()
    within_one_day = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div/div[3]/ul/li[1]/div')))
    within_one_day.click()
    search_within_one_day = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div/div[3]/div/div[2]/span/button')))
    search_within_one_day.click()
    classify_one_day = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div/div[4]/div/span/span/button')))
    classify_one_day.click()
    name_one_day = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/span/input')))
    name_one_day.send_keys('($35-2) (1_Day) ' + str(datetime.now().strftime('(%Y-%m-%d)')))
    OK_one_day_classification = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div[3]/button[1]')))
    OK_one_day_classification.click()


def one_day_customer_coupon_1(driver):
    time.sleep(5)
    driver.get('https://gsp.aliexpress.com/apps/crm/couponCreate')
    coupon_1 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div[2]/div/div/div/div/div/div/div[3]/div[1]/div/div/div/div/div[2]/div[2]/div[1]')))
    coupon_1.click()
    select = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div[2]/div/div/div/div/div/div/div[3]/div[1]/div/div/div/div/div[1]/div/div/div[1]/span[2]/button')))
    select.click()
    time.sleep(3)
    table_tr_one_td_one = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/div/div/div[3]/div/div/table/tbody/tr[1]/td[1]')))
    table_tr_one_td_one.click()
    OK = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div[2]/button[1]')))
    OK.click()
    time.sleep(3)
    confirm = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div[2]/div/div/div/div/div/div/div[3]/div[2]/div/div[1]/button')))
    confirm.click()


def main_program_account_1():
    options = ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)
    login_account_1(driver)
    one_day_customer_management(driver)
    one_day_customer_coupon_1(driver)


def main_program_account_2():
    options = ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)
    login_account_2(driver)
    one_day_customer_management(driver)
    one_day_customer_coupon_1(driver)


while True:
    if str(datetime.now().strftime('%H:%M:%S')) == '18:00:00':
        main_program_account_1()
        time.sleep(5)
        main_program_account_2()
    time.sleep(1)
