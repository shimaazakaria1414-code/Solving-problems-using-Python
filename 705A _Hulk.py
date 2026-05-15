n=int(input())
a =[]
for i in range(1,n+1):
    
    if i % 2 !=0:
        
        a.append("I hate")
        
    else:
        a.append("I love")
        
    if i != n:
        a.append("that") 
    else:
        a.append("it")    
          
print(" ".join(a))
