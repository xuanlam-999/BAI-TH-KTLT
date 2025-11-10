ho_va_ten = input('Nhập họ và tên: ')

#rsplit() giới hạn 1 lần chia (từ phải sang)
# Kết quả là một list chỉ có 2 phần tử: [Họ và Tên đệm, Tên riêng]
chu_cai = ten_day_du.rsplit(' ', 1)

ho_va_ten_dem = chu_cai[0]


ten = chua_cai[1]

print("Họ và Tên đệm: ",ho_va_ten_dem)
print("Tên riêng: ",ten)


