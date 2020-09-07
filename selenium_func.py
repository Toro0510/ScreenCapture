from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pymouse import *
from pykeyboard import *
import time

chrome_opt = Options()  # 创建参数设置对象.
# chrome_opt.add_argument('--headless')   # 无界面化.
# chrome_opt.add_argument('--disable-gpu')    # 配合上面的无界面化.
chrome_opt.add_argument('--start-maximized')
chrome_opt.add_argument('--hide-scrollbars')
# chrome_opt.add_argument('--window-size=1920,1080')  # 设置窗口大小, 窗口大小会有影响.
# chrome_opt.add_argument('–disable-javascript')   # 禁用javascript
chrome_opt.add_experimental_option('excludeSwitches', ['enable-automation'])  # 去除Chrome开发者模式

m = PyMouse()
k = PyKeyboard()
driver = webdriver.Chrome(options=chrome_opt)


def web_auth():
    driver.get('http://erp.xianghuanji.com/')
    time.sleep(3)
    driver.find_element_by_id('username').send_keys('zeyuan.ji')
    driver.find_element_by_id('password').send_keys('Abcd@1234')
    driver.find_element_by_css_selector("button").click()


def web_auth_stock():
    driver.get('http://stock.xianghuanji.com/')
    time.sleep(3)
    driver.find_element_by_id('username').send_keys('zeyuan.ji')
    driver.find_element_by_id('password').send_keys('Abcd@1234')
    driver.find_element_by_css_selector("button").click()


def web_auth_idba():
    driver.get('http://idba.xianghuanji.com/')
    time.sleep(3)
    driver.find_element_by_id('username').send_keys('zeyuan.ji')
    driver.find_element_by_id('password').send_keys('Abcd@1234')
    driver.find_element_by_css_selector("button").click()


def web_auth_riskp():
    driver.get('http://riskp.xianghuanji.com/')
    time.sleep(3)
    driver.find_element_by_id('username').send_keys('zeyuan.ji')
    driver.find_element_by_id('password').send_keys('Abcd@1234')
    driver.find_element_by_css_selector("button").click()



def page_1(trade_no):
    driver.get('http://erp.xianghuanji.com/stock/delivery/finish-list')

    driver.find_element_by_name('trade_no').send_keys(str(trade_no))
    query_button = driver.find_element_by_xpath(
        "/html/body/div[5]/div/div[2]/div/div[1]/div/form/div[2]/div/div/div/button[1]")
    driver.execute_script("arguments[0].click();", query_button)

    query_button_2 = driver.find_element_by_xpath(
        "/html/body/div[5]/div/div[2]/div/div[2]/div/div/div[1]/table/tbody/tr[1]/td[16]/span[1]/a")
    driver.execute_script("arguments[0].click();", query_button_2)

    time.sleep(3)
    driver.execute_script("document.body.style.zoom='0.5'")

    # imgs = selenium_func.driver.find_elements_by_xpath("//img")
    # imgs_list = [i.get_attribute(name='src') for i in imgs][2:]
    # print(imgs_list)


def page_2(trade_no):
    driver.get('http://erp.xianghuanji.com/contract/list')

    driver.find_element_by_name('order_no').send_keys(str(trade_no))
    # 查询
    query_button = driver.find_element_by_xpath(
        "/html/body/div[5]/div/div[2]/div/div[1]/div/form/div[2]/div/div/div/button")
    driver.execute_script("arguments[0].click();", query_button)

    # 详情
    query_button_2 = driver.find_element_by_xpath(
        "/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div/div[1]/table/tbody/tr/td[11]/a")
    driver.execute_script("arguments[0].click();", query_button_2)

    # all_handles = selenium_func.driver.window_handles
    driver.switch_to.window(driver.window_handles[-1])

    time.sleep(5)
    driver.execute_script("document.body.style.zoom='0.5'")


def page_3():
    # tr = driver.find_elements_by_xpath("//td[a]")
    # tr[1].click()

    query_button_3 = driver.find_element_by_xpath(
        "/html/body/div[5]/div/div[2]/div/div[1]/div[1]/div[4]/div[2]/table/tbody/tr/td[4]/a")
    driver.execute_script("arguments[0].click();", query_button_3)


def page_2_stock(trade_no):
    url = r'http://stock.xianghuanji.com/admin/order/view?trade_no=' + str(trade_no)
    driver.get(url)

    time.sleep(5)
    driver.execute_script("document.body.style.zoom='0.65'")


def page_5(trade_no):
    url = r'http://riskp.xianghuanji.com/DebtCollect/tradeDetail?trade_no=' + str(trade_no)
    driver.get(url)