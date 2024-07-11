print("""Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using Euler_59.txt, a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.""")


with open("Euler_59.txt") as file:
    lines = file.readlines()
    line = lines[0]



alphabet = 'abcdefghijklmnopqrstuvwxyz'
allowed = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890 .,:;+?!/[]()'\""
data = list(map(int,line.split(",")))
l = len(data)

def process(data,key1,key2,key3):
    ans = []
    aa = ans.append
    for n in range(l//3):
        t = n*3
        aa(chr(data[t]^key1))
        aa(chr(data[t+1]^key2))
        aa(chr(data[t+2]^key3))
    if all(bit in allowed for bit in ans):
        word = "".join(ans)
        print(word)
        sum = 0
        for each in ans:
            sum += ord(each)
        print(sum)
        return True
    return False
    # print(word, key1,key2,key3)




def main():
    for i in range(26):
        for j in range(26):
            for k in range(26):
                done = process(data,ord(alphabet[i]),ord(alphabet[j]),ord(alphabet[k]))
                if done:
                    return
            
main()