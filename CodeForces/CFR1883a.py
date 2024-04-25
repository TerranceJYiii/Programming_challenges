#CodeForce Round 1883a Morning

numpad = "1234567890"
n = int(input())
for test in range(n):
    pin = "1" + input()
    ans = 4
    for i in range(4):
        ans += abs(numpad.index(pin[i+1]) - numpad.index(pin[i]))
    print(ans)