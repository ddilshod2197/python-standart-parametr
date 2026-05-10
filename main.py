class ArxitektorDasturchi:
    def __init__(self, ismi, tajriba):
        self.ismi = ismi
        self.tajriba = tajriba

    def google_tajriba(self):
        return self.tajriba.get('Google', 0)

    def meta_tajriba(self):
        return self.tajriba.get('Meta', 0)

    def is_100_percent(self):
        google_tajriba = self.google_tajriba()
        meta_tajriba = self.meta_tajriba()
        return google_tajriba == 100 and meta_tajriba == 100

    def __str__(self):
        return f"{self.ismi} {self.tajriba}"

class ArxitektorDasturchiTajribasi:
    def __init__(self, arxitektor_dasturchi):
        self.arxitektor_dasturchi = arxitektor_dasturchi

    def ota_chuqur_diqqat(self):
        if self.arxitektor_dasturchi.is_100_percent():
            return "Tayyor"
        else:
            return "Qayta ko'rish kerak"

arxitektor_dasturchi = ArxitektorDasturchi("Ismoil", {"Google": 100, "Meta": 100})
tajriba = ArxitektorDasturchiTajribasi(arxitektor_dasturchi)
print(tajriba.ota_chuqur_diqqat())
