import numpy as np

with open("Task_Day15.txt","r") as infile:
    lines = infile.readlines()

ingredients = []
calories = []
for line in lines:
    line = line.split()
    cap, dur, flav, text, cal = map(int,[line[2], line[5], line[8], line[11], line[-1]])
    ingredients.append([cap,dur,flav,text])
    calories.append(cal)

for k in range(len(ingredients)):
    print(ingredients[k])

ingredients = np.array(ingredients)
calories = np.array(calories)

print(ingredients)
print(calories)

maxima = 0
for a in range(1,101):
    for d in range(101):
        if a + d > 100:
            break
        for c in range(101):
            if a + d + c > 100:
                break
            if (5*d) < c:
                continue
            for b in range(101):
                if a+b+c+d > 100:
                    break
                if a+b+c+d != 100:
                    continue
                if (b > 5*d) or (2*a + 3*b > 5*c):
                    continue

                teaspoon = np.array([a,b,c,d])
                total_cal = np.dot(teaspoon,calories)
                if  total_cal != 500:           # Task 15_2
                    continue                    # Task 15_2
                score = np.dot(teaspoon,ingredients)
                
                if any(p <= 0 for p in score):
                    temp = 0
                else:
                    temp = 1
                    for s in score:
                        temp *= s
                    maxima = max(temp,maxima)

print(maxima)
                

