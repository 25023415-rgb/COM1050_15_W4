m, n = map(int, input().split())
if m > 0 and n > 0:
    if m > n:
        sonho = n
    else:
        sonho = m
    for i in range(sonho, 0, -1):
        if m % i == 0 and n % i == 0:
            print(i)
            break
else:
    print("Nhập số nguyên dương")