n = int(input())
if 0 < n < 10**6:
    souocsochan = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 == 0:
            souocsochan += 1
    print(souocsochan)
else:
    print("Nhap so nguyen duong nho hon 10^6")