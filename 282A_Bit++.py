import sys
input = sys.stdin.readline
n= int(input())
x = 0
for i in range(n):
    statement = input().strip()
    if statement == "X++" or statement == "++X":
      x += 1
    elif statement == "X--" or statement == "--X":
      x -= 1
print(x)
