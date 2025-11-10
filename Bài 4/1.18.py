
n = int(input("Nhập số nguyên n: "))

# Tạo list chứa các số Fibonacci nhỏ hơn n
fibo = [0, 1]
while True:
    next_num = fibo[-1] + fibo[-2]
    if next_num >= n:
        break
    fibo.append(next_num)


print("Các số Fibonacci nhỏ hơn", n, "là:")
print(fibo)
