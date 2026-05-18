n = int(input())
d = {}
result = []

for _ in range(n):
    s = input()

    if s not in d:
        d[s] = 1
        result.append("OK")
    else:
        new_name = s + str(d[s])
        result.append(new_name)

        d[s] += 1
        d[new_name] = 1

print("\n".join(result))
