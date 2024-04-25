print("""Project Euler 1: Multiples Of 3 or 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.""")

# import sys

###For HACKERRANK
#def triangular_number(number: int) -> int:
#    return (number * number + number) // 2

#t = int(input().strip())

#for _ in range(t):
#    input_number = int(input().strip()) - 1
#    threes = triangular_number(input_number // 3) * 3
#    fives = triangular_number(input_number // 5) * 5
#    fifteens = triangular_number(input_number // 15) * 15
#    final_calculation = threes + fives - fifteens
#    print(final_calculation)

def multiplesOf3and5(number):
    tempset = set(i for i in range(number) if i%3==0 or i%5==0 )
    return sum(tempset)
             
input_number = input("\nPlease provide the input \n")
print(multiplesOf3and5(int(input_number)))