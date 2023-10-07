class Figure:
    def perimetr(self):
        return self.a + self.b

class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = self.check_value(a)
        self.b = self.check_value(b)
    
    @staticmethod
    def check_value(v):
        if v < 0:
            raise ValueError("Отрицательное значение")
        return v
    
    def perimetr(self):
        return 2 * (self.a + self.b)

r = Rectangle(1, 2)
print(r.perimetr())