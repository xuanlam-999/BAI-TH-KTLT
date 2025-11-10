def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Tạo tuple P gồm các số nguyên tố nhỏ hơn 1_000_000
P = tuple(i for i in range(2, 1_000_000) if is_prime(i))

# In ra màn hình (in giới hạn vì tuple rất dài)
print("Số lượng số nguyên tố nhỏ hơn 1 triệu là:", len(P))
print("10 số đầu tiên:", P[:10])
print("10 số cuối cùng:", P[-10:])

