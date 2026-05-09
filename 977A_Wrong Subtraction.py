a, b = map(int, input(). split())
for i in range(1, b + 1):
    if a % 10 != 0:
        a -= 1
    else:
        a //= 10
print(a)
