import math


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real_ = real
        self.imaginary_ = imaginary

    @property
    def real(self):
        return self.real_

    @property
    def imaginary(self):
        return self.imaginary_

    def __eq__(self, other):
        if isinstance(other, ComplexNumber):
            if self.real == other.real:
                if self.imaginary == other.imaginary:
                    return True
            else:
                return False

    def __radd__(self, other):
        return ComplexNumber(other + self.real, self.imaginary)

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
        else:
            return ComplexNumber(self.real + other, self.imaginary)

    def __rmul__(self, other):
        return ComplexNumber(self.real * other, self.imaginary * other)

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary,
                                 self.imaginary * other.real + self.real * other.imaginary)
        else:
            return ComplexNumber(self.real * other, self.imaginary * other)

    def __rsub__(self, other):
        return ComplexNumber(other - self.real, -self.imaginary)

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)
        else:
            return ComplexNumber(self.real - other, self.imaginary)

    def __rtruediv__(self, other):
        return ComplexNumber((self.real * other) / (self.real ** 2 + self.imaginary ** 2),
                             -((self.imaginary * other) / (self.real ** 2 + self.imaginary ** 2)))

    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber((self.real * other.real + self.imaginary * other.imaginary) /
                                 (other.real**2 + other.imaginary**2),
                                 (self.imaginary * other.real - self.real * other.imaginary) /
                                 (other.real**2 + other.imaginary**2))
        else:
            return ComplexNumber(self.real / other,self.imaginary / other)

    def __abs__(self):
        return math.sqrt(self.real**2 + self.imaginary**2)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        return ComplexNumber(math.e ** self.real * (math.cos(self.imaginary) + math.sin(self.imaginary)),0)

