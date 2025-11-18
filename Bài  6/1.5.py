class StringReverse:
    def __init__(self, input_str):
        self.input_str = input_str  

    def reverse_words(self):
        # Tách chuỗi thành danh sách các từ
        words = self.input_str.split()
        # Đảo ngược danh sách
        reversed_words = words[::-1]
        # Ghép lại thành chuỗi
        return ' '.join(reversed_words)

chuoi = input("Nhập chuỗi: ")
str_obj = StringReverse(chuoi)
print("Chuỗi sau khi đảo là:", str_obj.reverse_words())
