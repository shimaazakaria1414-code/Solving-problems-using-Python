n = int(input())
s = input().upper()
j = 0
k = 0
for i in range(n):
    if s[i] == 'A':
        j += 1
    elif s[i] == 'D':
        k += 1

if  j > k:
      print("Anton")
elif k > j:
      print("Danik")        
else :
      print("Friendship")
