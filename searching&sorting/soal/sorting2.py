n = int(input())
list_a = input().split()
a = 0
for i in range(n-1):
    for j in range(n-1):
        if list_a[j] > list_a[j+1]:
            a += 1
            tmp = list_a[j]
            list_a[j] = list_a[j+1]
            list_a[j+1] = tmp
            
print(list_a)
print(a)