import numpy as np
""" Numpy基本函数的使用：创建不同维度的数组
、利用索引访问数组元素、数组切片、整数索引、
布尔索引、数组的基本运算函数、数学函数、创建
矩阵、矩阵运算、排序函数、条件筛选函数、线性
代数相关函数 """

# 创建不同维度的的数组
a = np.arange(1, 17)
a = a.reshape(-1, 4)
b = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[10, 14, 5, 3], [7, 8, 9, 6]]])
c = np.empty((4, 3, 4), dtype=np.int8)
print(a.shape)
print(b)
print(c.shape)

# 利用索引访问
print(b[0, 1, 2])

# 数组切片
print(b[0, 0, :])

# 整数索引和布尔索引
print(a[[1, 2, 3], [1, 2, 3]])
print(a[a > 5])

# 数组基本运算
print(a+2)
print(a*2)
print(a*a)
d = np.array([[2, 2, 2, 2]])
print(a*d)

# 数学函数
print(a.sum())
print(a.cumprod())

# 创建矩阵
matA = np.matrix(a)
print(matA)
print(type(matA))
x = np.zeros((3, 3), dtype=np.int8)
print(x)
eye = np.mat(np.eye(3, 3, dtype=int))
print(eye)

# 矩阵运算
print(matA[:3, :3]*eye)
print(np.dot(matA[:3, :3], eye))
print(matA.T)


# 线性代数相关函数

print(np.linalg.pinv(matA))
