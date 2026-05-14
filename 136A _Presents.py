n=int(input())
m= list(map(int,input().split()))
my_dict = {i: m[i-1] for i in range(1,n+1)}
sorted_dic = dict(sorted(my_dict.items(), key=lambda item: item[1]))
for key in sorted_dic:
    print(key, end=" ")
