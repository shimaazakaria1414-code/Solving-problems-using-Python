s = input().split("WUB")
print(" ".join(s).strip(" "))

#anthor solution
s = input()
words = s.replace("WUB", " ").split()
print(" ".join(words))
