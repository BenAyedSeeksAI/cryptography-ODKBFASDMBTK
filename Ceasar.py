

def have(k):
    start = 65
    alpha = "".join(list(map( str , (chr(start+i) for i in range(26)) )))
    alphaRes = ""
    for e in alpha:
        nxt = ( (ord(e) - start) + k)% 26
        alphaRes += chr(nxt + start)
    encryptor,decryptor = {}, {}
    for e,e2 in zip(alpha,alphaRes):
        encryptor[e] = e2
        decryptor[e2] = e
    return encryptor, decryptor

def encryptOrDecrypt(stringy,dec_or_enc, enc = True):
    if enc:
        ans = ""
        for ltr in stringy:
            ans += dec_or_enc[ltr]
        return ans
    ans = ""
    for ltr in stringy:
        ans += dec_or_enc[ltr]
    return ans
    


inpt = input()
k = int(input())
enc,dec = have(k)
# encrypt the input by an k 
ans = encryptOrDecrypt(inpt.upper(),enc)
print(ans)
# return original input by decrypting the cypher
inpt = encryptOrDecrypt(ans, dec, enc=False)
print(inpt)