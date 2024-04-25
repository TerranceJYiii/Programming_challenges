print("""An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000 """)

strings = ""
for i in range(1,500000):
    strings += str(i)

print(len(strings))
print(strings[0])
print(strings[9])
print(strings[99])
print(strings[999])
print(strings[9999])
print(strings[99999])
print(strings[999999])