a, b = 1, 2
#tao bien de luu tong cac so thoa man dieu kien
total = 0
print(a, end=" ")

while (a <= 4000000 - 1):
    if a % 2 == 0:
#neu la so chan thi cong vao tong
        total += a
    a, b = b, a + b
    print(a, end=" ")

print("\n tong cac so chan ", total)
