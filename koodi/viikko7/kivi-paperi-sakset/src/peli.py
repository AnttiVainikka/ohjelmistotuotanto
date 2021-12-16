from kps import KiviPaperiSakset

def aloita_peli(pelityyppi):
        if pelityyppi not in ["a","b","c"]:
            return False

        print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")

        kps = KiviPaperiSakset()
        if pelityyppi == "a":
            kps.pelaaja_vastaan_pelaaja()
        if pelityyppi == "b":
            kps.pelaaja_vastaan_tekoaly(False)
        if pelityyppi == "c":
            kps.pelaaja_vastaan_tekoaly(True)
        return True
