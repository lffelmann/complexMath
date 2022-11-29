import math


class Complex:
    real = None
    imaginary = None
    modulus = None
    argument = None

    def __init__(self, value):
        """class of complex Numbers to calculate with.

        :param value: Complex number (str: can be given in cartesian: "x+yj" or polar: "re^phi")
        :type value: str | complex | float | int | Complex
        """
        # try to convert value to complex
        try:
            value = complex(value)
        except:
            pass
        # element without imaginary
        if isinstance(value, float):
            self.real = value
            self.imaginary = 0.
            if value < 0:
                self.modulus = value * -1
                self.argument = math.pi
            else:
                self.modulus = value
                self.argument = 0.
        # cartesian
        elif isinstance(value, complex):
            self.real = value.real
            self.imaginary = value.imag
            self.modulus = math.sqrt(abs(self.real) ** 2 + abs(self.imaginary) ** 2)
            if self.real == 0:
                if self.imaginary == 0:
                    self.argument = 0
                elif self.imaginary > 0:
                    self.argument = math.pi / 2
                else:
                    self.argument = 3 * math.pi / 2
            else:
                self.argument = math.atan(self.imaginary / self.real)
                if self.real < 0:
                    self.argument += math.pi
                if self.argument < 0:
                    self.argument += 2 * math.pi
        # polar
        elif isinstance(value, str) and "e^" in value:
            # extract modulus and argument
            modulusStr = value[0:value.find("e^")]
            if len(modulusStr) == 0:
                self.modulus = 0.
            else:
                self.modulus = float(modulusStr)
            argumentStr = value[value.find("e^") + 2:]
            if len(argumentStr) == 0:
                self.argument = 0
            else:
                self.argument = float(argumentStr)
            # revert if modulus is negative
            if self.modulus < 0:
                self.modulus = self.modulus * -1
                self.argument += math.pi
            # get argument in [0;2Pi[
            while self.argument < 0:
                self.argument += 2 * math.pi
            self.argument %= 2 * math.pi
            # convert to cartesian
            self.real = self.modulus * math.cos(self.argument)
            self.imaginary = self.modulus * math.sin(self.argument)
        # Complex
        elif isinstance(value, Complex):
            self.real = value.real
            self.imaginary = value.imaginary
            self.argument = value.argument
            self.modulus = value.modulus
        else:
            raise Exception("Value isn't a valid.")

    def __complex__(self):
        return complex(self.real, self.imaginary)

    def __str__(self):
        if self.imaginary < 0:
            spacer = ""
        else:
            spacer = "+"
        return str(self.real) + spacer + str(self.imaginary) + "j"

    def __add__(self, other):
        other = Complex(other)
        real = self.real + other.real
        imag = self.imaginary + other.imaginary
        return Complex(complex(real, imag))

    def __sub__(self, other):
        other = Complex(other)
        real = self.real - other.real
        imag = self.imaginary - other.imaginary
        return Complex(complex(real, imag))

    def __mul__(self, other):
        other = Complex(other)
        real = self.real * other.real - self.imaginary * other.imaginary
        imag = self.real * other.imaginary + self.imaginary * other.real
        return Complex(complex(real, imag))

    def __truediv__(self, other):
        other = Complex(other)
        real = (self.real * other.real + self.imaginary * other.imaginary) / (other.real ** 2 + other.imaginary ** 2)
        imag = (self.imaginary * other.real - self.real * other.imaginary) / (other.real ** 2 + other.imaginary ** 2)
        return Complex(complex(real, imag))

    def __pow__(self, power, modulo=None):
        modulus = self.modulus ** power
        argument = self.argument * power
        while argument < 0:
            argument += 2 * math.pi
        argument %= 2 * math.pi
        return Complex(str(modulus) + "e^" + str(argument))

    def root(self, power=2):
        """Get all roots af a complex number.

        :param power: n of the root (standard 2 for square root)
        :type power: int
        :return: all roots
        :rtype: list[Complex]
        """
        temp = []
        modulus = self.modulus ** (1 / power)
        for i in range(0, power):
            argument = (self.argument + i * 2 * math.pi) / power
            argument %= 2 * math.pi
            temp.append(Complex(str(modulus) + "e^" + str(argument)))
        return temp

    def __abs__(self):
        return self.modulus

    def __eq__(self, other):
        other = Complex(other)
        if self.real == other.real and self.imaginary == other.imaginary:
            return True
        return False

    def __ne__(self, other):
        other = Complex(other)
        if self.real != other.real or self.imaginary != other.imaginary:
            return True
        return False

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        other = Complex(other)
        real = other.real - self.real
        imag = other.imaginary - self.imaginary
        return Complex(complex(real, imag))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __rtruediv__(self, other):
        other = Complex(other)
        real = (other.real * self.real + other.imaginary * self.imaginary) / (self.real ** 2 + self.imaginary ** 2)
        imag = (other.imaginary * self.real - other.real * self.imaginary) / (self.real ** 2 + self.imaginary ** 2)
        return Complex(complex(real, imag))

    def __repr__(self):
        if self.imaginary < 0:
            spacer = ""
        else:
            spacer = "+"
        return str(self.real) + spacer + str(self.imaginary) + "j"
