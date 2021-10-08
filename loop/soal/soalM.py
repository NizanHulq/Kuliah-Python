a, b, c, d = [int(a) for a in input(). split()]
x = a/b
y = c/d
if x == y:
    print("=")

if x > y:
    print(">")

if x < y:
    print("<")