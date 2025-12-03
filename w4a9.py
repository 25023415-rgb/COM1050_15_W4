n = int(input("Nhập số nguyên dương n: "))
if n > 0:
    danh_sach = []
    i = 0
    while i * i <= n:
        so_chinh_phuong = i * i
        chuoi_so = str(so_chinh_phuong)
        if len(chuoi_so) == len(set(chuoi_so)):
            danh_sach.append(str(so_chinh_phuong))
            
        i += 1 

    if len(danh_sach) == 0:
        print("(no number)")
    else:
        print(" ".join(danh_sach))
else:
    print("Vui lòng nhập số nguyên dương.")
