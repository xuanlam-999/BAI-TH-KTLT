s = input("Nhập một câu: ")

# Khởi tạo biến đếm
dem_chu = 0
dem_so = 0

for ch in s:
    if ch.isalpha():      #Nếu là chữ cái (a-z, A-Z)
        dem_chu += 1
    elif ch.isdigit():    #Nếu là chữ số (0-9)
        dem_so += 1

print("Số chữ cái là:", dem_chu)
print("Số chữ số là:", dem_so)
