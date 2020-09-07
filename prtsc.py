from PIL import ImageGrab
import os


def prtsc(trade_no, user_name, page_num):
    # str_1 = str(trade_no) + '_' + str(user_name)
    # str_2 = str(trade_no) + ' Page_' + str(page_num) + '.png'

    str_1 = str(trade_no)
    str_2 = ' Page_' + str(page_num) + '.png'

    file_path = r'C:\Users\jizeyuan\Desktop\订单物流截图\\' + str_1

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    img_1 = ImageGrab.grab(bbox=(0, 0, 1080, 1920))
    img_1.save(file_path + '\\' + str_2)


def prtsc_2(trade_no, user_name, page_num):
    # str_1 = str(trade_no) + '_' + str(user_name)
    # str_2 = str(trade_no) + ' Page_' + str(page_num) + '.png'

    str_1 = str(trade_no)
    str_2 = ' Page_' + str(page_num) + '.png'

    file_path = r'C:\Users\jizeyuan\Desktop\订单物流截图\\' + str_1

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    img_1 = ImageGrab.grab(bbox=(0, 0, 1080, 1920))
    img_1.save(file_path + '\\' + str_2)


def prtsc_3(trade_no):
    str_1 = str(trade_no) + '.png'

    file_path = r'C:\Users\jizeyuan\Desktop\订单物流截图\\' + str_1

    # if not os.path.exists(file_path):
    #     os.makedirs(file_path)

    img_1 = ImageGrab.grab(bbox=(0, 0, 1080, 1920))
    img_1.save(file_path)


def prtsc_4(trade_no, page_num):
    str_1 = str(trade_no) + '_' + str(page_num) + '.png'

    file_path = r'C:\Users\jizeyuan\Desktop\订单物流截图\\' + str_1

    # if not os.path.exists(file_path):
    #     os.makedirs(file_path)

    img_1 = ImageGrab.grab(bbox=(0, 0, 1080, 1920))
    img_1.save(file_path)
