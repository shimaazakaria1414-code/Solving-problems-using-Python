n,h = map(int,input().split())
a = input().split()
j =0
k=0
for i in range(n):
    if int(a[i])<=h:
        j+=1
    else:
        k+=2
print(j+k)
