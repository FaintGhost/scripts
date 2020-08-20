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

# 调用环境变量指定的chrome浏览器创建浏览器对象
driver = webdriver.Chrome(options=options)

global today
today = date.today().strftime("%Y/%m/%d")
# choose = input("请输入你的选择:\n1.订座\n2.取消(已经预订)\n3.退出\n")
# if (choose == '1'):
#     login_process()
#     choice_process()
#     confirm()
#     result()
# if (choose == '2'):
#     cancel_process()

# un = input("请输入你的账号:")
# pwd = input("请输入你的密码:")
# lc = input("请输入校区:")
# area = input("请选择区域:")
# cond = input("请选择条件(mit Strom, PC, kein PC, LAN, Steharbeitsplatz)")
# date = input("请输入日期(格式2020/08/xx)")
# stime = input("起始时间(格式12:30)")
# etime = input("结束时间(格式23:45)")

best_area = ['38', '39', '40', '41', '42', '43']

# XPath
reserve_xpath = '//*[@id="startdiv"]/p[2]/a'
un_xpath = '//*[@id="readernumber"]'
pwd_xpath = '//*[@id="password"]'
login_xpath = '//*[@id="loginbtn"]'
accept_xpath = '//*[@id="startdiv"]/div/a[3]'
sto_xpath = '//*[@id="institution"]'
area_xpath = '//*[@id="area"]'
ausst_xpath = '//*[@id="fitting"]'
date_xpath = '//*[@id="from_date"]'
stime_xpath = '//*[@id="from_time"]'
etime_xpath = '//*[@id="until_time"]'
booking_xpath = '//*[@id="workspacebtn"]'
bkcode_xpath = '//*[@id="bookingCode"]'
seats_xpath = '//*[@id="booked_workspace"]'
tohome_xpath = '//*[@id="startdiv"]/button'
bkcinput_xpath = '//*[@id="bookingcode"]'
storno_xpath = '//*[@id="startdiv"]/p[3]/a'
cancelbtn_xpath = '//*[@id="stornobtn"]'

driver.get("https://seats.ub.uni-leipzig.de/")

print("--start--")
# get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)


def login_process():
    # 点击我要登陆
    reservieren = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, reserve_xpath)))
    reservieren.click()
    # 输入账号密码
    username = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, un_xpath)))
    password = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, pwd_xpath)))
    username.send_keys("009830-0")
    password.send_keys("31121994")
    # 登录
    login = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, login_xpath)))
    login.click()
    # 健康许可协议
    accept = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, accept_xpath)))
    driver.execute_script("arguments[0].scrollIntoView();", accept)
    # webdriver.ActionChains(driver).move_to_element(
    #     accept).click(accept).perform()
    accept.click()
    driver.save_screenshot("login_process.png")


def choice_process():
    # 选择校区
    standort = Select(WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, sto_xpath))))
    # standort.select_by_value(lc)
    # driver.execute_script("arguments[0].scrollIntoView();", standort)
    standort.select_by_value("Campus-Bibliothek")
    # 选择区域
    bereich = Select(WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, area_xpath))))
    # bereich.select_by_value(area)
    time.sleep(5)
    bereich.select_by_index(5)
    # 选择条件
    ausstattung = Select(WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, ausst_xpath))))
    # ausstattung.select_by_value(cond)
    ausstattung.select_by_value("kein PC")
    # 选择日期
    datum = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, date_xpath)))
    # datum.send_keys(date)
    datum.send_keys(today)
    driver.save_screenshot("date.png")
    # 开始时间
    fromtime = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, stime_xpath)))
    # fromtime.send_keys(stime)
    fromtime.send_keys("16:00")
    # 结束时间
    untiltime = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, etime_xpath)))
    # untiltime.send_keys(etime)
    untiltime.send_keys("23:00")
    driver.save_screenshot("choice_process.png")


def confirm_process():
    # 确认预定
    buchen = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, booking_xpath)))
    driver.execute_script("arguments[0].scrollIntoView();", buchen)
    # webdriver.ActionChains(driver).move_to_element(
    #     accept).click(accept).perform()
    driver.save_screenshot("final_confirm.png")
    buchen.click()


def result_process():
    try:
        WebDriverWait(driver, 10).until(EC.alert_is_present(), "alert timeout")
        alert_obj = driver.switch_to.alert
        msg = alert_obj.text
        print(msg)
        alert_obj.accept()
        print("alert accepted")
    except TimeoutException:
        print("booking successful")
        driver.save_screenshot("success_page.png")
        global bkcode
        bkcode = driver.find_element_by_id("bookingCode").text
        seatnumber = driver.find_element_by_id("booked_workspace").text
        # bkcode = WebDriverWait(driver, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, bkcode_xpath)))
        # seat = WebDriverWait(driver, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, seats_xpath)))
        if (seatnumber in best_area):
            print("it's in the best area")
            print("Your bookingcode is: " + bkcode)
            print("Your seat number is: " + seatnumber)
        elif (seatnumber not in best_area):
            time.sleep(1)
            cancel_process()
            print("but is not in the best area")
            print("this booking is canceled")


def cancel_process():
    zuruck = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, tohome_xpath)))
    zuruck.click()
    storno = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, storno_xpath)))
    storno.click()
    username1 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, un_xpath)))
    password1 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, pwd_xpath)))
    username1.send_keys(un)
    password1.send_keys(pwd)
    bkc = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, bkcinput_xpath)))
    bkc.send_keys(bkcode)
    cancel = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, cancelbtn_xpath)))
    cancel.click()
    WebDriverWait(driver, 10).until(EC.alert_is_present(), "alert timeout")
    alert_obj1 = driver.switch_to.alert
    msg1 = alert_obj1.text
    print(msg1)
    alert_obj1.accept()
    print("alert accepted")


def booking_loop():
    asdf


login_process()
choice_process()
confirm_process()
result_process()

print("--End--")
# driver.close()
