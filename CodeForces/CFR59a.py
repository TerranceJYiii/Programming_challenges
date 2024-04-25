#CodeForce Round 59a Word

word = input()
low, high = 0,0
for c in word:
    if c.isupper():
        high += 1
    else:
        low += 1
if low >= high:
    print(word.lower())
else:
    print(word.upper())