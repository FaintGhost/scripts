# 导入 webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from datetime import date

# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys
import time

# 创建chrome启动选项
options = webdriver.ChromeOptions()

# 指定chrome启动类型为headless 并且禁用gpu
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('log-level=3')

# 调用环境变量指定的chrome浏览器创建浏览器对象
driver = webdriver.Chrome(options=options)


# XPath
anmelden_xpath = '//*[@id="logIn_btn"]'
usr_xpath = '//*[@id="field_user"]'
pwd_xpath = '//*[@id="field_pass"]'
studium_xpath = '//*[@id="link000452"]/a'
m_an_xpath = '//*[@id="link000461"]/a'
p_bereich_xpath = '//*[@id="contentSpacer_IE"]/ul/li[1]/a'
info_xpath = '//*[@id="contentSpacer_IE"]/ul/li[1]/a'
status_xpath = '//*[@id="contentSpacer_IE"]/table/tbody/tr[2]/td'

driver.get("https://almaweb.uni-leipzig.de/")

print("--start--")

username = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, usr_xpath)))
password = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, pwd_xpath)))
username.send_keys("yz56gyju")
password.send_keys("Zyw941231")
anmelden = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, anmelden_xpath)))
anmelden.click()
driver.save_screenshot("anmelden.png")

studium = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, studium_xpath)))
studium.click()
driver.save_screenshot("studium.png")

m_an = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, m_an_xpath)))
m_an.click()
driver.save_screenshot("m_an.png")

p_bereich = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, p_bereich_xpath)))
p_bereich.click()
driver.save_screenshot("p_bereich.png")

informatik = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, info_xpath)))
informatik.click()
driver.save_screenshot("informatik.png")

status = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, status_xpath)))
info = status.text

print(info)
