n = int(input())

home = []
away = []

for _ in range(n):
    h, a = map(int, input().split())
    home.append(h)
    away.append(a)

count = 0

for h in home:
    for a in away:
        if h == a:
            count += 1

print(count)
