print("""A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part. """)
def fractionToDecimal(numr, denr):
 
    
    res = ""
 
    # Create a map to store already seen remainders. Remainder is used as key and its position in result is stored as value. Note that we need position
    # for cases like 1/6.  In this case, the recurring sequence doesn't start from first remainder.
    mp = {}
 
    # Find first remainder
    rem = numr % denr
 
    # Keep finding remainder until either
    # remainder becomes 0 or repeats
    while ((rem != 0) and (rem not in mp)):
 
        # Store this remainder
        mp[rem] = len(res)
 
        # Multiply remainder with 10
        rem = rem * 10
 
        # Append rem / denr to result
        res_part = rem // denr
        res += str(res_part)
 
        # Update remainder
        rem = rem % denr
 
    if (rem == 0):
        return ""
    else:
        return res[mp[rem]:]
 
max = 1
maxrec = 1
for i in range(3, 1000):
    res = fractionToDecimal(1, i)
    
    if (res == ""):
        continue
    else:
        reslen = len(res)
        if reslen > maxrec:
            maxrec = reslen
            max = i

print(max, maxrec)