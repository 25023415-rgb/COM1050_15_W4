a, b = map(int, input().split())
if a > 0 and b > 0:
    tongcacuoccuaa = 0
    tongcacuoccuab = 0
    for i in range(1, b + 1):
        if a % i == 0:
            tongcacuoccuaa += i
    for j in range(1, a + 1):
        if b % j == 0:
            tongcacuoccuab += j
    if tongcacuoccuaa == tongcacuoccuab:
        print("true")
    else:
        print("false")
else:
    print("Nhap so nguyen duong")