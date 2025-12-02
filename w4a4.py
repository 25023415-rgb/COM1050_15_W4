while True:
    try:
        n = int(input("Nhập một số nguyên: "))
        break
    except ValueError:
        print("Vui lòng nhập một số nguyên")

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
