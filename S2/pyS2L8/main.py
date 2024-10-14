import matplotlib.pyplot as plt
import numpy as np
from scipy import special
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

"""Задание 1"""
# n_max = 7
# x = np.linspace(-1, 1)
# y = np.transpose(np.array([special.lpn(n_max, xi)[0] for xi in x]))
#
# for i in range(1, len(y)):
#     plt.plot(x, y[i], label=f"n{i}")
#
# plt.legend()
# plt.title("Полиномы Лисажу")
# plt.grid()
# plt.show()


"""Задание 2"""
# A = [3, 3, 5, 5]
# B = [2, 4, 4, 6]
#
# t = np.linspace(0, 2*np.pi, 1000)
# f = []
#
# for i in range(len(A)):
#     fig, ax = plt.subplots()
#     ax.plot(np.cos(A[i] * t), np.sin(B[i] * t))
#     ax.grid()
# plt.show()


"""Задание 3"""
# f = plt.figure()
#
# a = np.linspace(0, 1, 1000)
# t = np.linspace(-np.pi*10, np.pi*10, 1000)
# print(a)
#
# def anim(i):
#     f.clear()
#     x = np.sin(a[i] * t)
#     i += 1
#     y = np.sin(t)
#     plt.plot(x, y)
#     plt.grid()
#
#
# anim = FuncAnimation(f, anim, frames=2000, interval=10)
# plt.show()

"""Задание 4"""
#
# a = 2
# f = 5
#
# fig, ax = plt.subplots(3, 1)
#
# x1 = np.linspace(0, 8*np.pi, 500)
# y1 = a*np.sin(f * x1)
#
# x2 = np.linspace(0, 8*np.pi, 500)
# y2 = np.cos(x2)
#
# axa1 = plt.axes([0.3, 0.9, 0.1, 0.1])
# axa2 = plt.axes([0.8, 0.9, 0.1, 0.1])
# axf1 = plt.axes([0.1, 0.9, 0.1, 0.1])
# axf2 = plt.axes([0.6, 0.9, 0.1, 0.1])
#
# sliderAXA1 = Slider(axa1, "аплит.", valmin=0, valmax=5)
# sliderAXA2 = Slider(axa2, "аплит.", valmin=0, valmax=5)
# sliderAXF1 = Slider(axf1, "част.", valmin=0, valmax=5)
# sliderAXF2 = Slider(axf2, "част.", valmin=0, valmax=5)
#
#
# line1, = ax[0].plot(x1, y1)
# line2, = ax[1].plot(x2, y2)
# line3, = ax[2].plot(x1+x2, y1+y2)
#
# def update(val):
#     s11 = sliderAXF1.val
#     s12 = sliderAXA1.val
#     line1.set_ydata(s12*np.sin(s11 * x1))
#
#     s21 = sliderAXF2.val
#     s22 = sliderAXA2.val
#     line2.set_ydata(s22*np.sin(s21 * x2))
#
#     line3.set_ydata(s12*np.sin(s11 * x1) + s22*np.sin(s21 * x2))
#
#
# sliderAXF1.on_changed(update)
# sliderAXA1.on_changed(update)
# sliderAXF2.on_changed(update)
# sliderAXA2.on_changed(update)
#
# plt.show()

"""Задание 5"""
#
# def func(a, b):
#     return (a - b) ** 2
#
#
# fig, ax = plt.subplots(1, 2, subplot_kw={'projection': '3d'})
#
# x1 = np.random.normal(0, 100, 100)
# y1 = np.random.normal(0, 100, 100)
# z1 = []
# for i in range(len(x1)):
#     z1.append(func(x1[i], y1[i]))
#
# x2 = np.random.normal(0, 100, 100)
# y2 = np.random.normal(0, 100, 100)
# z2 = []
# for i in range(len(x2)):
#     z2.append(func(x2[i], y2[i]))
#
# ax[0].plot_trisurf(x1, y1, z1)
# ax[0].set_xlabel('x')
# ax[0].set_ylabel('y')
# ax[0].set_zlabel('z')
#
# ax[1].plot_trisurf(x2, y2, z2)
# ax[1].set_xlabel('x')
# ax[1].set_ylabel('y')
# ax[1].set_zlabel('z')
# ax[1].set_zscale('log')
#
# plt.show()
