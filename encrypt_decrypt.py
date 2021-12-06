class ecrypt_decrypt:
    alpha=""
    key=""
    def __init__(self,alphabet,key):
        self.alpha=alphabet
        self.key=key
    def cypher_shift(self,ch,key):
        key%=len(self.alpha)
        if ch in self.alpha:
            if key>0:
                return self.alpha[(self.alpha.find(ch)+key)%len(self.alpha)]
            elif key<0:
                return self.alpha[((self.alpha.find(ch)+key)+len(self.alpha))%len(self.alpha)]
        return ch
    def encode(self,text):
        enc=""
        r=0
        for i in range(len(text)):
            if text[i] in self.alpha:
               enc += self.cypher_shift(text[i],self.alpha.find(self.key[r]))
            else:
                enc+=text[i]
            r+=1
            if r==len(self.key):
                r=0
        return enc
    def decode(self,text):
        dec=""
        r=0
        for i in range(len(text)):
            if text[i] in self.alpha:
               dec += self.cypher_shift(text[i],self.alpha.find(self.key[r])*-1)
            else:
               dec+=text[i]
            r+=1
            if r==len(self.key):
                r=0
        return dec
def is_corerect(alpha,key):
    for i in key:
        if i not in alpha:
            return False
    return True

alphabet=input("Enter a string alphabet ")
key=input("Enter a string key ")
while is_corerect(alphabet,key)==False or len(alphabet)==0 or len(key)==0:
    print("invalid input all characters in key need to pressent in alphabet")
    alphabet=input("Enter a string alphabet ")
    key=input("Enter a string key ")
ed=ecrypt_decrypt(alphabet,key)
while True:
    text=""
    sel=int(input("1 Encode\n2 Decode\nOther exit "))
    if sel>2 or sel<1:
        break
    if sel==1:
        text=input("Enter text to encode ")
        print("Encoded: ")
        print(ed.encode(text))
    elif sel==2:
        text=input("Enter text to decode ")
        print("Decoded: ")
        print(ed.decode(text))
