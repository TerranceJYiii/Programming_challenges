with open("Task_Day2.txt","r") as infile:
    lines = infile.readlines()

# x0 = row (UD), y1 = col (LR)
new_numpad = {"1":"1141", 
              "2":"2263", "3":"1274", "4":"4384",
              "5":"5556", "6":"25A7", "7":"36B8", "8":"47C9","9":"9899",
              "A":"6AAB", "B":"7ADC","C":"8BCC",
              "D":"BDDD"}
 
now = "5"
for line in lines:
    for each in line:
        if each == "U":
            now = new_numpad[now][0]
        elif each == "D":
            now = new_numpad[now][2]
        elif each == "L":
            now = new_numpad[now][1]
        elif each == "R":
            now = new_numpad[now][3]

    print(now)
          