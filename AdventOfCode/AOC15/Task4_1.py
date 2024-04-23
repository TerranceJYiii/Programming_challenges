from hashlib import md5

line = "bgvyzdsv"

i = 0
for i in range(10000000):
    temp = line + str(i)
    encoded = md5(temp.encode()).hexdigest()
    # Task4_1: if encoded[:5] == "00000": 
    if encoded[:6] == "000000":
        print(i)
        break