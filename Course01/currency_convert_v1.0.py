"""
    作者：AAA
    功能：汇率计算小程序
    版本：1.0
    日期：01/08/2017
"""

# 汇率
USD_VS_RMB: float = 6.77

# 人民币的输入
rmb_str_value: str = input("请输入RMB:")
print(rmb_str_value)

# 字符串转换数字
rmb_value: int = eval(rmb_str_value)


# 汇率计算
usd_value: int = rmb_value / USD_VS_RMB

# 输出结果
print('美元金额：', usd_value)


