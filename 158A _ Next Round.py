import sys
input = sys.stdin.readline
n ,k= map(int, input().split())
deg= list(map(int, input().split()))
deg.sort(reverse=True)
y =0
for i in deg:
    if i>=deg[k-1] and i>0:
        y+=1
print(y)
