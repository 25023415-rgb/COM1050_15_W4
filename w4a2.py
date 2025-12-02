# 1. Nhập số nguyên dương (lặp lại nếu nhập sai)
n = -1
while n <= 0:
    n = int(input("Nhập vào một số nguyên dương: "))

# 2. Kiểm tra số nguyên tố
la_nguyen_to = True  # Ban đầu giả sử là đúng

if n < 2:
    la_nguyen_to = False # Số 0 và 1 không phải nguyên tố
else:
    # Chạy thử từ 2 đến n-1 (không cần tính căn bậc 2)
    for i in range(2, n):
        if n % i == 0:
            la_nguyen_to = False
            break # Tìm thấy ước số thì dừng ngay, không cần kiểm tra tiếp

# 3. In kết quả
if la_nguyen_to == True:
    print(n, "là số nguyên tố.")
else:
    print(n, "KHÔNG PHẢI là số nguyên tố.")