print("""Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?""")

print("# ans for 20x20 = 137846528820")

def countroute(ver, hor):
    sum = 0
    if ver == hor:
        if ver == 2:
            sum += 3
            return sum
        elif ver == 3:
            sum += 10
            return sum
        elif ver == 4:
            sum += 35
            return sum
        elif ver == 5:
            sum += 126
            return sum
        elif ver == 6:
            sum += 462
            return sum
        elif ver == 7:
            sum += 1716
            return sum
        elif ver == 8:
            sum += 6435
            return sum
        elif ver == 9:
            sum += 24310
            return sum
        elif ver == 10:
            sum += 92378
            return sum
        elif ver == 11:
            sum += 352716
            return sum
        elif ver == 12:
            sum += 1352078
            return sum
        elif ver == 13:
            sum += 5200300
            return sum
        elif ver == 14:
            sum += 20058300
            return sum
        elif ver == 15:
            sum += 77558760
            return sum
        elif ver == 16:
            sum += 300540195
            return sum
        elif ver == 17:
            sum += 1166803110
            return sum
        elif ver == 18:
            sum += 4537567650
            return sum
        elif ver == 19:
            sum += 17672631900
            return sum
        
        
    if hor > 2:
        for i in range(1, ver+1):
            sum += countroute(i, hor-1)
    else:
        for i in range(ver):
            sum += i+1
    return sum


n = int(input('\nPlease provide the input\n'))
# for n in range(1,10):
ans = countroute(n,n)
print(ans*2)



#alternate solution (actually real efficient)
1-1-1-1
1-2-3-4
1-3-6-10
1-4-10-20