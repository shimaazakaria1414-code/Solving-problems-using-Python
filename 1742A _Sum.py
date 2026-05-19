t = int(input())
o=""
p=""
for _ in range(t):
    a,b,c = map(int,input().split())
    if a+b==c or a+c==b or b+c==a:
        p="YES"
    else:
        p="NO"
    o=o+p+"\n"

print(o)
