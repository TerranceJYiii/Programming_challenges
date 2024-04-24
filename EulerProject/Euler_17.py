print("""If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.""")

english = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8, 20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6}

n = int(input('\nPlease provide the input\n'))

total = 0
for i in range(1,n+1):
    if i <= 20:
        count = english.get(i)
        print(i, "has", count, "letters" )
    elif i < 100:
        count = english.get(i%10) + english.get((i//10)*10)
        print(i, "has", count, "letters" )
    elif i < 1000:
        if i%100 == 0:
            count = english.get(i//100) + 7
        elif i%100 < 21:
            count = english.get(i//100) + english.get(i%100) + 10
            print(i, "has", count, "letters" )
        else:
            count = english.get(i//100) + english.get(((i%100)//10)*10) + english.get(i%10) + 10
            print(i, "has", count, "letters" )
    else:
        count = 11
        print(i, "has 11 letters" )
    
    total += count

print(total)