s = input()
j = 1
for i in range(1,len(s)):
   if  s[i] == s[i-1]:
      j += 1
      if j >= 7:
        print("YES")   
        break  
   else:
      j = 1
else:      
   print("NO")   
#Another solution   
s = input().strip()

if "0000000" in s or "1111111" in s:
    print("YES")
else:
    print("NO")
