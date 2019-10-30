class Matrix:
    def __init__(self, elements):
        self.a11, self.a12, self.a21, self.a22 = elements
    
    @property
    def elements(self):
        return [self.a11, self.a12, self.a21, self.a22]
    
    def __add__(self, other):
        elements = [x + y for x, y in zip(self.elements, other.elements)]
        return Matrix(elements)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            a11 = self.a11 * other.a11 + self.a12 * other.a21
            a12 = self.a11 * other.a12 + self.a12 * other.a22
            a21 = self.a21 * other.a11 + self.a22 * other.a21
            a22 = self.a21 * other.a12 + self.a22 * other.a22
            elements = [a11, a12, a21, a22]
            return Matrix(elements)
        else:
            elements = [other * x for x in self.elements]
            return Matrix(elements)

    def __rmul__(self, other):
        elements = [other * x for x in self.elements]
        return Matrix(elements)
    
    def __str__(self):
        return f"{self.a11} {self.a12}\n{self.a21} {self.a22}"


m1 = Matrix([100, 2, 3, 4])
m2 = Matrix([1, 0, 0, 1])
print(m2 * m1)