
from search_module1 import Sequential_Search

# Nhập danh sách từ bàn phím
n = int(input("Nhập số phần tử của danh sách: "))
dlist = []

for i in range(n):
    val = int(input(f"Nhập phần tử thứ {i+1}: "))
    dlist.append(val)

item = int(input("Nhập phần tử cần tìm: "))

# Gọi hàm tìm kiếm
found, pos = Sequential_Search(dlist, item)

# Hiển thị kết quả
if found:
    print(f"Tìm thấy {item} tại vị trí {pos}")
else:
    print(f"Không tìm thấy {item} trong danh sách")
