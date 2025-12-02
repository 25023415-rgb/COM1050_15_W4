while True:
    try:
        n = int(input())
        if 0 < n < 100:
            break
        else:
            print("Vui lòng nhập số nguyên dương nhỏ hơn 100.")
    except ValueError:
        print("Nhập không hợp lệ. Vui lòng nhập số nguyên.")

giaithua = 1
for i in range(1, n + 1):
    giaithua = giaithua * i

print(giaithua)