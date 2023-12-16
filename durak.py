class Durak:
    def __init__(self,id,bekleyen_yolcu,binen_yolcu,inen_yolcu,kalan_yolcu):
        self.id = id,
        self.seferi_bekleyen_yolcu = bekleyen_yolcu
        self.kalan_seferi_bekleyen_yolcu = kalan_yolcu
        self.sefere_binen_yolcu = binen_yolcu
        self.seferden_inen_yolcu = inen_yolcu


    def get_id(self):
        return self.id

    def get_seferi_bekleyen_yolcu(self):
        return self.seferi_bekleyen_yolcu
    
    def get_sefere_binen_yolcu(self):
        return self.sefere_binen_yolcu

    def get_seferden_inen_yolcu(self):
        return self.seferden_inen_yolcu
    


    def update_id(self,new_id):
        self.id = new_id

    def update_seferi_bekleyen_yolcu(self,seferi_bekleyen_yolcu):
        self.seferi_bekleyen_yolcu = seferi_bekleyen_yolcu
    
    def update_sefere_binen_yolcu(self,sefere_binen_yolcu):
        self.sefere_binen_yolcu = sefere_binen_yolcu

    def update_seferden_inen_yolcu(self,seferden_inen_yolcu):
        self.seferden_inen_yolcu = seferden_inen_yolcu