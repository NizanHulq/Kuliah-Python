def f(n):
    if n == 0:
        return 10
    elif n > 0 and n%2 == 0 :
        return 4 * f(n//2)
    else:
        return f(n-1) + 1

msk = int(input())

print(f(msk))