print("""Project Euler 4: Largest palindrome product
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.""")

def generate_Palindrome():
    palindromes_with_6_digits = []
    for i in range(6,10):
        for j in range(10):
            for k in range(10):
                current_palindrome = ''.join([str(i),str(j),str(k),str(k),str(j),str(i)])
                palindromes_with_6_digits.append(int(current_palindrome))
    return palindromes_with_6_digits

def ifabiggerthan1000(a,b):
    if a > 1000:
        for i in range(2,12):
            if a % i == 0:
                a /= i
                b *= i
                break
    if a > 1000:
        for i in range(2,12):
            if a % i == 0:
                a /= i
                b *= i
                break
    return (a,b)
    

                
def find_multiple(n):
    num = n
    a = 1
    can_divide = True
    success = False
    fail = False
    while can_divide and not success and not fail:
        for i in range(2,200):
            if num % i == 0:
                a *= i
                num //= i
                if 100<=a<1000 and 100<=num<1000:
                    success = True
                elif a > 1000:
                    fail = True
                break
            if i == 199:
                can_divide = False
    a,num = ifabiggerthan1000(a,num)
    if 100<=a<1000 and 100<=num<1000:
        success = True
    print(f"{a} and {num} from {n}" )
    return a,num,success


palindrome_list = generate_Palindrome()
success = False
for i in range(len(palindrome_list)):
    if not success:
        num = palindrome_list[-i-1]
        a,b,success = find_multiple(num)
    else:
        break
print(f"{a} x {b} = {num}")

