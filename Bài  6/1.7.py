import math

class Circle:
    def __init__(self, radius):

        if radius < 0:
            raise ValueError("Bán kính không thể là số âm.")
        self.radius = radius

    def calculate_area(self):
        area = math.pi * (self.radius ** 2)
        return area

    def calculate_perimeter(self):
        """
        Tính chu vi của hình tròn (còn gọi là chu vi).
        Công thức: Chu vi = 2 * π * r

        Returns:
            float: Chu vi của hình tròn.
        """
        perimeter = 2 * math.pi * self.radius
        return perimeter

# sử dụng class

my_circle = Circle(5)

area = my_circle.calculate_area()
print(f"Bán kính hình tròn: {my_circle.radius}")
print(f"Diện tích hình tròn: {area:.4f}") # In ra 4 chữ số thập phân

perimeter = my_circle.calculate_perimeter()
print(f"Chu vi hình tròn: {perimeter:.4f}")
