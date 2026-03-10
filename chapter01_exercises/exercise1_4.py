# 阶乘序列求和 1! + 2! + 3! + ... + 10!
sum = 0
tmp = 1
for i in range(1,11):
    tmp *= i      # 计算 i!
    sum += tmp    # 累加
print("运算结果是:{}".format(sum))