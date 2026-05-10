word = input().strip()
word1 = input().strip()
s = []
for i in range(len(word),0,-1):
    s.append(word[i-1])
if s == list(word1):
    print("YES")
else:
    print("NO")   
#Another solution
word = input().strip()
word1 = input().strip()
if word == word1[::-1]:
    print("YES")
else:
    print("NO")    
