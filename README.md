# complexNumbers

Use complex numbers in python.

## 1 Initial Complex

```
z = Complex(value)
```

value can be 5 different datatypes:

- `int`
- `float`
- `complex`
- `str`
- `Complex`

### 1.1 `int, float`

They are used when a real number should be become a complex number. (no imaginary part)

### 1.2 `complex`

Standard complex numbers also can be initialed. (e.g.: `1+1j`)

### 1.3 `str`

With a string there can be entered complex numbers in the cartesian and polar form.

#### 1.3.1 cartesian form

should be entered like this: `"x+yj"`

#### 1.3.2 polar form

Modulus and argument are separated by `e^`. (e.g.: `1e^1`)

### 1.4 `Complex`

Value can also be the same type as the own class.

## 2 Variables

The class has following `__self__` variables.

- `real`: real part of the cartesian form
- `imaginary`: imaginary part of the cartesian form
- `modulus`: modulus of the polar form
- `argument`: argument of the polar form in the range [0; 2Pi[

## 3 Methods

The class can be used with the following methods:

- `__add__ , __radd__ , __iadd__` equals `+ , +=`
- `__sub__ , __rsub__ , __isub__` equals `- , -=`
- `__mul__ , __rmul__ , __imul__` equals `* , *=`
- `__truediv__ , __rtruediv__ , __itruediv__` equals `/ , /=`
- `__pow__` equals `**` ***ATTENTION:*** only real numbers can be used as `power` and when used to get a root only one
  solution returns.
- `__eq__` equals `==`
- `__ne__` equals `!=`
- `__abs__` equals `abs()` returns the modulus
- `__str__` equals `str()` returns the number in cartesian form (e.g.: `"1+1j"`)
- `root(n)` returns a list with all possible roots of the complex number. `n` is the power of the root (e.g.: n = 2 ...
  square root)

## 4 Example

```
>>> a = Complex("1+1j")
>>> b = Complex("1e^1")
>>> print(a.modulus)
1.4142135623730951
>>> print(a.argument)
0.7853981633974483
>>> print(b.real)
0.5403023058681398
>>> print(b.imaginary)
0.8414709848078965
>>> print(a+b)
1.5403023058681398+1.8414709848078965j
>>> print(a-b)
0.45969769413186023+0.1585290151921035j
>>> print(a*b)
-0.30116867893975674+1.3817732906760363j
>>> print(a/b)
1.3817732906760363-0.30116867893975674j
>>> print(a**2)
1.2246467991473535e-16+2.0000000000000004j
>>> print(b**0.5)
0.8775825618903728+0.479425538604203j
>>> print(b.root())
[0.8775825618903728+0.479425538604203j, -0.8775825618903728-0.4794255386042029j]
>>> print(abs(b)
1.0
>>> print(a == a)
True
>>> print(a != b)
True
```