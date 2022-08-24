def place(stringy):
    if len(stringy) == 0:
        return ''
    if len(stringy) == 1:
        return stringy
    first = stringy[0]
    last = stringy[-1]
    return first + last + place(stringy[1:-1])



msg = "Hello my friends I am here to tell you that this encryption can be decrypted easily"
msgEncrypted = []
for wrd in msg.split():
    msgEncrypted.append(place(wrd))

print(" ".join(msgEncrypted))