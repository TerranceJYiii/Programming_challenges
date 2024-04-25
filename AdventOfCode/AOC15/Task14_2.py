with open("Task_Day14.txt","r") as infile:
    lines = infile.readlines()

def travelling(time, period, speed, runtime):
    if (time%period < runtime):
        return speed
    return 0

time = 2503

players = []
for line in lines:
    line = line.split()
    name, speed, runtime, resttime = line[0], line[3], line[6], line[-2]
    players.append([int(resttime) + int(runtime), int(speed), int(runtime)])

results = [0] * 9
distance = [0] * 9

for t in range(time):
    for i in range(9):
        distance[i] += travelling(t, *players[i])
    temp_max = max(distance)
    for each in [i for i in range(9) if distance[i] == temp_max]:
        results[each] += 1
    # print(distance)
    # print(results)
    # print()

print(results)
print(max(results))