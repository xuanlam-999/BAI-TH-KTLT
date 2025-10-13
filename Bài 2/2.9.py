str = input("nhap string: ")# Nhập vào một chuỗi
dict = {}# Tạo một từ điển rỗng
for i in str:
    dict[i] = str.count(i)# Đếm số lần xuất hiện của ký tự đó và lưu vào dict
print(dict)
