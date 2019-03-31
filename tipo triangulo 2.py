a = float(input())
b = float(input())
c = float(input())

if a == b and b == c:
    print('equilatero')
elif a != b and b != c and a != c:
    print('escaleno')
else:
    print('isosceles')
