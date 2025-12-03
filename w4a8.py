n = int(input())
if n >=0:
    step = 0
    while str(n) != str(n)[::-1]:
        n += int(str(n)[::-1])
        step += 1
    print(f"{step}")
    print(f"{n}")
else:
    print("Nhap so nguyen duong")
