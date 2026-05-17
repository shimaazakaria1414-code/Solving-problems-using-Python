,b,c = map(int,[input()for _ in range(3)])
print(max(
    a + b + c,
    a * b * c,
    (a + b) * c,
    a * (b + c),
    a + b * c,
    a * b + c
))
