x = sorted(map(int, input().split()))
median = x[1]
print(abs(x[0] - median) + abs(x[1] - median) + abs(x[2] - median))
#حل اخر 
m= sorted(map(int,input().split()))
print(max(m)-min(m))
