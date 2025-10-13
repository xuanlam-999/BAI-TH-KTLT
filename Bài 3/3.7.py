from math import sqrt

print("Nhập các lệnh di chuyển của robot (ví dụ: UP 5, DOWN 3).")
print("Nhập dòng trống để kết thúc!\n")

# Khởi tạo tọa độ ban đầu
x = 0
y = 0

while True:
    data = input("Nhập lệnh: ")
    if not data:  # nếu người dùng nhập trống -> dừng
        break
    huong, buoc = data.split()
    buoc = int(buoc)

    # Xử lý từng hướng di chuyển
    if huong.upper() == "UP":
        y += buoc
    elif huong.upper() == "DOWN":
        y -= buoc
    elif huong.upper() == "LEFT":
        x -= buoc
    elif huong.upper() == "RIGHT":
        x += buoc
    else:
        print(" Hướng không hợp lệ! Hãy nhập UP/DOWN/LEFT/RIGHT.")

# Tính khoảng cách từ (0,0) đến (x,y)
khoang_cach = sqrt(x**2 + y**2)

print(f"\nTọa độ cuối cùng của robot: ({x}, {y})")
print(f"Khoảng cách đến vị trí ban đầu: {round(khoang_cach)}")
