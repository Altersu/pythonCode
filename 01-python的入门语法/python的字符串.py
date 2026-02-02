# name = "alter"
# salary = "15000"
# print(name +" 2026翻身！ 工资" + salary)
#
# message = "2026年顺顺利利 %s" %name
# print(message)
#
# class_num =66
# avg_salary = 16781
# message = "第%s位员工，工资是%s" %(class_num,avg_salary)
# print(message)

# name = "alter"
# year = 26
# high = 160.00
# message = "姓名%s，年龄%d,身高%.3f" %(name,year,high)
# print(message)
# num1 = 11
# num2 = 11.234
# print("数字11宽度限制5，结果是：%5d"%num1)
# print("数字11宽度限制1，结果是：%1d"%num1)
# print("数字11.234宽度限制7，小数精度2，结果是：%7.2f"%num2)
# print("数字11.234宽度无限制，小数精度2，结果是：%.2f"%num2)
#
# name = "aaaa"
# age = 26
# weight = 45.6
# print(f"姓名{name},年龄{age},体重{weight}")

# print(f"1*8的结果是{1*8}")

name = "未来科技"
stock_price = 19.99
stock_code = "006688"
stock_price_daily_growth_factor = 1.2
growth_days = 7
print(f"公司：{name},股票代码:{stock_code},"
      f"当前股价：{stock_price},"
      f"每日增长系数是:{stock_price_daily_growth_factor},"
      f"进过{growth_days}天的增长后,"
      "股价达到了：%2.2f"%(stock_price*stock_price_daily_growth_factor**7)

      )