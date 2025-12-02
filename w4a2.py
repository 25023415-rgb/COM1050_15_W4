n = -1
while n <= 0:
    n = int(input("Nhập vào một số nguyên dương: "))

la_nguyen_to = True

if n < 2:
    la_nguyen_to = False
else:
    for i in range(2, n):
        if n % i == 0:
            la_nguyen_to = False
            break

if la_nguyen_to == True:
    print(n, "là số nguyên tố.")
else:
    print(n, "KHÔNG PHẢI là số nguyên tố.")

