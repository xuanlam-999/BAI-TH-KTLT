
s = input("Nhập một câu: ")

# Khởi tạo biến đếm
dem_hoa = 0
dem_thuong = 0

# Duyệt qua từng ký tự trong chuỗi
for ch in s:
    if ch.isupper():      
        dem_hoa += 1
    elif ch.islower():    
        dem_thuong += 1

print("Số chữ hoa:", dem_hoa)
print("Số chữ thường:", dem_thuong)
