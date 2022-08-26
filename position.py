def have(char, k):
    start = 65
    nxt = (( ord(char) - start ) + k) % 26
    res = chr(nxt + start)
    return res

def encrypt(word):
    ans = ""
    for idx, ltr in enumerate(word):
        ans += have(ltr, idx + 1)
    return ans

def CompleteEncryption(msg):
    msg = msg.upper().split()
    msgEnc = []
    for wrd in msg:
        wrdEnc = encrypt(wrd)
        msgEnc.append(wrdEnc)
    return ' '.join(msgEnc)

msg = "The way is not easy for me to pass But I will try and try again"
print(CompleteEncryption(msg))



