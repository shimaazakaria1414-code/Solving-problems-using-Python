n,t = map(int,input().split())
bg =  list(input().upper())
for _ in range(t):
    i=0
    while i< n-1:
        if bg[i]=="B"and bg[i+1]=="G":
            bg[i], bg[i +1] = bg[i + 1], bg[i]
            i+=2
        else:
            i+=1
print("".join(bg))                
