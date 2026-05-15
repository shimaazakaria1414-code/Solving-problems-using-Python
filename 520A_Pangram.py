import string
p = string.ascii_lowercase
n=int(input())
s = input().lower()
for i in p :
    if i not in s : 
        print("NO")
        break
else:
    print("YES")  
