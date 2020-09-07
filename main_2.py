import time
import prtsc
import selenium_func
import pandas as pd

trade_no_df = pd.read_excel(r'C:\Users\jizeyuan\Desktop\sn号_前200单和总表copy_20200721.xlsx', sheet_name='前200单sn')
trade_no_df.info()

selenium_func.web_auth_riskp()
time.sleep(5)

Ct = 0
for i, r in trade_no_df.iterrows():
    Ct += 1
    print(Ct, r['订单号'], r['user_name'])

    selenium_func.page_5(r['订单号'])
    time.sleep(3)
    selenium_func.driver.execute_script("document.body.style.zoom='0.5'")
    time.sleep(3)
    prtsc.prtsc(r['订单号'], r['user_name'], '5_1')

    div = selenium_func.driver.find_element_by_xpath('/html/body/div/div/div/div/div[6]/div')
    # 滑动滚动条到某个指定的元素
    js = "arguments[0].scrollIntoView();"
    # 将下拉滑动条滑动到当前div区域
    selenium_func.driver.execute_script(js, div)
    time.sleep(3)
    prtsc.prtsc(r['订单号'], r['user_name'], '5_2')

    # selenium_func.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # # 滚动条移动至底部
    # time.sleep(3)
    # prtsc.prtsc(r['订单号'], r['user_name'], '5_3')
