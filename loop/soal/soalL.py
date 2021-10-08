x = float(input())
y = x - int(x)

if y < 0.4:
    print(int(x))

if y >= 0.4:
    print(int(x) + 1)