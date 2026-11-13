# 1.6 幸运数字计算。用户输入姓名，输出该名字对应的幸运数字，不超过3位数字
import random
name = input("请输入名字：")
lucky = 1
random.seed(7)
for c in name:
    lucky += ord(c) * random.randint(1,77)
print("幸运数字是：{}".format(lucky%777))