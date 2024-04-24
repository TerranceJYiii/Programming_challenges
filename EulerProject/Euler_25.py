print("""The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?""")

n = int(input("\nPlease provide the input \n"))
i = 2
n1 = 1
n2 = 1 
l2 = 1
while l2 < n:
    n1 += n2
    n2 += n1
    i += 2
    l2 = len(str(n2))

print(n1,"\n")
print(n2,"\n")
print(i)
 