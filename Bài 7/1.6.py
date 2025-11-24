def lay_n_dong_cuoi_cung(fname, n):
    with open(fname, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    return lines[-n:]

danh_sach_dong = lay_n_dong_cuoi_cung('D:/Kì 3 (năm 2)/Thực hành KTLT/hfhd.py', 5)
for line in danh_sach_dong:
    print(line, end='')
