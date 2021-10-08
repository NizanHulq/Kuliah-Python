inp1 = input().split()
inp2 = input().split()

print()
print()

inp3 = input().split()
inp4 = input().split()

a,b = int(inp1[0]),int(inp1[1])
c,d = int(inp2[0]),int(inp2[1])
e,f = int(inp3[0]),int(inp3[1])
g,h = int(inp4[0]),int(inp4[1])

w = a*e + b*g
x = a*f + b*h
y = c*e +d*g
z = c*f + d*h
print(w,x)
print(y,z)