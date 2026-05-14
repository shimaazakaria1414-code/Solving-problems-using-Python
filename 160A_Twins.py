n=int(input())
m= list(map(int,input().split()))
m.sort(reverse= True)
total=sum(m)
count=0
my_sum=0
for i in m:
    my_sum += i
    count += 1
 
    if my_sum > total - my_sum:
        break
 
print(count)
