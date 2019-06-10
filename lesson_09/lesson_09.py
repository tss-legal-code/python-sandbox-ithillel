from math import pi
class Figure(object):
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        raise NotImplementedError("perimeter not implemented in figure")

    def area(self):
        raise NotImplementedError("perimeter not implemented in figure")

# f=Figure([])
# f.area()
# f.perimeter()

class Triangle(Figure):
    def __init__(self, sides):
        if len(sides) != 3:
            raise Exception("Triangle must have 3 sides")
        super().__init__(sides)
        """ две стороны должны быть болеше третьей стороны """

    def perimeter(self):
        p = sum(self.sides)
        return p

    def area(self):
        hp = sum(self.sides) / 2
        ar = hp
        for i in self.sides:
            ar *= (hp - i)
        ar = ar ** 0.5
        return ar


t = Triangle([3, 4, 5])
print(t.perimeter())
print(t.area())


class Rectangle(Figure):

    def __init__(self, sides):
        if len(sides) != 2:
            raise Exception("Rectangle takes 2 opposite sides")
        super().__init__(sides)

    def perimeter(self):
        p = sum(self.sides) * 3
        return p

    def area(self):
        ar = self.sides[0] * self.sides[1]
        return ar


r = Rectangle([2, 5])
print(r.perimeter())
print(r.area())

class Circle(Figure):
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            print("Circle: radius must be numeric")
            raise Exception()
        self.r = radius

    def perimeter(self):
        p = 2 * pi * self.r
        return p

    def area(self):
        ar = pi * self.r ** 2
        return ar

    def __str__(self):
        return f"Circle: radius = {self.r}"

c = Circle(5)
print(c)
print(c.perimeter())
print(c.area())