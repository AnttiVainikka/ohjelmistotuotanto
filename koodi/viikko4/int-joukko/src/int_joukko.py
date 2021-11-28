KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):

        self.ljono = [0] * kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.alkioiden_lkm = 0


    def kuuluu(self, n):
        return n in self.ljono

    def lisaa(self, n):
        try:
            if not self.kuuluu(n):
                self.ljono[self.alkioiden_lkm] = n
                self.alkioiden_lkm += 1

                if self.alkioiden_lkm % len(self.ljono) == 0:
                    taulukko_old = self.ljono
                    self.kopioi_taulukko(self.ljono, taulukko_old)
                    self.ljono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
                    self.kopioi_taulukko(taulukko_old, self.ljono)

        except IndexError:
            return False
        return True


    def poista(self, n):
        loyty = False
        for i in range(0,len(self.ljono)-1):
            if self.ljono[i] == n:
                self.alkioiden_lkm -= 1
                loyty = True
            if loyty:
                self.ljono[i] = self.ljono[i+1]
        if loyty:
            return True
        return False


    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def palauta_alkioiden_maara(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
