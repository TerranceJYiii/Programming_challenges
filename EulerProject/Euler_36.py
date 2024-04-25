print("""The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.) """)


def isPalindrome(i):
    stri = str(i)
    l = len(stri)
    for j in range(l//2):
        if stri[j] != stri[l-1-j]:
            return False
    return True

def dectobin(i):
    if i <= 1:
        return i
    else:
        return i%2 + 10*(dectobin(i//2))

anslist = []
aa = anslist.append

for i in range(1000000):
    if isPalindrome(i):
        bin = dectobin(i)
        if isPalindrome(bin):
            # print(i,bin)
            aa(i)

print(sum(anslist))
