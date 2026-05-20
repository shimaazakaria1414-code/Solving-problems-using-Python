n = int(input())
p = list(map(int,input().split()))
d={}
l=0
k=0
for i in range(1,len(p)+1):
    if p[i-1] % 2 == 0:
        d[i]=1
        l+=1
    else:
        d[i]=0
        k+=1
for key, value in d.items():
    if l > k:
        if value == 0:
         print(key)
    else:
        if value == 1:
         print(key)
