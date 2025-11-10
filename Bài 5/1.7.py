import numpy as np

# Tạo kiểu dữ liệu có cấu trúc
dt = np.dtype([
    ('ten', 'U20'),       # Chuỗi Unicode dài tối đa 20 ký tự
    ('chieucao', 'f4'),   # Float 4 byte
    ('lop', 'U10')        # Chuỗi Unicode dài tối đa 10 ký tự
])

# Tạo mảng dữ liệu
sinhvien = np.array([
    ('Anh', 1.72, '12A1'),
    ('Lâm', 1.65, '12A2'),
    ('My', 1.58, '12A1'),
    ('Duy', 1.80, '12A3'),
    ('Thảo', 1.60, '12A2')
], dtype=dt)

print("==> Dữ liệu ban đầu:")
print(sinhvien)

# Sắp xếp theo chiều cao (tăng dần)
sapxep = np.sort(sinhvien, order='chieucao')

print("\n==> Dữ liệu sau khi sắp xếp theo chiều cao:")
print(sapxep)
'''np.dtype([...]) → định nghĩa kiểu dữ liệu phức hợp cho từng cột.

('ten', 'U20') → kiểu chuỗi Unicode dài tối đa 20 ký tự.

('chieucao', 'f4') → kiểu số thực 32-bit.

np.sort(..., order='chieucao') → sắp xếp mảng theo cột chieucao.'''
