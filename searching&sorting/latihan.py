# latihan 1

list_a = [7, 2, 10, 9, 1]
length = len(list_a)
for i in range(length-1):
    for j in range(length-1):
        if list_a[j] < list_a[j+1]:
            tmp = list_a[j]
            list_a[j] = list_a[j+1]
            list_a[j+1] = tmp
print(list_a)
x = int(input())
b = list_a[0:x]
print(b)
    

# latihan 2
"""list_a = [7, 2, 10, 9, 1]
length = len(list_a)
for i in range(length-1):
    for j in range(length-1):
        if list_a[j] < list_a[j+1]:
            tmp = list_a[j]
            list_a[j] = list_a[j+1]
            list_a[j+1] = tmp

inp = input().split()
x = int(inp[0])
y = int(inp[1])

b = list_a[x-1:y]
print(b)"""