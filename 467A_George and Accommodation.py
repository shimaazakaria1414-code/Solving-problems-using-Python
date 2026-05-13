n=int(input())
j=0
for i in range(n):
    a,b=map(int,input().split())
    r=b-a
    if r >=2:
        j+=1
print(j)   
