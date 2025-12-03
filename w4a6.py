a, b = map(int, input().split())
if a > 0 and b > 0 and a <= b:
    tong = 0
    for i in range(a, b + 1):
        if i < 2:
            la_nguyen_to = False
        else:
            la_nguyen_to = True
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    la_nguyen_to = False
                    break
        
        if la_nguyen_to:
            tong += i
    print(tong)