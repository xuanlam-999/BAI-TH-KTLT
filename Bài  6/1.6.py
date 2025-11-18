class StringManipulator:
    """
    Một class đơn giản để lấy một chuỗi từ người dùng và in chuỗi đó bằng chữ in hoa.
    """
    
    def __init__(self):
        self.s = ""

    def get_String(self):
        self.s = input("Nhập chuỗi của bạn: ")

    def print_String(self):
        print(self.s.upper())
        
# Tạo một đối tượng (instance) của class
manipulator = StringManipulator()

manipulator.get_String()

manipulator.print_String()
