s = input().lower()
vowels = "aeyiou"
for i in s:
    if i not in vowels:

        print("."+i, end="")
