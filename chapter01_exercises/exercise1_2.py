# 整数序列求和
n = input("请输入整数N:")
sum = 0
for i in range(int(n)):
    sum += i+1  # 注意这里是 i+1，因为range从0开始
print("1到N之和:", sum)