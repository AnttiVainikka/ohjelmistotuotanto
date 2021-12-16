from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu

class KiviPaperiSakset:
    def __init__(self,muisti=10):
        self.tekoaly = TekoalyParannettu(muisti)
        self.tuomari = Tuomari()
        self._siirto = 0

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
    
    def aktivoi_tuomari(self,ekan_siirto,tokan_siirto):
        self.tuomari.kirjaa_siirto(ekan_siirto,tokan_siirto)
        self.tekoaly.aseta_siirto(ekan_siirto)
        print(self.tuomari)
    
    def lopeta_peli(self):
        print("Kiitos!")
        print(self.tuomari)

    def anna_siirto(self):
        self._siirto = self._siirto + 1
        self._siirto = self._siirto % 3

        if self._siirto == 0:
            return "k"
        elif self._siirto == 1:
            return "p"
        else:
            return "s"

    def pelaaja_vastaan_pelaaja(self):
        while True:
            ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
            tokan_siirto = input("Toisen pelaajan siirto: ")
            if not self._onko_ok_siirto(ekan_siirto) or not self._onko_ok_siirto(tokan_siirto):
                break
            self.aktivoi_tuomari(ekan_siirto,tokan_siirto)
        self.lopeta_peli()

    def pelaaja_vastaan_tekoaly(self,parempi):
        while True:
            ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
            if parempi:
                tokan_siirto = self.tekoaly.anna_siirto()
            else:
                tokan_siirto = self.anna_siirto()

            print(f"Tietokone valitsi: {tokan_siirto}")

            if not self._onko_ok_siirto(ekan_siirto):
                break

            self.aktivoi_tuomari(ekan_siirto,tokan_siirto)
        self.lopeta_peli()
