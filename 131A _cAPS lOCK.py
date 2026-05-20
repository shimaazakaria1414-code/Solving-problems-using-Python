s1=input()
if len(s1)==1:
    print(s1.swapcase())
elif (s1.isupper()
    or s1[0].islower() 
    and s1[1::].isupper()):

        print(s1.swapcase()) 
else:
    print(s1) 
