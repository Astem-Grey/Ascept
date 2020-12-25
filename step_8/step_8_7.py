
class ComlexChar:

    def __init__(self, a, b, i):
        self. a = a
        self.b = b
        self.i = i

    def __add__(self, other):
        result = (self.a + other.a) + (self.b + other.b) * self.i
        return result

    def __mul__(self, other):
        result = self.a * other.a + self.b * other.a * self.i + self.a * other.b * self.i + self.a * other.b * self.i + self.b * other.b * self.i * self.i
        return result

abc = ComlexChar(2, 20, 5)
abc2 = ComlexChar(5, 26, 5)
print(abc + abc2)
print(abc * abc2)