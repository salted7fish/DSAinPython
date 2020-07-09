
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

    def transfunc(self, sigma):


        tf = [[0 for i in range(sigma)] for j in range(self.pattLen + 1)]

        for q in range(self.pattLen + 1):
            for a in range(sigma):
                k = min(self.pattLen, q + 1)

                while (self.suffix(self.patt[0: q] + chr(a), self.patt[0: k]) == False):
                    k -= 1

                tf[q][a] = k

        return tf

    def getnextarray(self):
        m = self.pattLen
        i, j = 1, 0
        next = [0] * m

        while i < m:
            if self.patt[i] == self.patt[j]:
                next[i] = j + 1
                i += 1
                j += 1
            elif j > 0:
                j = next[j - 1]
            else:
                i += 1

        return next

    def Naive(self):
        m = self.pattLen
        n = self.textLen
        for i in range(n - m + 1):
            if self.match(self.text[i: i + m], self.patt[0: m]):
                print("Pattern occurs with shift " + str(i))
                return i

        print("No match")
        return -1

    def RabinKarp(self, d=127, q=10007):
        m = self.pattLen
        n = self.textLen
        h = pow(d, m - 1, q)
        p = t = 0

        for i in range(m):
            p = (d * p + ord(self.patt[i])) % q
            t = (d * t + ord(self.text[i])) % q

        for s in range(n - m + 1):
            if p == t:
                if self.match(self.text[s: s + m], self.patt[0: m]):
                    print("Pattern occurs with shift " + str(s))
                    return s
            if s < n - m:
                t = (d * (t - h * ord(self.text[s])) + ord(self.text[s + m])) % q

        print("No match")
        return -1

    def FiniteAutomaton(self, sigma=127):
        m = self.pattLen
        n = self.textLen
        q = 0
        tf = self.transfunc(sigma)

        for i in range(n):
            q = tf[q][ord(self.text[i])]
            if q == m:
                print("Pattern occurs with shift " + str(i - m + 1))
                return i - m + 1

        print('No match.')
        return -1

    def KnuthMorrisPratt(self):
        m = self.pattLen
        n = self.textLen
        next = self.getnextarray()
        i = j = 0

        while i < n:
            if self.text[i] == self.patt[j]:
                if j == m - 1:
                    print("Pattern occurs with shift " + str(i - m + 1))
                    return i - m + 1
                i += 1
                j += 1
            elif j > 0:
                j = next[j - 1]
            else:
                i += 1

        print('No Match.')
        return -1