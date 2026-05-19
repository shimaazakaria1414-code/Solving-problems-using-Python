t = int(input())
n=[]
for _ in range(t):
    m= int(input())
    p= ((m+1)//2)-1
    n.append(f"{p}")
print("\n".join(n))   
