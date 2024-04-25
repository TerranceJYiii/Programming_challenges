print("""In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins? """)

basecoindict = {"1":1, "2":2, "5":5, "10":10, "20":20, "50":50, "100":100, "200":200}
basecoin = [1,2,5,10,20,50,100,200]

i = 1

for a in range(3):
    for b in range(int(1+(200 - 100*a)/50)):
        for c in range(int(1+(200 - 100*a - 50*b)/20)):
            for d in range(int(1+(200 - 100*a - 50*b - 20*c)/10)):
                for e in range(int(1+(200 - 100*a - 50*b - 20*c - 10*d)/5)):
                    for f in range(int(1+(200 - 100*a - 50*b - 20*c - 10*d - 5*e)/2)):
                        i+=1

print(i)