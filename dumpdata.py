"""
üçkuyular iskleden kalkan otobüs narlıdereye gidiyor  -> x to y
toplam 41 sefer yapıyor 
havanın 3 koşulu var
1 sefer 80 yolcu alabilir 
günün önemli saatleri vardır bu saatlerde durakta yolcu fazla olacak
(6-9 arası ve 4-7 arası)

X VE Y ARASINDAKİ DURAKLAR  30 durak var 
['Hava Hastanesi' 'Adnan Saygun Sanat Merkezi' 'Fahrettin Altay Meydan 5'
 'kuyular skele Son Durak' 'Fahrettin Altay Meydan 9 '
 'Fahrettin Altay Meydan 2' 'Beyaz' 'Balova Kahveler' 'Molla Kuyusu'
 ' Bankas Evleri' 'Teleferik' 'Hoca' 'Drtyol' 'Dokuz Eyll' 'Kantar' 'zsu'
 'Gzel Sanatlar Fakltesi' 'Balc' 'Narldere tfaiye' 'Narldere Cami' 'Uluda'
 'Kprba' 'Siteler' 'ehitlik' 'Narldere Belediye' 'Narldere Piknik Yeri'
 'Profesr Doktor Aziz Sancar Ortaokulu' 'retmenler' 'z Mavikent'
 'Narldere' 'Narldere Huzur']



"""

import random
from sefer import Sefer
from durak import Durak


def genarate_random_val(first_number,last_number):
    
    random_number = random.randint(first_number, last_number)
    return random_number


def sefer_baslat(sefer_saatleri,max_kapasite,durak_sayisi):
    for sefer_no in range(0,len(sefer_saatleri)):
        ilk_durak_yolcusu = ilk_durak(max_kapasite)
        sefer_obj = Sefer(sefer_saati=sefer_saatleri[sefer_no],yolcu_kapasitesi=max_kapasite,mevcut_yolcu=ilk_durak_yolcusu)
        a,b,c = sefer_saatine_gore_uret(sefer_obj)
        yeni_ilk_durak = Durak(1,ilk_durak_yolcusu,ilk_durak_yolcusu,0,0)
        sefer_obj.addDurak(yeni_ilk_durak)
        durakları_gez(durak_sayisi,sefer_obj,80,a,b,c)
        son_durak(sefer_obj,durak_sayisi)

        # ilk ve son durak hariç durakları gezdi ilk durak sefer başlangıcında alındı
        # bu satırda son durak fonksiyonu çağrılamı ve kimse binden herkes inmeli 
        
        for durak in sefer_obj.durak:
            print(f"durak No: {durak.id}Durakta bekleyen Yolcu sayısı = {durak.seferi_bekleyen_yolcu}   fakat otobüse binen insan sayısı = {durak.sefere_binen_yolcu} ve bunun yanında bu durakta = {durak.seferden_inen_yolcu} kişi indi")
        break 

def durakları_gez(durak_sayisi,sefer_obj,max_kapasite,a,b,c): # fonksiyon ismi saçma
    for durak_no in range(1,(durak_sayisi-1)):
        ara_durak_(sefer_obj,durakno=durak_no+1,a = a,b = b,c = c)

def _generate_aradurak_value(sefer_obj,a=5,b=20,c = 60):
    random_durakta_min_bekleyen = genarate_random_val(a,b)
    random_durakta_max_bekleyen = genarate_random_val(b,c)
    durakta_toplam_bekleyen = genarate_random_val(random_durakta_min_bekleyen,random_durakta_max_bekleyen)
    random_sayi_inen = genarate_random_val(0,sefer_obj.getMevcutYolcu())
    
    return durakta_toplam_bekleyen,random_sayi_inen

def sefer_saatine_gore_uret(sefer_obj,):
    if sefer_obj.getSefersaati() in ["6.00","7.00"]:
        print("sefersaati uyuştu")
    return 5,20,60

def ara_durak_(sefer_obj,durakno,a,b,c):
    durakta_toplam_bekleyen,inen = _generate_aradurak_value(sefer_obj,a,b,c)
    sefer_obj.updateMevcutYolcu((-inen))
    binen = yer_varmi(sefer_obj,durakta_toplam_bekleyen)
    kalan_yolcu = durakta_toplam_bekleyen - binen
    sefer_obj.updateMevcutYolcu(binen)
    new_durak = Durak(durakno,durakta_toplam_bekleyen,binen,inen,kalan_yolcu=kalan_yolcu)
    sefer_obj.addDurak(new_durak)


def yer_varmi(sefer_obj,durakta_toplam_bekleyen):
    mevcut_yer_var_mi = sefer_obj.getMevcutYolcu() < sefer_obj.getYolcuKapasitesi()
    binen = 0
    if mevcut_yer_var_mi:
        mevcut_yer = sefer_obj.getYolcuKapasitesi()-sefer_obj.getMevcutYolcu()
        if  mevcut_yer < durakta_toplam_bekleyen:
            binen = mevcut_yer
        else:
            binen = durakta_toplam_bekleyen

    return binen


def son_durak(sefer_obj,durak_sayisi):
    yeni_son_durak = Durak(durak_sayisi,0,0,sefer_obj.getMevcutYolcu(),0)
    sefer_obj.addDurak(yeni_son_durak)
    sefer_obj.updateMevcutYolcu((-sefer_obj.getMevcutYolcu()))

def ilk_durak(max_kapasite):
   binen = genarate_random_val(1,max_kapasite/2)
   return binen

sefer_baslat(["6.00","7.00"],80,5)

"""
öncesinde sefer ve durak sınıflarının verilerini bir json formatına çevireksin durak bilgileri sefer sınıfının
durak listesinde bulunuyor yani bir sefer geçtiği tüm durakların bilgilerini saklamakta sefer üzerinden bir json oluşturabilirsin
json = dict python için 
pandas kütüphanesini kullanacaksın orda dict to df var o fonksion

hat no sefer baslangiç saati ,sefer_süresi(sefer bitiş zamanı),durak no,alınan yolcu,bekleyen yolcu, toplam yolcu,sefer sayısı 


"""