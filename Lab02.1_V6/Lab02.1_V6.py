# Lab_02.cpp
# < Іваньо Іван >
# Лабораторна робота № 2.
# Лінійні програми.
# Варіант 0.6

import math # імпорт бібліотеки math

a = float(input("a = ")) # ввід даних

z1 = math.cos(a) + math.cos(2 * a) + math.cos(6 * a) + math.cos(7 * a) # розрахунок для z1

z2 = 4 * math.cos(a / 2) * math.cos(5 / 2 * a) * math.cos(4 * a) # розрахунок для z2

print("z1 = ", round(z1, 5)) # вивід z1
print("z2 = ", round(z2, 5)) # вивід z2
print("z1 + z2 = ", z1 + z2)
print("Hello, World!")
