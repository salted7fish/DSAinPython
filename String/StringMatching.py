
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

    def suffix(self, pqa, pk):
        if pk == '':
            return True
        m = len(pk)
        n = len(pqa)

        for i in range(m):
            if pk[i] != pqa[n - m + i]:
                return False

        return True

    def transfunc(self):
        sigma = 128

        tf = [[0 for i in range(sigma)] for j in range(self.pattLen + 1)]

        for q in range(self.pattLen + 1):
            for a in range(sigma):
                k = min(self.pattLen, q + 1)

                while (self.suffix(self.patt[0: q] + chr(a), self.patt[0: k]) == False):
                    k -= 1

                tf[q][a] = k

        return tf

    def Naive(self):
        for i in range(self.textLen - self.pattLen + 1):
            if self.match(self.text[i: i + self.pattLen], self.patt[0: self.pattLen]):
                print("Pattern occurs with shift " + str(i))
                return None

        print("No match")

    def RabinKarp(self, q=10007):
        d = 128
        h = pow(d, self.pattLen - 1, q)
        p = t = 0

        for i in range(self.pattLen):
            p = (d * p + ord(self.patt[i])) % q
            t = (d * t + ord(self.text[i])) % q

        for s in range(self.textLen - self.pattLen + 1):
            if p == t:
                if self.match(self.text[s: s + self.pattLen], self.patt[0: self.pattLen]):
                    print("Pattern occurs with shift " + str(s))
                    return None
            if s < self.textLen - self.pattLen:
                t = (d * (t - h * ord(self.text[s])) +
                     ord(self.text[s + self.pattLen])) % q

        print("No match")

    def FiniteAutomaton(self):
        q = 0
        tf = self.transfunc()

        for i in range(self.textLen):
            q = tf[q][ord(self.text[i])]
            if q == self.pattLen:
                print("Pattern occurs with shift " + str(i - self.pattLen + 1))
                return None

        print('No match.')

    def KnuthMorrisPratt(self):
        pass
