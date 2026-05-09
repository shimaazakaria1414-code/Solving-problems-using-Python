n = int(input())
s = input()
j=0
for i in range(1, n):
    if s[i] == s[i-1]:
        j+=1
print(j)
