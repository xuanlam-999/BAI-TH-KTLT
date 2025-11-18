class RomanConverter:
    # Bảng giá trị các ký tự La Mã
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # Hàm khởi tạo
    def __init__(self, roman):
        self.roman = roman.upper()  # lưu chuỗi La Mã (chuyển thành chữ hoa)

    # Phương thức chuyển đổi sang số nguyên
    def to_integer(self):
        total = 0
        prev_value = 0

        # Duyệt ngược chuỗi La Mã (từ phải sang trái)
        for char in reversed(self.roman):
            value = self.roman_values[char]

            # Nếu giá trị nhỏ hơn giá trị trước đó → phải trừ
            if value < prev_value:
                total -= value
            else:
                total += value

            prev_value = value

        return total


# --- Chương trình chính ---
so_roman = input("Nhập số La Mã: ")
converter = RomanConverter(so_roman)
so_nguyen = converter.to_integer()
print("Giá trị số nguyên là:", so_nguyen)
