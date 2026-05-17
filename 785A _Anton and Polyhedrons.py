n = int(input())
j=0
for i in range(n):
    s = input()
    if s == 'Tetrahedron':
        j = j + 4
    elif s == 'Cube':
        j = j + 6
    elif s == 'Octahedron':
        j = j+ 8
    elif s == 'Dodecahedron' :
        j = j + 12
    elif s == 'Icosahedron':
        j = j+20
print(j)
