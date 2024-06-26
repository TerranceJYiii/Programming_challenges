print("""You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?""")

def isleap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    return False
        

monthsday = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

day = 2
dayofmonth = 1
month = 1
year = 1901

numofSunday = 0
dayinmonth = 31

while(year != 2001):

    day +=1
    dayofmonth+= 1

    if dayofmonth > dayinmonth:
        dayofmonth = 1
        month += 1
        if month == 13:
            year += 1
            month = 1
        
        if month != 2:
            dayinmonth = monthsday.get(month)
        else:
            if isleap(year):
                dayinmonth = 29
            else:
                dayinmonth = 28

    if day%7 == 0 and dayofmonth == 1:
        numofSunday += 1

    # print(dayofmonth, "/", month, "/", year, day%7)
print(numofSunday)




