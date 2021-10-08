length = int(input())
list_a = input().split()

for i in range(length-1):
    for j in range(length-1):
        if list_a[j] > list_a[j+1]:
            tmp = list_a[j]
            list_a[j] = list_a[j+1]
            list_a[j+1] = tmp
index = 0           
for i in range(length-1):
    if int(list_a[i]) == 165 :
        index = i+1
        break
print(index)
