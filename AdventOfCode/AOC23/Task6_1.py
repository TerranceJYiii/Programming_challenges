with open("Task_Day6.txt","r") as infile:
    lines = infile.readlines()

times = list(map(int,lines[0].split()[1:]))
distances = list(map(int,lines[1].split()[1:]))
l = len(times)

ans = 1
for each in range(l):
    time = times[each]
    distance = distances[each]
    for i in range(time):
        if (i*(time-i)) > distance:
            success = time - 2*i + 1
            print(success)
            ans *= success
            break

print(ans)