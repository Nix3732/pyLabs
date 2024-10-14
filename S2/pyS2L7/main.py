import numpy as np
import scipy
import time

"""Задание 1"""
# data = np.loadtxt("input.txt", delimiter=',', dtype=np.int_)
# print(data.sum())
# print(data.max())
# print(data.min())

"""Задание 2"""
# x = np.array([])
# while True:
#     i = input()
#     try:
#         int(i)
#     except:
#         if i == '':
#             break
#         print("it`s not a number")
#         continue
#     x = np.append(x, int(i))
#
# index = np.array([])
# for i in range(1, len(x)):
#     if x[i] != x[i-1]:
#         index = np.append(index, i-1)
#         if i == len(x)-1:
#             index = np.append(index, i)
#     else:
#         if all(x[j] == x[j+1] for j in range(i-1, len(x)-i)):
#             index = np.append(index, len(x)-i+1)
#             break
#
#
# y = np.array([])
# for i in index:
#     i = int(i)
#     y = np.append(y, x[i])
# index = np.insert(index, 0, -1)
# index = np.diff(index)
#
# print(y)
# print(index)

"""Задание 3"""
# n = np.random.normal(size=(10, 4))
# print(n.max())
# print(n.min())
# print(n.mean())
# print(n.std())
# n5 = n[5:]
# print(n5)

"""Задание 4"""
# x = np.array([])
# while True:
#     i = input()
#     try:
#         int(i)
#     except:
#         if i == '':
#             break
#         print("it`s not a number")
#         continue
#     x = np.append(x, int(i))
# zero = x == 0
# m = x[1:][zero[:-1]]
# print(int(m.max()))

"""Задание 5"""
# X = np.array([[1, 3], [5, 7]])
# C = np.array([[1, 1], [1, 3]])
# M = np.array([0, 0])
#
# t1 = time.perf_counter()
# logpdf = -0.5 * (np.log(2 * np.pi) + np.log(np.linalg.det(C)) +
#                  np.einsum('ij,ij->i', X - M, np.dot(np.linalg.inv(C), X - M)))
# t1f = time.perf_counter()
# print(logpdf)
# print(t1f-t1, "\n")
#
# t2 = time.perf_counter()
# g = scipy.stats.multivariate_normal(M, C).logpdf(X)
# t2f = time.perf_counter()
#
# print(g)
# print(t2f-t2, "\n")
#
# print("Разница значений и времени")
# print(logpdf-g)
# print(t2f-t2-(t1f-t1))

"""Задание 6"""

# a = np.arange(16).reshape(4, 4)
#
# a[0], a[2] = a[2], a[0].copy()
#
# print(a)

"""Задание 7"""

# url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# iris = np.loadtxt(url, delimiter=',', dtype='object')
#
# data = iris[:, 4]
#
# print(*np.unique(data))
# print(len(np.unique(data)))

"""Задание 8"""
# d = [0, 1, 2, 0, 0, 4, 0, 6, 9]
#
# print(*np.nonzero(d))