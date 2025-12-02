# -*- coding: utf-8 -*-
while True:
    try:
        n = int(input("Nhập một số nguyên: "))
        break

if n < 0:
    n = -n

dem_so = 0
if n == 0:
    dem_so = 1
else:
    while n > 0:
        n = n // 10
        dem_so += 1

print("Số chữ số:", dem_so)