# 2.两个集合的交并差集

setA = set(input("输入集合A(空格分隔) ").split())
setB = set(input("输入集合B(空格分隔) ").split())
print("集合的交集为", setA & setB)
print("集合的并集为", setA | setB)
print("setA - setB", setA - setB)
