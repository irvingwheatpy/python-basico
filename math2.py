print('The following is a series of math problems.')
print('Q: if (2^3)^4 = x, find the value of x')

a = 2
b = 3
c = 4

print('A: 2 * 2 * 2 =', a * a * a)

d = a * a * a

print('A: 8 * 8 * 8 * 8 =', d * d * d * d)

print('Q: A triangle has a base of 10 cm and a height of 8 cm. Find the area of this triangle.')

e = 10
f = 8
g = 1 / 2

print('Area is 1/2 * base * height')
print('A: 1/2 * 10 * 8 =', g * e * f, 'square cm')

print('Q: What comes next in the sequence: 2, 4, 8, 16?')

x = 1

while x < 5:
    a = a * 2
    print(a)
    x += 1

print('A: The next number in the sequence is', a)

print('Q: Which fraction is larger: 2/3 or 3/5')

o = 2 / 3
p = 3 / 5

if o > p:
    print('A: 2/3 is greater than 3/5')
else:
    print('A: 3/5 is greater than 2/3')

