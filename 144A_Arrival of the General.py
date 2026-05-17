n= int(input())
num = list(map(int, input().split()))
a=num.index(max(num))
b=n - 1 -num[::-1].index(min(num))
if a > b :
    print(a+n-2-b)
 
else:
       
    print(a+n-1-b) 
