import time
import prtsc
import selenium_func
import pandas as pd

trade_no_df = pd.read_excel(r'C:\Users\jizeyuan\Desktop\sn号_前200单和总表copy_20200721.xlsx', sheet_name='前200单sn')
trade_no_df.info()


# selenium_func.web_auth_idba()
# time.sleep(1)
# selenium_func.web_auth_stock()
# time.sleep(1)
selenium_func.web_auth()


Ct = 0
for i, r in trade_no_df.iterrows():
    Ct += 1
    print(Ct, r['订单号'], r['user_name'])

    time.sleep(3)
    selenium_func.page_1(r['订单号'])
    time.sleep(3)
    selenium_func.m.click(105, 90)  # 点击侧边栏
    time.sleep(3)

    scrollHeight=selenium_func.driver.execute_script("return document.documentElement.scrollHeight")
    time.sleep(1)

    if scrollHeight <=1850:
        prtsc.prtsc_3(r['订单号'])

    else:
        prtsc.prtsc_4(r['订单号'], 1)
        time.sleep(3)
        selenium_func.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        # 滚动条移动至底部
        time.sleep(3)
        prtsc.prtsc_4(r['订单号'], 2)

selenium_func.driver.close()