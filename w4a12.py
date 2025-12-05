sotiengoc = float(input())
N = int(input())
if sotiengoc > 0 and N > 0:
    for i in range(N):
        sotiengoc = sotiengoc + sotiengoc * 0.7/100
    print(int(sotiengoc))
else:
    print("Nhap so duong")
