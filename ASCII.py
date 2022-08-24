
def have():
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphaRes = ""
    start = 65
    for ltr in alpha:
        val = str(ord(ltr))
        ddg,dg = int(val[0]),int(val[1])
        nxt1,nxt2 = (ord(ltr)-start + ddg) % 26, (ord(ltr) - start + dg) % 26
        alphaRes += chr(nxt1 + start) + chr(nxt2 + start)
    
    encryptor = {}
    for idx, val in enumerate(alpha):
        encryptor[val] = alphaRes[idx] + alphaRes[idx + 1]
    return encryptor

encryptor = have()
word = "Hello"
ans= ""
for ltr in word.upper():
    ans += encryptor[ltr]
print(ans)
        
        





