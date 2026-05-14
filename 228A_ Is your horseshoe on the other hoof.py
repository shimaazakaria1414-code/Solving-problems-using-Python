n= list(map(int,input().split()))
s = set(n)
if 4 != len(s):
    print(4 - len(s))
else:
    print(0)
