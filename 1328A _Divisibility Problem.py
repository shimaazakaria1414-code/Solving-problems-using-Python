n=int(input())
x =0
s=[]
for i in range(n):
    a,b = map(int,input().split())
    if a % b ==0:
        x=0
    else:
        x = b - (a%b)         
    s.append(f"{x}")
print("\n".join(s))      
