ALPH=26
     
class Cryptography():
    def __init__(self,text, steps):
        self.original_text = text
        self.latest_text = text
        self.steps = steps
        self.crypted_text = ""
        self.decrypted_text = ""
    def Make_encryption(self, encrypt_flag):
        ResponseLine = []
        Line = self.latest_text.split(" ")
        if encrypt_flag:
            for word in Line:
                res = self.crypt_word(word)
                ResponseLine.append(res)
            self.crypted_text = " ".join(ResponseLine)
            self.latest_text = self.crypted_text
        else:
            for word in Line:
                res = self.decrypt_word(word)
                ResponseLine.append(res)
            self.decrypted_text = " ".join(ResponseLine)
            self.latest_text = self.decrypted_text
        return self
    def encryption_operation(self, stry, coef):
        res = ""
        for ltr in stry:
            itr = ""
            if ord(ltr) >= ord("a"):
                itr = chr((((ord(ltr)-ord("a")) + (self.steps * coef)) % ALPH)+ord("a"))
            elif ord(ltr) >= ord("A"):
                itr = chr((((ord(ltr)-ord("A")) + (self.steps * coef)) % ALPH)+ord("A"))
            res+=itr
        return res
    def positional_encryption_operation(self, stry, coef):
        res = ""
        for ind,ltr in enumerate(stry):
            itr = ""
            if ord(ltr) >= ord("a"):
                itr = chr((((ord(ltr)-ord("a")) + ((self.steps + ind + 1)* coef)) % ALPH)+ord("a"))
            elif ord(ltr) >= ord("A"):
                itr = chr((((ord(ltr)-ord("A")) + ((self.steps + ind + 1)* coef)) % ALPH)+ord("A"))
            res+=itr
        return res
    def crypt_word(self, stry):
        res = self.encryption_operation(stry, 1)
        return res
    def decrypt_word(self, stry):
        res = self.encryption_operation(stry, -1)
        return res
stry = "Hello Github from Tunisia"
print(stry)
crp = Cryptography(stry, 5)
print(crp.Make_encryption(encrypt_flag=True).latest_text)
crp1 = Cryptography(stry, 5)
print(crp1.Make_encryption(encrypt_flag=True).Make_encryption(encrypt_flag=False).latest_text)
