from hashlib import md5

input_id = "ugkcyxxp"
ans = []
i = 0
while len(ans)<8:
    data = input_id + str(i)
    result = md5(data.encode())
    if result.hexdigest()[:5] == "00000":
        ans.append(result.hexdigest()[5])
    i += 1
    
print(ans)
print("".join(ans))