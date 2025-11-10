numbers = input("Nhập các số, cách nhau bằng dấu cách: ")

# Chuyển chuỗi nhập vào thành danh sách số nguyên
numbers = [int(x) for x in numbers.split()]

# Lọc các số lẻ
odd_numbers = [x for x in numbers if x % 2 != 0]

print("Các số lẻ trong danh sách là:", odd_numbers)
