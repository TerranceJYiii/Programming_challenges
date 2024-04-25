with open("Task_Day14.txt","r") as infile:
    lines = infile.readlines()

def distance_travelled(time, period, speed, runtime):
    period_distance = (time // period) * speed * runtime
    additional_distance = min(time%period, runtime) * speed
    return (period_distance + additional_distance)


time = 2503

results = []
for line in lines:
    line = line.split()
    # name, speed, runtime, period = line[0], line[3], line[6], line[-2]
    speed, runtime, resttime = map(int,[line[3], line[6], line[-2]])
    results.append(distance_travelled(time,resttime+runtime,speed,runtime))

print(results)
print(max(results))




