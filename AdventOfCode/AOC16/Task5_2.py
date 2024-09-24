from hashlib import md5

input_id = "ugkcyxxp"
ans = [' ',' ',' ',' ',' ',' ',' ',' ']
valid = '01234567'
i = 0
while ' ' in ans:
    data = input_id + str(i)
    result = md5(data.encode()).hexdigest()
    if result[:5] == "00000" and result[5] in valid:
        if ans[int(result[5])] == ' ':
            ans[int(result[5])] = result[6]    
    i += 1
    
print(ans)
print("".join(ans))