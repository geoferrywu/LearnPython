"""
    作者：AAA
    功能：汇率计算小程序
    版本：3.0
    日期：01/08/2017
    新增功能：字符串处理
    新增功能：程序一直运行，直到用户选择退出
"""

# 汇率
USD_VS_RMB: float = 6.77

# 带单位货币输入
currency_str_value: str = input("请输入带单位的货币金额(退出请输入Q):")
i = 0
while currency_str_value[-1].upper() != 'Q':
    i = i + 1
    # print('第', i, '次运行')

    # 获取货币单位
    unit_str = currency_str_value[-3:].upper()
    # print(unit_str)

    if unit_str == 'CNY':
        # 输入的是人民币
        rmb_value = eval(currency_str_value[0:-3])
        usd_value = rmb_value / USD_VS_RMB
        print('美元(USD)金额是：', usd_value)
    elif unit_str == 'USD':
        # 输入的是美元
        usd_value = eval(currency_str_value[0:-3])
        rmb_value = usd_value * USD_VS_RMB
        print('人民币(RMB)金额是：', rmb_value)
    else:
        # 其他情况
        print('不支持该货币单位')

    print('***********************')  # 空行
    currency_str_value: str = input("请输入带单位的货币金额(退出请输入Q):")


print('程序已退出')
