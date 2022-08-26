def have(char, k):
    start = 65
    nxt = (( ord(char) - start ) + k) % 26
    res = chr(nxt + start)
    return res

def be(char, k):
    start = 65
    idx = (ord(char) - start)
    if k > idx:
        res = 26 - k + idx
        res = chr(res + start)
    else:
        res = idx - k
        res = chr(res + start) 
    return res

def encrypt(word):
    ans = ""
    for idx, ltr in enumerate(word):
        ans += have(ltr, idx + 1)
    return ans

def decrypt(word):
    ans = ""
    for idx, ltr in enumerate(word):
        ans += be(ltr, idx + 1)
    return ans

def CompleteEncryption(msg):
    msg = msg.upper().split()
    msgEnc = []
    for wrd in msg:
        wrdEnc = encrypt(wrd)
        msgEnc.append(wrdEnc)
    return ' '.join(msgEnc)

def CompleteDecryption(msg):
    msg = msg.upper().split()
    msgEnc = []
    for wrd in msg:
        wrdEnc = decrypt(wrd)
        msgEnc.append(wrdEnc)
    return ' '.join(msgEnc)

msg = "The way is not easy for me to pass But I will try and try again"
EncMsg = CompleteEncryption(msg)
print(EncMsg)
DecMsg = CompleteDecryption(EncMsg)
print(DecMsg)



