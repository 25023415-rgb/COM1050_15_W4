n = int(input())
socochuoidainhat = 1
dodaichuoi = 0
if n > 0:
    for i in range(1, n + 1):
        temp = i
        length = 1
        while temp != 1:
            if temp % 2 == 0:
                temp = temp // 2
            else:
                temp = 3 * temp + 1
            length += 1
        if length > dodaichuoi:
            dodaichuoi = length
            socochuoidainhat = i
    print(socochuoidainhat)
else:
    print("Nhap so nguyen duong")