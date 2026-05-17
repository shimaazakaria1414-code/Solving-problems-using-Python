n= int(input())
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
num3=len(set(num1[1::]+num2[1::]))
 
if n == num3:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")   
