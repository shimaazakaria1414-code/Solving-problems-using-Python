s = input()
n =set(s)
for i in s:
    if i == '{'or i == '}'or i == ','or i == ' ':
        n.discard(i)
        
print(len(n)) 
