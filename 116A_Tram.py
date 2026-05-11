y= int(input())
w = []
m=0
for i in range(y):
    a,b = map(int,input().split())
    m = m-a+b
    w.append(m)
print(max(w))   
