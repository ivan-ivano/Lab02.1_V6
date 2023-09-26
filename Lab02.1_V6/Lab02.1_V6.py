# Lab_02.cpp
# < ������ ���� >
# ����������� ������ � 2.
# ˳��� ��������.
# ������ 0.6

import math # ������ �������� math

a = float(input("a = ")) # ��� �����

z1 = math.cos(a) + math.cos(2 * a) + math.cos(6 * a) + math.cos(7 * a) # ���������� ��� z1

z2 = 4 * math.cos(a / 2) * math.cos(5 / 2 * a) * math.cos(4 * a) # ���������� ��� z2

print("z1 = ", round(z1, 5)) # ���� z1
print("z2 = ", round(z2, 5)) # ���� z2

