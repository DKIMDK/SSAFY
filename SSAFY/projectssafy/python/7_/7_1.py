

# 아래 클래스를 수정하시오.
class Shape:
    #7_1
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    #7_5
    def __str__(self):
        return (f'Shape: width={self.width}, height={self.height}')
    
    #7_2
    def calculate_area(self):
        return self.width * self.height

    #7_3
    def calculate_perimeter(self):
        return 2*self.width + 2*self.height
    
    #7_4
    def print_info(self):
        print(f'Width: {self.width}')
        print(f'Height: {self.height}')
        print(f'Area: {self.calculate_area()}')
        print(f'Perimeter: {self.calculate_perimeter()}')

shape1 = Shape(5, 3)
# print(shape1.width, shape1.height)
#area1 = shape1.calculate_area()
#perimeter1 = shape1.calculate_perimeter()
print(shape1)

