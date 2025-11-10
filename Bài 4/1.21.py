binary_input = input("Nhập các số nhị phân 4 chữ số, cách nhau bằng dấu phẩy: ")
binary_list = binary_input.split(',')

# Lọc các số chia hết cho 5
result = []
for b in binary_list:
    # Chuyển từ nhị phân sang thập phân
    num = int(b, 2)
    if num % 5 == 0:
        result.append(b)
print("Các số nhị phân chia hết cho 5 là:", ','.join(result))
