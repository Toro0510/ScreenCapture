import time
import prtsc
import selenium_func
import pandas as pd

trade_no_df = pd.read_excel(r'C:\Users\jizeyuan\Desktop\sn号_前200单和总表copy_20200721.xlsx', sheet_name='前200单sn')
trade_no_df.info()


# selenium_func.web_auth_idba()
# time.sleep(1)
selenium_func.web_auth_stock()
time.sleep(1)
selenium_func.web_auth()


Ct = 0
for i, r in trade_no_df.iterrows():
    Ct += 1
    print(Ct, r['订单号'], r['user_name'])

    time.sleep(3)
    selenium_func.page_1(r['订单号'])
    time.sleep(3)
    selenium_func.m.click(105, 90)  # 点击侧边栏
    prtsc.prtsc(r['订单号'])

    time.sleep(3)
    selenium_func.page_2(r['订单号'])
    time.sleep(3)
    selenium_func.m.click(105, 90)  # 点击侧边栏
    # prtsc.prtsc(r['订单号'], r['user_name'], 2)
    time.sleep(3)

    time.sleep(3)
    selenium_func.page_3()
    time.sleep(3)
    prtsc.prtsc(r['订单号'], r['user_name'], 3)

    time.sleep(3)
    selenium_func.page_2_stock(r['订单号'])
    time.sleep(3)
    prtsc.prtsc(r['订单号'], r['user_name'], 2)

    time.sleep(1)
    selenium_func.driver.close()
    selenium_func.driver.switch_to.window(selenium_func.driver.window_handles[-1])
