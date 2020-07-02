
class StringMatching:
    def __init__(self, text, patt):
        self.text = text
        self.patt = patt
        self.textLen = len(text)
        self.pattLen = len(patt)

    def match(self, t, p):
        for i in range(self.pattLen):
            if t[i] != p[i]:
                return False

        return True

    def char2int(self, c):
        rt = ord(c) - ord('a') + 1
        return rt

    def Naive(self):
        for i in range(self.textLen - self.pattLen + 1):
            if self.match(self.text[i: i + self.pattLen], self.patt[0: self.pattLen]):
                print("Pattern occurs with shift " + str(i))
                return None

        print("No match")

    def RabinKarp(self, d, q=10007):
        h = pow(d, self.pattLen - 1, q)
        p = t = 0

        for i in range(self.pattLen):
            p = (d * p + self.char2int(self.patt[i])) % q
            t = (d * t + self.char2int(self.text[i])) % q

        for s in range(self.textLen - self.pattLen + 1):
            if p == t:
                if self.match(self.text[s: s + self.pattLen], self.patt[0: self.pattLen]):
                    print("Pattern occurs with shift " + str(s))
                    return None
            if s < self.textLen - self.pattLen:
                t = (d * (t - h * self.char2int(self.text[s])) +
                     self.char2int(self.text[s + self.pattLen])) % q

        print("No match")

    def FiniteAutomaton(self):
        pass

    def KnuthMorrisPratt(self):
        pass