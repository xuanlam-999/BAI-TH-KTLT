# main.py
from search_module import binary_search

# Nhập danh sách từ bàn phím
n = int(input("Nhập số phần tử của danh sách: "))
lst = []

for i in range(n):
    val = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(val)

# Sắp xếp danh sách trước khi tìm kiếm (vì Binary Search cần dữ liệu tăng dần)
lst.sort()
print("Danh sách sau khi sắp xếp:", lst)

# Nhập phần tử cần tìm
value = int(input("Nhập phần tử cần tìm: "))

# Gọi hàm tìm kiếm
found, pos = binary_search(lst, value)

# Hiển thị kết quả
if found:
    print(f"Tìm thấy {value} tại vị trí {pos}")
else:
    print(f"Không tìm thấy {value} trong danh sách")
