yes=[ "YES","yes","YEs","YeS","Yes","yES","yEs","yeS"]
out=[]
n = int(input())
for _ in range(n):
    s= input()
    if s in yes:
        out.append("YES")
    else:
        out.append("NO")        
print("\n".join(out))  

