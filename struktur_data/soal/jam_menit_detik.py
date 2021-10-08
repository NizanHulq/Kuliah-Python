inp = int(input())

j = inp//3600
m = inp%3600//60
d = inp%3600%60

print(j)
print(m)
print(d)
