# 列表(List)详解

## 列表的创建
```python
ls = [425, "BIT", [10, "CS"], 425]           # 直接创建
list("中国")            # ['中', '国']，字符串转列表
list((1,2,3))           # [1,2,3]，元组转列表
```

## 列表的索引和切片
```python
ls = [1, 2.5, 'test', 3+4j, True, [3,1.63], 5.3]
ls[2]           # 'test'（单个元素）
ls[2:3]         # ['test']（切片返回列表）
ls[5][1]        # 1.63（访问嵌套列表）
```

## 列表的修改（可变性）
```python
# 单个元素修改
ls[1] = 'python'

# 切片修改（可增减元素数量）
ls[1:4] = ['python', 20]    # 替换2-4个元素为2个元素
ls[0:2] = []                 # 删除前两个元素
```

## 列表的遍历
```python
for e in ls:
    print(e, end=" ")
```

## 列表的应用示例
```python
# 气温统计
daily_temperatures = [22.5, 24.0, 19.5, 21.0, 23.5]
avg_temp = sum(daily_temperatures) / len(daily_temperatures)
max_temp = max(daily_temperatures)
day_of_max = daily_temperatures.index(max_temp) + 1
```
