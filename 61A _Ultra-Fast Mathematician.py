n1 = input()
n2 = input()
s=[]
for i in range(len(n1)):
    if n1[i]== n2[i]:
        s.append("0")
    else:
        s.append("1")
print("".join(s))
