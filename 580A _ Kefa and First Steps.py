t = int(input())
n = list(map(int,input().split()))
j=1
best=1
for i in range(1,len(n)):
    if n[i]>=n[i-1]:
        j+=1
    else:
        j=1
    best = max(best, j)
print(best)    
 
