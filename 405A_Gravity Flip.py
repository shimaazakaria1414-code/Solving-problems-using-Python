n=int(input())
s =map (int,input().split())
p=sorted(s)
a=[]
for i in p:
    a.append(f"{i}")
print(" ".join(a))
