s = input()
j = 0
k= 0
for i in s:
    if i.islower():
        j += 1
    else:
        k += 1
if j >= k:
    print(s.lower())
else:   
    print(s.upper())
  
