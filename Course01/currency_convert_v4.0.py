"""
    作者：AAA
    功能：汇率计算小程序
    版本：3.0
    日期：01/08/2017
    新增功能：字符串处理
    新增功能：程序一直运行，直到用户选择退出
    新增功能：汇率兑换功能封装到函数
"""


def convert_currency(in_value, rate):
    out_value = in_value * rate
    return out_value


# 汇率
USD_VS_RMB = 6.77


# 带单位货币输入
currency_str_value = input("请输入带单位的货币金额(退出请输入Q):")

while currency_str_value[-1].upper() != 'Q':
    # 获取货币单位
    unit_str = currency_str_value[-3:].upper()
    # print(unit_str)

    if unit_str == 'CNY':
        # 输入的是人民币
        exchange_rate = 1 / USD_VS_RMB
    elif unit_str == 'USD':
        # 输入的是美元
        exchange_rate = USD_VS_RMB
    else:
        # 其他情况
        exchange_rate = -1
        # 其他情况

    if exchange_rate != -1:
        in_money = eval(currency_str_value[0:-3])
        out_money = convert_currency(in_money, exchange_rate)
        print('兑换后的金额：', out_money)
    else:
        print('不支持该货币')

    print('***********************')  # 空行
    currency_str_value = input("请输入带单位的货币金额(退出请输入Q):")

print('程序已退出')
