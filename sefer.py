
class Sefer:
    def __init__(self,sefer_saati,yolcu_kapasitesi,mevcut_yolcu):
        self.sefer_saati = sefer_saati
        self.yolcu_kapasitesi = yolcu_kapasitesi
        self.mevcut_yolcu = mevcut_yolcu
        self.durak = []
    def addDurak(self,durak_obj):
        self.durak.append(durak_obj)
    def getDuraklar(self):
        return self.durak
    
    def getYolcuKapasitesi(self):
        return self.yolcu_kapasitesi
    
    def getMevcutYolcu(self):
        return self.mevcut_yolcu
    
    def getSefersaati(self):
        return self.sefer_saati
    
    def updateMevcutYolcu(self,yeni_miktar):
        self.mevcut_yolcu += yeni_miktar
       