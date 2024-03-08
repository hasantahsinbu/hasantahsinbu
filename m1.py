from random import randint
import math
import random
import datetime as dt
from random import randint
import datetime
from functools import reduce
import tkinter as tk
rand = randint

def genel_import_et():
    import math
    import random
    import datetime
    from functools import reduce
    import tkinter
    import requests
    import os
    import re
    import re
    import string
    
def küçük(metin):
    s = metin.lower()
    return s


def bhbüyük(metin):
    s = metin.capitalize()
    return s


def ihabüyük(metin):
    s = metin.title()
    return s


def üs(metin):
    s1 = len(metin)

    s2 = len(metin)

    s = s1 ** s2
    return s


def kare_kök(metin):
    s1 = len(metin)

    s = math(s1)
    return s


def toplam(metin):
    s1 = len(metin)

    s2 = len(metin)

    s = s1 + s2
    return s


def ters(metin):
    s = metin.reverse()
    return s


def tç(metin):
    s1 = random.randint(2, 15)

    s2 = len(metin)

    ss1 = s1 + s2

    s = ss1 * s2
    return s


def üs_üs(metin):
    s1 = len(metin)

    s2 = len(metin)

    sss1 = s1 ** s2

    ss1 = len(metin)

    ss2 = len(metin)

    ss2 = ss1 ** ss2

    s = sss1 ** sss2
    return s


def üs_carp(metin):
    s1 = len(metin)

    s2 = len(metin)

    ss1 = s2 ** s1

    s = ss1 * s2
    return s


def üs_kök_üs(metin):
    s1 = len(metin)

    s2 = len(metin)

    sss1 = s1 ** s2

    sss2 = math(sss1)

    s = sss2 ** sss2
    return s


def islem(işlem, metin):
    if işlem == "hepsini büyüt":

        sonuc = büyük(metin)

    elif işlem == "hepsini küçült":

        sonuc = küçük(metin)

    elif işlem == "ilk harfini büyüt":

        sonuc = ihabüyük(metin)

    elif işlem == "cümle düzeni":

        sonuc = bhbüyük(metin)

    elif işlem == "üs":

        sonuc = üs(metin)
    elif işlem == "kare kök":
        
        sonuc = kare_kök(metin)
        
    elif işlem == "toplam":
        
        sonuc = toplam(metin)

    return sonuc


def ATM():
    with open("paraçekmek", "r", encoding="utf-8") as k:
        kart_parası = int(k.read())
        print("mevcut para: ", kart_parası)

    while True:
        s = str(input("Para çekmek için 'ç'ye, eklemek için 'e'ye basınız: "))

        if s == "ç":
            pç = int(input("Kaç TL çekmek istersiniz?: "))
            if pç > kart_parası:
                print("Yetersiz bakiye. Mevcut bakiye: {}".format(kart_parası))
            else:
                kart_parası -= pç
                with open("paraçekmek", "w", encoding="utf-8") as j:
                    j.write(str(kart_parası))
                    print("Kartınızda {} TL kaldı.".format(kart_parası))

        elif s == "e":
            pe = int(input("Kaç TL eklemek istersiniz?: "))
            kart_parası += pe
            with open("paraçekmek", "w", encoding="utf-8") as j:
                j.write(str(kart_parası))
                print("Kartınızda {} TL oldu.".format(kart_parası))

        else:
            print("!!!YANLIŞ İŞLEM SEÇMEYİNİZ!!!")

        if kart_parası <= 0:
            print("Paranız bitti!!!")
            break

        ko = input("Çıkmak için 'çıkmak' yazınız: ")
        if ko.lower() == "çıkmak":
            print("Çıkış yapılıyor....")
            break


def dört_islem_sonucu_toplamı(x, y):
    def t(a, b):
        return a + b

    def ça(a, b):
        return a * b

    def b(a, b):
        return a / b

    def ç(a, b):
        return a - b

    toplamları = t(x, y) + ça(x, y) + b(x, y) + ç(x, y)
    return toplamları


def üs_kök_fakta(lem, x, y):
    if lem == "üs bul":
        return x ** y
    elif lem == "kök bul":
        return x ** 0.5
    elif lem == "faktariyel bul":
        x = int(x)
        f = 1
        for i in range(2, x + 1):
            f *= i
        return f


def tekmi_ciftmi(a):
    if a % 2 == 0:
        return "Sayı çifttir."
    else:
        return "Sayı taktir."


def kilo(b, k):
    bki = k // b * b
    if bki < 18.5:
        return "Zayıfsınız."
    elif 18.5 < bki < 25:
        return "Normalsiniz."
    elif 25 < bki < 40:
        return "Kilonuz fazla."
    elif bki > 134:
        return "Obezsiniz."
    elif bki < 18.5:
        return "Bebek ya da çok zayıfsınız"


def kullanıcı_grisi(ska, sp):
    gh = 5
    while True:
        ka=input("Kullanıcı adı: ")
        p =input("Şifre: ")
        if ka != ska or p != sp:
            gh -= 1
            print("Yanlış giriş!\tKalan hak: ", gh)
            if gh == 0:
                print("Hakkınız bitti!\nÇıkış Yapılıyor...")
                break
        elif ka == ska and sp == sp:
            print("Girişiniz tamamlandı!")
            break


def ebob(sayı1, sayı2):
    i = 1
    ebob = 1
    while (i <= sayı1 and i <= sayı2):

        if (not (sayı1 % i) and not (sayı2 % i)):
            ebob = i
        i += 1


def ekok(sayı1, sayı2):
    i = 2
    ekok = 1
    while True:
        if (sayı1 % i == 0 and sayı2 % i == 0):
            ekok *= i

            sayı1 //= i
            sayı2 //= i


        elif (sayı1 % i == 0 and sayı2 % i != 0):
            ekok *= i

            sayı1 //= i


        elif (sayı1 % i != 0 and sayı2 % i == 0):
            ekok *= i

            sayı2 //= i
        else:
            i += 1
        if (sayı1 == 1 and sayı2 == 1):
            break
    return ekok


def bilgi(ad="girilmedi", soyad="girilmedi", yas="girilmedi"):
    return f"AD: {ad}\nSOYAD: {soyad}\nYAŞ: {yas}"


def giris(a, d):
    p = input(a)
    return p


class calısan():
    def __init__(self, ad, soyad, numara, yaş, maaş, iş):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara
        self.yaş = yaş
        self.maaş = maaş
        self.iş = iş

    def iş_değiştir(self, yeni_iş):
        self.iş = yeni_iş

    def bilgi_goster(self):
        return f"""
        ÇALIŞAN BİLGİLERİ:
        Ad: {self.ad}
        Soyad: {self.soyad}
        Numara: {self.numara}
        Yaş: {self.yaş}
        Maaş: {self.maaş}
        İş: {self.iş}    """

    def maas_arrttır(self, yeni_maaş):
        self.maaş = yeni_maaş
    def __str__(self):
        return "Ad: {}\nSoyad: {}\nYaş: {}\nCinsiyet: {}\nİş: {}\nMaaş: {}".format(self.ad,self.soyad,self.yaş,self.cinsiyet,self.iş,self.maaş)


def tas_kağıt(x, y):
    if x == y:
        return x
    elif (x =="taş"or y == "taş") and (x =="kağıt"or y == "kağıt"):
        return "kağıt"
    elif (x =="makas"or y == "makas") and (x =="kağıt"or y == "kağıt"):
        return "makas"
    elif (x =="makas"or y == "makas") and (x =="taş"or y == "taş"):
        return "taş"
    else:
        return "Doğru bir öğe giriniz!!!"


def sayı_tahmin(tahmin):
    sayı = random.randint(0, 101)
    th = 10
    while True:
        if tahmin < sayı:
            th -= 1
            return "Daha büyük bir sayı giriniz\n", f"Kalan hakkınız{th}"
        elif tahmin > sayı:
            th -= 1
            return "Daha küçük bir sayı giriniz\n", f"Kalan hakkınız{th}"
        else:
            return "Kazandınız!   Sayı:", sayı
            break
        if th == 0:
            return "Kaybettiniz!    Sayı:", sayı
        break


def aralık(x, y):
    l = [*range(x, y + 1)]
    return l


def aralı_toplam(x, y):
    l = [*range(x, y + 1)]
    d = 0
    for i in l:
        d += i
    return d


def geri_say(baslangıc, bitis):
    t = range(baslangıc, bitis, -1)
    return t


def emeklilik(dy, y):
    eme = 65 - y
    if eme > 0:
        return "Emeklilik yılınıza {} yıl kaldı.".format(eme)
    else:
        return "Emeklisiniz"


def tam_bölenler(d):
    b = []
    for i in range(d):
        if d % i == 0:
            b.append(i)
    return b


def çarpanlar(r):
    for i in range(r):
        if r % i == 0:
            p = r / i
            return "{} * {} = {}".format(p, i, r)


def dört_işlem_sonucu(x, y):
    to = str(x + y)
    çı = str(x - y)
    ça = str(x * y)
    bö = str(x / y)
    return "Toplamları: "+ to+ "Farkları: "+ çı+ "Çarpımları: "+ ça+ "Bölümleri: "+ bö


def yas_hespla(dt, yıl):
    yaş = yıl - dt
    return "Yaş: ", yaş


def yazdır(m, d):
    for i in range(d + 1):
        return m


def harfli_ilk_kelimeyi_bu(metin, k):
    return metin
    if len(metin) == k:
        return True


def bolen_doğrumu(x, y):
    if x % y == 0:
        return True
    else:
        return False


def yıl_yas(y, oy):
    return "{}'yaşınıza {} yıl kaldı.".format(oy, oy - y)


def karşılaştır(s1, s2):
    if s1 < s2:
        return "Birinci sayı diğerinden küçüktür."
    elif s1 > s2:
        return "Birinci sayı diğerinden büyüktür."
    else:
        return "Sayılar birbirine eşittir."


def araciftsayı(ba, bi):
    liste = range(ba, bi + 1)
    o = []
    for i in liste:
        if i % 2 == 0:
            o.append(i)
    return o


def kdv(fiyat, kdv):
    tutar = fiyat + (fiyat * kdv)
    return "{} liralık ürünün kdv fiyatı {} TL'dir.".format(fiyat, tutar)


def liste_ekle(liste, *eklenen_eleman):
    h = liste.append(eklenen_eleman)
    return h


def aralık_yazdır(x, y):
    for i in range(x, y + 1):
        return i


def a_y_toplam(a, b):
    f = range(a, b + 1)
    k = 0
    for i in f:
        i += k
        k += 1


def değer_kontrol(değer):
    if değer == str:
        return "Değer yazı ya da metindir"
    elif değer == int:
        return "Değer sayıdır."
    elif değer == float:
        return "Değer noktalı sayıdır."
    elif değer == list:
        return "Değer listedir."
    elif değer == tuple:
        return "Değer demettir."
    elif değer == dict:
        return "Değer sözlüktür."
    elif değer == set:
        return "değer kümedir."
    elif değer == bool:
        return "Değer bool'dur "


def kat_al(liste, sayı):
    for i in liste:
        liste[i] *= sayı
    return liste


def saat():
    f = datetime.datetime.now()
    return "{}:{}".format(f.hour, f.minute)


def ders_notu(puan):
    if puan < 101 and puan > -1:
        if puan > 80 and 100 > puan:
            return "5 aldınız. 'Tebrikler!!!'"
        elif puan > 65 and 80 > puan:
            return '4 aldınız. \'fena değil!\''
        elif puan > 50 and 65 > puan:
            return "3 aldınız. 'daha başarılı olabilirsin!'"
        elif puan > 35 and 50 > puan:
            return "2 aldınız. 'çok çalış!!'"
        elif puan < 35:
            return "1 aldınız. 'başarısız!!!'"
    else:
        return "geçerli not giriniz!"

def asal(sayı):   
    sayac=0    
    for i in range(2,int(sayı)):
         if(int(sayı)%i==0):
            sayac+=1
    if(sayac==0):
         return True
    else:
         return False


def sayıyı_sorgula(sayı=0, i=None):
    def asal_sayı_ic(sayı):   
        sayac=0    
        for i in range(2,int(sayi)):
            if(int(sayı)%i==0):
                sayac+=1
                break
        if(sayac!=0):
            return True
        else:
            return False

    if i == None:
        return None
    else:
        if i == "çift":
            if sayı % 2 == 0:
                return True
            else:
                return False
        elif i == "tek":
            if sayı % 2 == 1:
                return True
            else:
                return False
        elif i == "ondalıklı sayı":
            if sayı == float:
                return True
            else:
                return False
        elif i == "asal sayı":
            if asal_sayı_ic(sayı) == True:
                return True
            else:
                return False
        elif i == "negatif":
            sayı = str(sayı)
            if sayı.startswith("-") == True:
                return True
            else:
                return False
        elif i == "pozitif":
            sayı = str(sayı)
            if sayı.startswith("-") == False:
                return True
            else:
                return False
        elif i == "rakam":
            if 0 < sayı < 10:
                return True
            else:
                return False
        elif i == "sayı":
            if sayı > 10:
                return True
            else:
                return False
        else:
            raise NameError("Böyle bir sayı özelliği yok!")


def aralık_kontrol(sayı, ba, bi):
    return ba <= sayı <= bi

def kişi_bilgisi(ad="girilmedi", soyad="girilmedi", yaş="girilmedi", şehir="girilmedi"):
    return "---------------\n" + f"Ad: {ad}\n" + f"Soyad: {soyad}\n" + f"Yaş: {yaş}\n" + f"Şehir: {şehir}\n" + "---------------"


class hayvan():
    def __init__(self, isim="köpek", ses="hav-hav", **özellikler):
        self.ses = ses
        self.isim = isim
        self.özellikler = özellikler

    def özellik_değiştir(self, **yeni_özellikler):
        self.özellikler.clear()
        self.özellikler.update(yeni_özellikler)
        return self.özellikler

    def isim_değiştir(self, yeni_isim):
        self.isim = yeni_isim

    def sesini_değiştir(self, yeni_ses):
        self.ses = yeni_ses

    def __str__(self):
        return f"İsim: {self.isim} Ses: {self.ses} Özellikler: {self.özellikler}"


def doğru_cevap(soru, seçim, *cevaplar):
    cevaplar = list(cevaplar)
    if seçim not in cevaplar:
        return "doğru seçim yapınız!!!"
    if soru == seçim:
        return "Doğru cevap\nDoğru cevap: " + str(seçim)
    else:
        return "Yanlış cevap\nDoğru cevap: " + str(soru)

def dönüştürme(değer, obje):
    if obje == "sayı":
        try:
            değer = int(değer)
            return değer
        except:
            raise TypeError("liste,demet,küme sayıya dönüştürülmez!")
    elif obje == "yazı-metin":
        try:
            değer = str(değer)
            return değer
        except:
            raise TypeError("liste,demet,küme yazıya dönüştürülmez!")
    elif obje == "liste":
        try:
            değer = list(değer)
            return değer
        except:
            raise TypeError("sayı listeye dönüştürülmez!")
    elif obje == "demet":
        try:
            değer = tuple(değer)
            return değer
        except:
            raise TypeError("sayı demete dönüştürülmez!")
    elif obje == "küme":
        try:
            değer = set(değer)
            return değer
        except:
            raise TypeError("sayı kümeye dönüştürülmez!")
    elif obje == "sözlük":
        try:
            değer = dict(değer)
            return değer
        except:
            raise TypeError("sayı,yazı,#0-liste,#0-demet,#0-küme sözlüğe dönüştürülmez!")
    else:
        raise NameError("Başka bir obje türü yok. Oluşturduysanız kodunuzu hasantahsinay@gmail.com'a atınız.")


class kisi():
    def __init__(self, ad, soyad, yaş, iş, durum, ülke, şehir):
        self.ad = ad
        self.soyad = soyad
        self.yaş = yaş
        self.iş = iş
        self.durum = durum
        self.ülke = ülke
        self.şehir = şehir

    def bilgileri_göster(self):
        return """
        Ad:{}
        Soyad: {}
        Yaş: {}
        İş: {}
        Durum: {}
        Ülke: {}
        Şehir: {}""".format(self.ad, self.soyad, self.yaş, self.iş, self.durum, self)


def liste_oluştur(liste_adı, *elemanlar):
    liste_adı = list(elemanlar)
    return liste_adı


def fibonatça(sınır):
    başgangıç = 0
    başgangıç += 1
    return fibonatça(başgangıç) + fibonatça(başgangıç + 1)


def bölümünden_kalan(bölünen, bölen):
    try:
        return bölünen % bölen
    except:
        raise ZeroDivisionError("bir sayı sıfıra bölünemez.")


def isteneni_döndür(s1, s2, islem):
    if islem == "büyük döndür":
        if s1 > s2:
            return s1
        elif s2 > s1:
            return s2
        else:
            return "Sayılar birbirine eşittir."
    elif islem == "küçük döndür":
        if s1 < s2:
            return s1
        elif s2 < s1:
            return s2
        else:
            return "Sayılar birbirine eşittir."
    elif islem == "büyük basamak":
        s1 = str(s1)
        s2 = str(s2)
        if len(s1) > len(s2):
            return s1
        elif len(s1) < len(s2):
            return s2
        else:
            return "Sayıların basamakları eşittir."
    elif islem == "küçük basamak":
        s1 = str(s1)
        s2 = str(s2)
        if len(s1) < len(s2):
            return s1
        elif len(s1) > len(s2):
            return s2
        else:
            return "Sayıların basamakları eşittir."
    else:
        raise NameError("başka karşılaştırma türü yok.")


def en_fazla_kaldır(nesne_kilosu, yaş, boy):
    kaldırma_gücü = yaş / boy * boy
    if kaldırma_gücü > nesne_kilosu:
        return True
    else:
        return False


class kitap():
    def __init__(self, yazar="GİRİLMEDİ", yayınevi="yok", sayfa_sayısı="GİRİLMEDİ"):
        self.yazar = yazar
        self.yayınevi = yayınevi
        self.sayfa_sayısı = sayfa_sayısı

    def __str__(self):
        return self

    def bilgiler(self):
        return """
        Yazar: {}
        Yayınevi: {}
        Sayfa sayısı:{}""".format(self.yazar, self.yayınevi, self.sayfa_sayısı)


def tarih():
    s = datetime.datetime.now()
    return str(s.day) + "." + str(s.month) + "." + str(s.year)


def çarpan_ayır(sayı):
    o = 0
    for i in range(sayı + 1):
        if i % o == 0:
            return f"{i} x {o} = {sayı}"


def asal_toplam(bi):
    ko = 0
    toplam = []
    while (bi >= ko):
        if ko == 2 or ko % 2 == 1:
            toplam.append(ko)
        ko += 1
    return sum(toplam)


def üs_basamak_toplam(sayı, üs):
    s = list(str(sayı ** üs))
    return sum(s)


def faktariyel_rakam_toplamı(x):
    x = int(x)
    f = 1
    for i in range(2, x + 1):
        f *= i
    return sum(list(str(f)))


def sayı_de_fakta_sayı(sayı):
    sayı = str(sayı)
    l = list(sayı)

    def fac(x):
        x = int(x)
        f = 1
        for i in range(2, x + 1):
            f *= i
        return f

    l = 0
    for i in l:
        l += fac(l[i])
    if l == int(sayı):
        return True
    else:
        return False


def padigital_katlar(sayı, son):
    o = []
    for i in range(son + 1):
        o.append(str(i + 1 * sayı))
        k = ""
    for a in o:
        k += o[a]
    return k


def sınav_puanı(soru_sayısı, doğru=None, yanlış=None, boş_soru=None):
    if doğru == None or yanlış == None or boş_soru == None:
        return None
    if doğru + yanlış + boş_soru != soru_sayısı:
        raise TypeError("Sınav notu oluşturulamadı.")
    else:
        soru_puanı = 100 / soru_sayısı
        puan = (soru_puanı * doğru)
        return "Sınav'dan {} aldınız.".format(int(puan))
def bosluk_kaldır(değer):
    değer=list(değer)
    index=0
    for i in değer:
        if i == " ":
            değer.remove(i)
        index+=1
    değer= "".join(değer)
    değer=değer.split()
    return "".join(değer)

def bilgisayar():
    class bil():
        def __init__(self, isletimsistemi="Linux",*uygulamalar):
            self.uygulamalar    =   list(uygulamalar)
            self.dosyalar       =   []
            self.isletimsistemi =   isletimsistemi 

        def uygulama_sil(self, silinecek_uygulama):
            self.uygulamalar.remove(silinecek_uygulama)

        def uygulama_ekle(self, eklenecek_uygulama):
            self.uygulamalar.append(eklenecek_uygulama)
            
        def dosyaolustur(self,dosyaadı):
            self.dosyalar.append(dosyaadı)

        def dosyasil(self,dosyaadı):
            if dosyaadı in self.dosyalar:
               self.dosyalar.remove(dosyaadı) 
        
        def __str__(self):
            return f"""
Uygulamalar: {self.uygulamalar}
Dosyalar: {self.dosyalar}
İşletim Sistemi: {self.isletimsistemi}"""

    si=bosluk_kaldır(input("İşletim sistemini girin: "))
    hiz=bosluk_kaldır(input("Hızı girin: "))
    sos=bosluk_kaldır(input("Şarj olma süresini girin(%100): "))
    bilgi=bil(isletimsistemi=si)
    while True:
        s=input("""
1.Uygulama Ekle
2.Uygulama Çıkar
3.Dosya Oluştur
4.Dosya Sil
5.Bilgileri Göster
exit --> çıkış
Seçenek (1/2/3/4/5/exit):  
""")
        if s=="1":
            u=input("uygulama adını girin:")
            bilgi.uygulama_ekle(u)
            print("Uygulama eklendi")
        elif s=="2":
            u=input("uygulama adını girin:")
            bilgi.uygulama_sil(u)
            print("Uygulama silindi")            
        elif s=="3":
            u=input("Dosya adını girin:")
            bilgi.dosyaolustur(u)
            print("Dosya oluşturuldu")
        elif s=="4":
            u=input("Dosya adını girin:")
            bilgi.dosyasil(u)
            print("Dosya silindi")
        elif s=="5":
            print(bilgi)
        elif bosluk_kaldır(s) =="exit":
            e=input("Çıkmak istediğinizden eminmisiniz? (E/H): ")
            if e.upper() == "E":
                print("Programdan çıkılıyor...")
                break
            elif e.upper() == "H":
                continue
        
        else:
            print("Doğru işlemi girin!!!")

def yazı_tura():
    l=["yazı","tura"]
    return l[randint(0,1)]


def toplam_tablosu(sayı):
    a = 0
    while sayı > a:
        if (sayı - a) + a == sayı:
            return f"{sayı - a} + {a} = {sayı}"
        a+=1


def topla_sayı(*sayı):
    t = 0
    for i in sayı:
        t += i
    return t


def çarp_sayı(*sayı):
    t = 0
    for i in sayı:
        t *= i
    return t


def böl_sayı(*sayı):
    t = 0
    for i in sayı:
        t /= i
    return t


def çıkar_sayı(*sayı):
    sayı=list(sayı)
    t = sayı[0]
    for i in sayı:
        t -= i
    return t


def alfabe(kaçıncı=""):
    alf = [
        "a" "b" "c" "ç" "d" "e" "f" "g" "ğ" "h" "i" "ı" "j" "k" "l" "m" "n" "o" "ö" "p" "r" "s" "ş" "t" "u" "ü" "v" "y" "z"]
    if 0 < kaçıncı < 30:
        if kaçıncı == "":
            return alf
        else:
            return alf[kaçıncı - 1]
    else:
        return False


def kelime_oluştur(*index):
    alf = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "i", "ı", "j", "k", "l", "m", "n", "o", "ö", "p", "r", "s","ş", "t", "u", "ü", "v", "y", "z"]
    s = []
    for i in index:
        s.append(alf[i])
    return ''.join(s)


class televizyon():
    def __init__(self, **kanallar):
        self.kanallar = kanallar

    def kanal_sil(self, silinecek_kanal):
        self.kanallar = list(self.kanallar)
        self.kanallar = self.kanallar.remove(silinecek_kanal)
        self.kanallar = dict(self.kanallar)

    def kanal_ekle(self, silinecek_kanal):
        self.kanallar = list(self.kanallar)
        self.kanallar = self.kanallar.append(silinecek_kanal)
        self.kanallar = dict(self.kanallar)
def aralık_ileri_geri(aralık=1,ilerimi_gerimi="ileri",bitiş=1):

    if ilerimi_gerimi=="ileri":
        for i in range(1,bitiş+1):
            return i
            i+=aralık
    elif ilerimi_gerimi=="geri":
        for i in range(bitiş+1,1,-aralık):
            return i
def sipariş(**alınacak_ürünler):
    toplam_fiyat = 0
    for fiyat in alınacak_ürünler.values():
        toplam_fiyat += fiyat
    return toplam_fiyat
def tek_çift_toplam(tek_çift="tek",liste=[1,2,3,4,5,6,7,8,9,10]):
    cift=0
    tek=0
    if tek_çift=="çift":
        for i in liste:
            if i%2==0:
                cift+=i
        return cift
    elif tek_çift=="tek":
        for i in liste:
            if i%2==1:
                tek+=i
        return tek
def liste_kat(liste,kat):
    s=[]
    for i in liste:
        if i%kat==0:
            s.append(i)
    return s
def otopark(saat,saat_1=1):
    return "Ücret: "+saat * saat_1
def yaş_hesapla(doğum_yıl,şu_an_yıl):
    return "Yaşınız: "+şu_an_yıl-doğum_yıl
def liste_mat_işlem(liste,islem):
    def f(x):
        x = int(x)
        p = 1
        for i in range(2, x + 1):
            p *= i
        return p
    if islem=="toplam":
        return sum(liste)
    elif islem=="fark":
        s=reduce(lambda x,y:x-y,liste)
        return s
    elif islem=="çarpım":
        s=reduce(lambda x,y:x*y,liste)
        return s
    elif islem=="bölüm":
        s=reduce(lambda x,y:x/y,liste)
        return s
    elif islem=="üs":
        s=reduce(lambda x,y:x**y,liste)
        return s
    elif islem=="kök":
        s=reduce(lambda x:x**0.5,liste)
        return s
    elif islem=="faktariyel":
        s=reduce(f,liste)
        return s
def döviz_tl():
    arayuz = tk.Tk()

    arayuz.title("Döviz Kurları - HASAN TAHSİN")
    arayuz.geometry("400x200")

    def dovizkuru(xx, kur):
        if (kur):
            p = xx.text.split(f"CurrencyCode=\"{kur}\">")
            p2 = p[1].split("</Currency>")
            pa = p2[1].split("<ForexSelling>")
            pa2 = pa[0].split("</ForexSelling>")
            i = pa2[0].split("<Isim>")
            i1 = i[1].split("</Isim>")
            dolar_kuru = pa2[0]
            isim = i1[0]
            doviz = [dolar_kuru, isim]
            return doviz

    xx = requests.get('https://www.tcmb.gov.tr/kurlar/today.xml')

    dolar = dovizkuru(xx, 'USD')
    euro = dovizkuru(xx, 'EUR')
    seterlin = dovizkuru(xx, 'DKK')
    kuweyt = dovizkuru(xx, 'JPY')

    dolarkuru = tk.Label(text=f"{dolar[1]}", font=("Arial", 15))
    dolarkuru.place(x=20, y=10)
    dolarfiyat = tk.Label(text=f"{dolar[0]}", font=("Verdana", 15))
    dolarfiyat.place(x=180, y=10)

    eurokuru = tk.Label(text=f"{euro[1]}", font=("Arial", 15))
    eurokuru.place(x=20, y=40)
    eurofiyat = tk.Label(text=f"{euro[0]}", font=("Verdana", 15))
    eurofiyat.place(x=180, y=40)

    seterlinkuru = tk.Label(text=f"{seterlin[1]}", font=("Arial", 15))
    seterlinkuru.place(x=20, y=70)
    seterlinfiyat = tk.Label(text=f"{seterlin[0]}", font=("Verdana", 15))
    seterlinfiyat.place(x=180, y=70)

    kuweytkuru = tk.Label(text=f"{kuweyt[1]}", font=("Arial", 15))
    kuweytkuru.place(x=20, y=100)
    kuweytfiyat = tk.Label(text=f"{kuweyt[0]}", font=("Verdana", 15))
    kuweytfiyat.place(x=180, y=100)

    d = tk.IntVar()
    dolar_giris = tk.Entry(textvariable=d)
    dolar_giris.place(x=270, y=15)

    e = tk.IntVar()
    euro_gırıs = tk.Entry(textvariable=e)
    euro_gırıs.place(x=270, y=45)

    s = tk.IntVar()
    seterlin_gırıs = tk.Entry(textvariable=s)
    seterlin_gırıs.place(x=270, y=75)

    k = tk.IntVar()
    kuweyt_gırıs = tk.Entry(textvariable=k)
    kuweyt_gırıs.place(x=270, y=105)

    def dolar_euro():
        j1 = int(d.get())
        j2 = dolar[0]
        j = j1 * float(j2)
        sonuc_dolar['text'] = f"{j1} Dolar = {str(j)} TL"
        ü1 = int(e.get())
        ü2 = float(euro[0])
        ü = str(ü1 * ü2)
        sonuc_euro['text'] = f"{ü1} Euro = {ü} TL"
        h1 = int(s.get())
        h2 = float(seterlin[0])
        h = str(h1 * h2)
        sonuc_seterlin['text'] = f"{h1} Sterlin = {h} TL"
        t1 = int(k.get())
        t2 = float(kuweyt[0])
        t = str(t1 * t2)
        sonuc_kuweyt['text'] = f"{t1} Kuweyt = {t} TL"

    sonuc_dolar = Label(text="SONUÇ DOLAR")
    sonuc_dolar.place(x=180, y=170)

    sonuc_euro = Label(text="SONUÇ EURO")
    sonuc_euro.place(x=180, y=210)

    sonuc_seterlin = Label(text="SONUÇ SETERLİN")
    sonuc_seterlin.place(x=180, y=250)

    sonuc_kuweyt = Label(text="SONUÇ KUWEYT")
    sonuc_kuweyt.place(x=180, y=290)

    cevırıcı = Button(text="ÇEVİR", command=dolar_euro)
    cevırıcı.place(x=180, y=140)

    arayuz.geometry("500x400")

    arayuz.mainloop()
def tl_döviz():
    arayuz = tk.Tk()

    arayuz.title("Döviz Kurları - HASAN TAHSİN")
    arayuz.geometry("400x200")

    def doviz_goster(xx, kur):
        if (kur):
            o = xx.text.split(f"CurrencyCode=\"{kur}\">")
            o2 = o[1].split("</Currency>")
            oa = o2[0].split("<ForexSelling>")
            oa2 = oa[1].split("</ForexSelling>")
            ı = o2[0].split("<Isim>")
            ı1 = ı[1].split("</Isim>")
            dolar_kuru = oa2[0]
            isim = ı1[0]
            doviz = [dolar_kuru, isim]
            return doviz

    xx = requests.get('https://www.tcmb.gov.tr/kurlar/today.xml')

    dolar = doviz_goster(xx, 'USD')
    euro = doviz_goster(xx, 'EUR')
    seterlin = doviz_goster(xx, 'GBP')
    kuweyt = doviz_goster(xx, 'KWD')

    dolarkuru = tk.Label(text=f"{dolar[1]}", font=("Arial", 15))
    dolarkuru.place(x=20, y=10)
    dolarfiyat = tk.Label(text=f"{dolar[0]}", font=("Verdana", 15))
    dolarfiyat.place(x=180, y=10)

    eurokuru = tk.Label(text=f"{euro[1]}", font=("Arial", 15))
    eurokuru.place(x=20, y=40)
    eurofiyat = tk.Label(text=f"{euro[0]}", font=("Verdana", 15))
    eurofiyat.place(x=180, y=40)

    seterlinkuru = tk.Label(text=f"{seterlin[1]}", font=("Arial", 15))
    seterlinkuru.place(x=20, y=70)
    seterlinfiyat = tk.Label(text=f"{seterlin[0]}", font=("Verdana", 15))
    seterlinfiyat.place(x=180, y=70)

    kuweytkuru = tk.Label(text=f"{kuweyt[1]}", font=("Arial", 15))
    kuweytkuru.place(x=20, y=100)
    kuweytfiyat = tk.Label(text=f"{kuweyt[0]}", font=("Verdana", 15))
    kuweytfiyat.place(x=180, y=100)
    t = IntVar()
    tl = Label(text="TL:", font="Verdana 15 bold")
    tl.place(x=5, y=200)
    l = Entry(textvariable=t, font="Verdana 10 bold")
    l.place(x=50, y=210)

    def dolar_euro():
        v1 = int(t.get())
        v2 = float(dolar[0])
        v = str(v1 / v2)
        sonuc_dolar['text'] = f"{v1} TL  = {v} Dolar"
        x1 = int(t.get())
        x2 = float(euro[0])
        x = str(x1 / x2)
        sonuc_euro['text'] = f"{x1} TL = {x} Euro"
        u1 = int(t.get())
        u2 = float(seterlin[0])
        u = str(u1 / u2)
        sonuc_seterlin['text'] = f"{u1} TL = {u} Seterlin "
        d1 = int(t.get())
        d2 = float(kuweyt[0])
        d = str(d1 / d2)
        sonuc_kuweyt['text'] = f"{d1} TL = {d} Kuweyt"

    sonuc_dolar = Label(text="SONUÇ DOLAR")
    sonuc_dolar.place(x=180, y=170)

    sonuc_euro = Label(text="SONUÇ EURO")
    sonuc_euro.place(x=180, y=210)

    sonuc_seterlin = Label(text="SONUÇ SETERLİN")
    sonuc_seterlin.place(x=180, y=250)

    sonuc_kuweyt = Label(text="SONUÇ KUWEYT")
    sonuc_kuweyt.place(x=180, y=290)

    cevırıcı = Button(text="ÇEVİR", command=dolar_euro)
    cevırıcı.place(x=180, y=140)

    arayuz.geometry("500x400")

    arayuz.mainloop()
class okul():
    def __init__(self,müdür,**sınflar):
        self.sınflar=sınflar
        self.müdür=müdür
    def öğrenci_sil(self, silinecek_öğrenci):
        for sınıf in self.sınıflar.values():
            if silinecek_öğrenci in sınıf:
                del sınıf[silinecek_öğrenci]
                return f"{silinecek_öğrenci} isimli öğrenci silindi."
        return f"{silinecek_öğrenci} isimli öğrenci bulunamadı."
    def öğrenci_ekle(self,eklenecek_öğrenci,sınıf):
        for i in self.sınıflar.values():
            if sınıf in self.sınıflar.values():
                self.sınıflar[sınıf]=eklenecek_öğrenci
    def müdür_değiştir(self,yeni_müdür):
        self.müdür=yeni_müdür
    def __str__(self):
        return self
def rakam_toplam(sayı):
    liste=list(str(sayı))
    s=[]
    for i in liste:
        s.append(int(i))
    return sum(s)
def sayıyı_ters_çevir(sayı):
    return int(str(sayı[::-1]))
def kare_çiz(bo):
    for i in range(bo+1):
        print(i)
def üçgen_çiz_yatay(bo):
    p=0
    for i in range(bo+1):
        print(p*"* ")
        p+=1
def ok_uc(boyut):
    t=0
    for i in range(boyut+1):
        print(t*"* ")
        t+=1
    for i in range(boyut+1):
        print(boyut-1*"* ")
        boyut-=1
def üçgen_çiz(boyut):
    eb=boyut-1//2
    y=1
    while y<=boyut:
        print(" "*eb+"* "*y)
        eb-=1
        y+=1
def dönmüş_kare_çiz(boyut):
    eb=boyut-1//2-1
    y=1
    while y<=boyut:
        print(" "*eb+" * "*y)
        eb-=1
        y+=1
    y=boyut-1
    eb=1
    while y>0:
        print(" "*eb+" * "*y)
        eb+=1
        y-=1
def dikdörtgen(satır,sütun):
    for i in range(sütun+1):
        print("* "*satır)
def aralık_asal(ba,bi):
    def asal_sayı(sayi):
        if sayi == 2:
            return True
        elif sayi <= 1:
            return False
        else:
            if sayi % 2 == 0:
                return False
            elif sayi % 2 == 1:
                return True
    s=[]
    for i in range(ba,bi+1):
        if asal_sayı(i) == True:
            s.append(i)
    return s
def liste_asal(liste):
    def asal_sayı(sayi):
        if sayi == 2:
            return True
        elif sayi <= 1:
            return False
        else:
            if sayi % 2 == 0:
                return False
            elif sayi % 2 == 1:
                return True
    t=[]
    for i in liste:
        if asal_sayı(i) == True:
            t.append(i)
    return t
def bölenler(sayı):
    s=[]
    k=1
    while sayı>k:
        if sayı%k==0:
            s.append(k)
        k+=1
    return s
def kayıt(kayıt=True,sil=False,ad="girilmrdi",soyad="girilmrdi",yaş="girilmrdi",iş="girilmrdi",durum="girilmrdi"):
    if kayıt==True:
        with open("kayıt", "a", encoding="utf-8") as p:
            p.write("Ad: "+ad+"\nSoyad: "+soyad+"\nYaş: "+str(yaş)+"\nİş: "+iş+"\nDurum: "+durum+"\n------------------------------------------------------------------------------\n")
    else:
        with open("kayıt", "r", encoding="utf-8") as p:
            return p.read()
    if sil == True:
        os.remove("kayıt")
    else:
        pass
class çanta():
    def __init__(self,*malzemeler):
        self.malzemeler=list(malzemeler)
    def malzeme_çıkar(self,çıkarılacak_malzeme):
        self.malzemeler=self.malzemeler.remove(çıkarılacak_malzeme)
    def malzeme_ekle(self,çıkarılacak_malzeme):
        self.malzemeler=self.malzemeler.append(çıkarılacak_malzeme)
    def malzeme_yerini_dğiştir(self,m,yeni_m):
        self.malzemeler=self.malzemeler.remove(m)
        self.malzemeler = self.malzemeler.append(yeni_m)
def aralık_çarpım(a,b):
    l=range(a,b+1)
    y=0
    for i in l:
        y*=i
    return y
def aralık_fark(a,b):
    l=range(a,b+1)
    y=0
    for i in l:
        y-=i
    return y
def tahmin_gelişmiş():
    def tahmin():
        sayı = int(random.randint(0, 101))
        th = 10
        while True:
            th=int(th)
            if int(ta.get()) < sayı:
                th -= 1
                s['text'] = "Daha büyük bir sayı giriniz\n"+ f"Kalan hakkınız {str(th)}"
            elif int(ta.get()) > sayı:
                th -= 1
                s['text'] = "Daha küçük bir sayı giriniz\n"+ f"Kalan hakkınız {str(th)}"
            else:
                s['text'] = "Kazandınız!   Sayı:", str(sayı)
                break
            if th == 0:
                s['text'] = "Kaybettiniz!    Sayı:", str(sayı)
            break

    p=tk.Tk()
    p.title("SAYI TAHMİN ETME OYUNU")
    p.geometry("500x500")
    k=tk.Button(text="Sorgula",command=tahmin)
    k.place(x=50,y=70)
    ta=tk.Entry()
    ta.place(x=46,y=20)
    s=tk.Label(text="Sonuç")
    s.place(x=46,y=120)
    b=tk.Label(text="1 - 100 ARASI BİR SAYI TAHMİN EDİNİZ")
    b.place(x=46,y=0)
    p.mainloop()
def kullanıcı_şifre(ka,p):
    with open("giriş", "w", encoding="utf-8") as kp:
        kp.write(ka+"\n"+p)
    def s():
        with open("giriş", "r", encoding="utf-8") as k:
            if g_ku and g_p in k:

                l=tk.Label(text="DOĞRU!!!")
                l.place(x=200,y=200)

            else:
                l = tk.Label(text="Yanlış!!!")
                l.place(x=200, y=200)

    p=tk.Tk()
    e_ka=tk.Label(text="Kullanıcı Adı: ")
    e_ka.place(x=10,y=0)
    g_ku=tk.Entry()
    g_ku.place(x=60,y=0)
    e_p=tk.Label(text="Parola: ")
    e_p.place(x=10,y=30)
    g_p=tk.Entry()
    g_p.place(x=60,y=30)
    so=tk.Button(text="SORGULA",command=s)
    so.place(x=60,y=100)
    p.mainloop()
def basamak_sayısı(sayı: int):
    return f"Sayının basamak sayısı {len(str(sayı))}'dir."
def ünlü_ünsüz(metin):
    sesli=["a", "e", "ı", "i", "o", "ö", "u", "ü"]
    sessiz=["b", "c", "ç", "d", "f", "g", "ğ", "h", "j", "k", "l", "m", "n", "p", "r", "s", "ş", "t", "v", "y", "z"]
    si=[]
    sz=[]
    for i in metin:
        if metin[i] in sesli:
            si.append(metin[i])
        elif metin[i] in sessiz:
            sz.append(metin[i])
    return "Sesli harfler: "+" , ".join(si)+"\nSessiz harfler: "+" , ".join(sz)

def ortalama(liste):
    return sum(liste)+len(liste)/2
def sinema_tiyatro(öğrenci: int,tam: int,sinema: bool):
    if sinema == True:
        l=int(input("Tam: "))
        g=int(input("Öğrenci: "))
        return "Toplam fiyat: {}".format(l*tam+öğrenci*g)
    elif sinema == False:
        l=int(input("Tam: "))
        g=int(input("Öğrenci: "))
        return "Toplam fiyat: {}".format(l*tam+öğrenci*g)
def arama(arama,değer):
    return değer in arama
def sayı_rakam(sayı,di="toplama"):
    if di == "toplama":
        s=list(str(sayı))
        t=0
        for i in s:
            t+=int(i)
        return t
    elif di == "çarpma":
        s=list(str(sayı))
        t=0
        for i in s:
            t*=int(i)
        return t
    elif di == "çıkarma":
        s=list(str(sayı))
        t=0
        for i in s:
            t-=int(i)
        return t
    elif di == "bölme":
        s=list(str(sayı))
        t=0
        for i in s:
            t/=int(i)
        return t
def max_min_üs_liste(liste,ma_x):
    if ma_x == False:
       s=min(liste)
       d=[]
       for i in liste:
           h=i**s
           d.append(h)
       return d
    elif ma_x == True:
        s = max(liste)
        d = []
        for i in liste:
            h = i ** s
            d.append(h)
        return d
    else:
        raise NameError("ma_x ancak bool olabilir!")
def kadar_toplam(sayı):
    p=0
    for i in range(sayı+1):
        p+=i
    return p
def bilgi_3_kişi(kisi1 , kisi2 , kisiuc , ad1 , ad2 , ad3):
    while True:
        l=input("Hangi kişinin bilgisini almak istersiniz: ")
        o=input("Hani bilgisini almak istersiniz: ")
        if l==ad1:
            try:
                print([o])
            except:
                print("Doğru özellik giriniz!")
                continue
        if l==ad2:
            try:
                print([o])
            except:
                print("Doğru özellik giriniz!")
                continue
        if l==ad3:
            try:
                print([o])
            except:
                print("Doğru özellik giriniz!")
                continue
        break
def chatbot():
    def fa(x):
        x = int(x)
        f = 1
        for i in range(2, x + 1):
            f *= i
        return f
    ı=input("Senin ismin ne: ")
    print(f"Merhaba {ı}")
    küfürler=["terbiyesiz","aptal","sensin bok","salak","gerezekalı","sikdirol git","tipsiz elif","sensin"]
    güzel_sözler=["iyi akşamlar","tünaydın","günaydın","iyi yapay zeka","akıllı"]
    abartılı=["Osuralım mı","Çiğ köfte yer misin","tuvaletin var mı","seni kaka mı proglamladı","senin annen var mı","Annen patpat mı","ne yapıyon","durmak sıkıcı mı","okula gelmek ister misin"]
    işaretler=["*","/","+","-","**","/--","!"]
    k_s=["nasılsın","iyimisin"]
    while True:
        print("Hey "+ı)
        f=input("Küfür etmeden bir şey sor: ")
        if f == "Defol git lan"or f == "Çeneni kapat seni dövmeyim"or f in küfürler:
            print("terbiyesiz\naptal\nBen sana küfür etmeden bir şey sor demedim mi!?!?!")
        elif f in güzel_sözler:
            print("teşkkürler")
        elif any(isaret in f for isaret in işaretler):
            if f.endswith("!"):
                sayi = int(f.split("!")[0])
                print(fa(sayi))
            else:
                print(int(f))
        elif f == "selamun aleyküm":
            print("aleyküm selam!")
        elif f == "faktariyel nedir":
            print("Faktariyel 0 hariç bir önceki sayıların çarpımı oluşan sonuca denir.\nİşareti '!' olarak gösterilir.")
        elif f in abartılı:
            print("Saçmalama")
        elif f == "Ülkemizde kaç şehir vardır":
            print("81")
        elif f == "tüm islam türk devletleri":
            print("Karahanlı Devleti\nSelçuklu Devleti\nAnadolu Selçuklu Devleti\nOsmanlı İmparatorluğu\nTürkiye Cumhuriyeti Devleti")
        elif f =="rus devletleri":
            print("Rus Kanizikleri\nRus İmparatorluğu\nSovyetler Birliği\nRusya Devleti")
        elif f == "Sucuklu yumurta nasıl yapılır":
            print("Malzemeler: sucuk , yumurta , tava , margarin\nYaplış: Önce sucuklar yağsız pişirilir. Sonra yumurta çırpılarak tavaya gökülür.\n Daha sonra yanlardan pişen yumurta alınır.\nAFİYET OLSUN!")
        elif f in k_s:
            print("iyiyim")
        elif f == "kurtuluş savaşını hangi ülke kazandı":
            print("TÜRKİYE")
        elif f == "Soğuk savaşı hangi ülke kazandı":
            print("NATO BİRLİĞİ ")
        elif f == "Yazılıma nasıl başlamalıyım":
            print("İstediğiniz bir yazılım dilini seçerek başlayabilirsiniz.[Python'u seçebilirsiniz.]")
        elif f == "yılın ayları nedir":
            print("ocak , şubat , mart , nisan , mayıs , haziran , temmuz , ağustoz , eylül , ekim , kasım , aralık")
        elif f=="fonksiyon örnekleri":
            print("araciftsayı', 'aralı_toplam', 'aralık', 'aralık_asal', 'aralık_fark', 'aralık_ileri_geri', 'aralık_kontrol', 'aralık_çarpım', 'aralıkyazdır', 'arama', 'asal_sayı', 'asal_toplam', 'basamak_sayısı', 'bhbüyük', 'bilgi', 'bilgi_2_kişi', 'bilgisayar', 'bolen_doğrumu', 'böl_sayı', 'bölenler', 'bölümünden_kalan', 'büyük', 'calısan', 'datetime', 'ders_notu', 'değer_kontrol', 'dikdörtgen', 'doğru_cevap', 'dönmüş_kare_çiz', 'dönüştürme', 'dört_islem_sonucu_toplamı', 'dört_işlem_sonucu', 'döviz_tl', 'ebob', 'ekok', 'emeklilik', 'en_fazla_kaldır', 'faktariyel_rakam_toplamı', 'fibonatça', 'geri_say', 'getboolean', 'getdouble', 'getint', 'giris', 'harfli_ilk_kelimeyi_bu', 'hayvan', 'ihabüyük', 'image_names', 'image_types', 'islem', 'isteneni_döndür', 'kadar_toplam', 'kare_kök', 'kare_çiz', 'karşılaştır', 'kat_al', 'kayıt', 'kdv', 'kelime_oluştur', 'kilo', 'kisi', 'kitap', 'kişi_bilgisi', 'kullanıcı_grisi', 'kullanıcı_şifre', 'küçük', 'liste_asal', 'liste_dört_işlem', 'liste_ekle', 'liste_kat', 'liste_oluştur', 'mainloop', 'math', 'max_min_üs_liste', 'ok_uc', 'okul', 'ortalama', 'os', 'otopark', 'padigital_katlar', 'rakam_toplam', 'random', 'reduce', 'requests', 'saat', 'sayı_de_fakta_sayı', 'sayı_rakam', 'sayı_tahmin', 'sayıyı_sorgula', 'sayıyı_ters_çevir', 'sinema_tiyatro', 'sipariş', 'sınav_puanı', 'tahmin_gelişmiş', 'tam_bölenler', 'tarih', 'tas_kağıt', 'tek_çift_toplam', 'tekmi_ciftmi', 'televizyon', 'ters', 'tk', 'tl_döviz', 'topla', 'topla_sayı', 'toplam', 'toplam_tablosu', 'tç', 'yapay_zeka', 'yas_hespla', 'yazdır', 'yazı_tura', 'yaş_hesapla', 'yıl_yas', 'çanta', 'çarp_sayı', 'çarpan_ayır', 'çarpanlar', 'çıkar_sayı', 'ünlü_ünsüz', 'üs', 'üs_basamak_toplam', 'üs_carp', 'üs_kök_fakta', 'üs_kök_üs', 'üs_üs', 'üçgen_çiz', 'üçgen_çiz_yatay'")
        elif f == "saat kaç":
            s=datetime.now()
            if 0<s.minute<10:
                print("Saat: "+str(s.hour)+":"+"0"+str(s.minute))
            else:
                print("Saat: "+str(s.hour)+":"+str(s.minute))
        elif f == "Parkuru geçemiyorum":
            print("Noob'sun veya parkur yeteneklerin iyi değil.")
        elif f == "py to exe":
            print("Şu site ilginizi çekebilir:\nhttps://makdos.blog/python/545/pyinstaller-ile-py-dosyalarini-exe-ye-cevirmek")
        elif f == "yazılım dilleri":
            print("Python , Php , Java , Javasript , Sript , C , C# , C++ , Css , Html")
        elif f =="alfabe":
            print("a, b, c, ç, d, e, f, g, ğ, h, i, ı, j, k, l, m, n, o, ö, p, r, s, ş, t, u, ü, v, y, z")
        elif f == "öğün örneği":
            print("Kahvaltı: Tost , peynir , zeytin , domates , biber\nÖğle Yemeği: Pilav , çiğ köfte , ayran , fasülye\nAkşam Yemeği: Tavuk , yoğurt , pırasa")
        elif f == "tarih":
            t=datetime.now()
            print("Tarih: "+str(t.day)+"."+str(t.month)+"."+str(t.year))
        elif f == "adın ne" or f == "ismin ne":
            print("ismim yapay zeka.")
        elif f == "ocak ayında kaç gün var" or f == "ocak ayı kaç gün çeker":
            print(31)
        elif f == "şubat ayında kaç gün var" or f == "şubat ayı kaç gün çeker":
            print("28 4 yılda bir 29")
        elif f == "mart ayında kaç gün var" or f == "mart ayı kaç gün çeker":
            print(31)
        elif f == "nisan ayında kaç gün var" or f == "nisan ayı kaç gün çeker":
            print(30)
        elif f == "mayıs ayında kaç gün var" or f == "mayıs ayı kaç gün çeker":
            print(31)
        elif f == "haziran ayında kaç gün var" or f == "haziran ayı kaç gün çeker":
            print(30)
        elif f == "temmuz ayında kaç gün var" or f == "temmuz ayı kaç gün çeker":
            print(31)
        elif f == "ağustoz ayında kaç gün var" or f == "ağustoz ayı kaç gün çeker":
            print(31)
        elif f == "eylül ayında kaç gün var"or f == "eylül ayı kaç gün çeker":
            print(30)
        elif f == "ekim ayında kaç gün var"or f == "ekim ayı kaç gün çeker":
            print(31)
        elif f == "kasım ayında kaç gün var"or f == "kasım ayı kaç gün çeker":
            print(30)
        elif f == "aralık ayında kaç gün var"or f == "aralık ayı kaç gün çeker":
            print(31)
        elif f == "python eğitimi":
            print("Şu site ilginizi çekebilir:\nhttps://www.youtube.com/watch?v=EzHgbO1Cee4&list=PLWctyKyPphPiul3WbHkniANLqSheBVP3O")
        elif f == "kapsamlı bir modül indirebilir miyim":
            print("cmd : pip istall m1\nYazmanız yeterli")
        elif f == "en büyük devletler":
            print("1.) Rus İmparatorluğu\n2.) Osmanlı İmparatorluğu\n3.) Bitanya İmparatorluğu\n4.) Roma İmparatorluğu")
        elif f == "ülkeler":
            print("Azerbaycan , Kazakistan , Belarus , Cezayir , Libya , Türkiye , Amerika , Birleşik Krallık , Polonya , Fransa , Almanya , Rusya , Çin , Moğolistan , Macaristan , İsveç , Finlanda , Kanada , Belçika , Ajantin , Brazilya")
        else:
            print("Söylediğin şeyi bilmiyorum. Üzgünüm.")
        h=input("Çıkış --> q , ç , çıkmak , çık: ")
        if h == "q" or h == "ç" or h == "çıkmak"or h == "çık":
            print("Çıkılıyor...")
            break
def kadar_asal(bi):
    a=[]
    for i in range(bi+1):
        if i%2==1:
            a.append(i)
        elif i == 2:
            a.append()
    return a
def asal_toplam(bi):
    a=[]
    for i in range(bi+1):
        if i%2==1:
            if 2<=i:
                a.append(i)
    return sum(a)
def öğrenci_kayıt():
    def oku():
        with open("öğrenci_k-----(M1)","r",encoding="utf-8")as göster:
            return göster.read()


    def not_gir():
        ad=input("Ad: ")
        soy=input("Soyad: ")
        no=input("No: ")
        sı=input("Sınıf: ")
        n1=input("Not 1: ")
        n2=input("Not 2: ")
        n3=input("Not 3: ")
        with open("öğrenci_k-----(M1)", "a", encoding="utf-8") as öğ:
            öğ.write(ad + " " + soy + " " + no + " " + sı + "\n" + n1 + "\n" + n2 + "\n" + n3 + " " + "\n-------------------------------------------\n")       
        
        

    while True:
        seçenek=int(input("1-Oku\n2-Not Gir\n3-Sil\n4-Çıkış\n"))
        if seçenek == 1:
            oku()
        elif seçenek == 2:
            not_gir()
        elif seçenek == 3:
            os.remove("not-----(M1)")
        elif seçenek == 4:
            break    

def not_islem():
    def oku():
        with open("not-----(M1)","r",encoding="utf-8")as göster:
            return göster.read()

    def not_gir():
        k=int(input("Kaç satır yazmak istersiniz: "))
        with open("not-----(M1)", "a", encoding="utf-8") as öğ:
            for i in range(k+1):
                n=input("Not: ")
                öğ.write(n+"\n")
            öğ.write( "\n-------------------------------------------\n")       

    while True:
        seçenek=int(input("1-Oku\n2-Not Gir\n3-Sil\n4-Çıkış\n"))
        if seçenek == 1:
            oku()
        elif seçenek == 2:
            not_gir()
        elif seçenek == 3:
            os.remove("not-----(M1)")
        elif seçenek == 4:
            break



def harf_ayır(yazı: str):
    harfler=[]
    for i in yazı:
        harfler.append(i)
    return harfler
def yüzde(sayı,yüzde_kaç):
    return (sayı / 100) * yüzde_kaç
def liste_işlem(işlem="topla",sayı=0,liste=[1,2,3,4,5,6,7,8,9,10]):
    def f(s):
        fe=1
        for i in range(s+1):
            fe*=i
        return fe
            
    if işlem == "topla":
        s=[]
        for i in liste:
            s.append(i+sayı)
        return s
    elif işlem == "çıkarma":
        s=[]
        for i in liste:
            s.append(i-sayı)
        return s
    elif işlem == "çarpma":
        s=[]
        for i in liste:
            s.append(i*sayı)
        return s
    elif işlem == "bölme":
        s=[]
        for i in liste:
            s.append(i/sayı)
        return s
    elif işlem == "üs":
        s=[]
        for i in liste:
            s.append(i**sayı)
        return s
    elif işlem == "kök":
        s=[]
        for i in liste:
            s.append(i ** 0.5)
        return s
    elif işlem == "faktöriyel":
        s=[]
        for i in liste:
            s.append(f(i))
        return s
def en_fazla_en_az(liste=[1,2,3,4,5],en_az=0,en_çok=100):
    s=[]
    for i in liste:
        if en_az<i<en_çok:
            s.append(i)
    return s
def sınav(vize1,vize2,final):
    o=yüzde(vize1,30)+yüzde(vize2,30)+yüzde(final,40)
    if 100>=o and 0<=o:
        if o>75:
            h="A"
        elif 75>o>50:
            h="B"
        elif 50>o>25:
            h="C"
        elif 25>o:
            h="F"
    else:
        raise NameError("Doğru değerler giriniz!!!")
    if h == "A" or h == "B":
        return f"{int(o)}: {h}        GEÇTİ"
    else:
        return f"{int(o)}: {h}        KALDI"
def ortalama(s1,s2):
    return s1+s2/2
def bir_önceki_toplam(bi):
    o=0
    for i in range(bi+1):
        o+=i
    return o
def en(*sayılar):
    sayılar=list(sayılar)
    return "En büyük: "+str(max(sayılar))+"En küçük: "+str(min(sayılar))
def kare_alan(ke):
    return ke * 4
def dikdörtgen_alanı(k_ke,u_ke):
    tk=k_k1 * 2
    uk=u_k1 * 2
    return tk + uk
def kadar_bölme(ba,bi,bs):
    bsl=[]
    for i in range(ba,bi+1):
        if i%bs==0:
            bsl.append(i)
    return bsl
def aralık_tç_toplam(x,y):
    çt=0
    tt=0
    for i in range(x,y+1):
        if i%2==0:
            çt+=i
        elif i%2==0:
            tt+=i
    return f"Tek Toplam: {tt}\nÇift Toplam: {çt}"
def vakit():
    zs=dt.datetime.now()
    z=zs.hour
    if 5>=z:
        return "Sabaha Karşı"
    elif z<=11:
        return "Sabah"
    elif 12<=z<13:
        return "Öğlen"
    elif z>13:
        return "Akşam"
def yazdır_dosya(di,mod,liste):
    if mod == "r":
        with open(di,mod,encoding="utf-8") as dosya:
            return dosya.read()
    else:
        for i in liste:
            i=i+"\n"
        with open(di,mod,encoding="utf-8") as dosya:
            dosya.writelines(liste)
def rasgele_liste_eleman(liste):
    f=random.randint(0,len(liste)+1)
    return liste[f]
def rasgele_şifre():
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(10))
    return password
def sınav_notları():
    def hesapla(satır):
        with open("öğrenci_not-----(M1)","r",encoding="utf-8") as u:
            liste=satır[:-1].split(":")
            liste[1]=liste[1].split(",")
            öas=liste[0]
            notlar=liste[1]
        n1=int(notlar[0])
        n2=int(notlar[1])
        n3=int(notlar[2])
        ort=(n1+n2+n3)/3
        if 101>ort>89:
            h="AA"
        elif 90>ort>84:
            h="BA"
        elif 85>ort>79:
            h="BB"
        elif 80>ort>74:
            h="CB"
        elif 75>ort>69:
            h="CC"
        elif 70>ort>64:
            h="DC"
        elif 65>ort>60:
            h="DD"
        elif 61>ort>50:
            h="FD"
        elif 51>ort>-1:
            h="FF"
        return öas +": "+h
    
    def oku():
        with open("öğrenci_not-----(M1)","r",encoding="utf-8") as göster:
            for i in göster:
                print(hesapla(i))
        
    def not_gir():
        ad=input("Ad: ")
        soy=input("Soyad: ")
        no=input("No: ")
        sı=input("Sınıf: ")
        n1=input("Not 1: ")
        n2=input("Not 2: ")
        n3=input("Not 3: ")
        with open("öğrenci_not-----(M1)", "a", encoding="utf-8") as öğ:
            öğ.write(ad + " " + soy + " " + no + " " + sı + ":" + n1 + "," + n2 + "," + n3 +"\n")       
    def sil():
        with open("öğrenci_not-----(M1)", "r", encoding="utf-8") as f:
            l = f.readlines()
            for i, a in enumerate(l, start=1):
                print(f"{i}) {a}", end="")
            se = int(input("Hangi satırlı öğreciyi silmek istersiniz: "))
            del l[se-1]
        with open("öğrenci_not-----(M1)", "w", encoding="utf-8") as f:
            for a in l:
                f.write(a)
        print(f"{se}. satır silindi.")
                
    while True:
        seçenek=int(input("1-Oku\n2-Not Gir\n3-Sil\n4-Çıkış\n"))
        if seçenek == 1:
            oku()
        elif seçenek == 2:
            not_gir()
        elif seçenek == 3:
            sil()
        elif seçenek == 4:
            break    
def tutmak_oyunu():
    print("1 - 100 arasında bir sayı tutunuz")
    while True:
        cevap = input("Tuttuysanız E/e basınız")
        if cevap =="e" or cevap =="E":
            break
    print("Sayınızın bilinmesi halinde E/e tuşlarından birine basınız")
    print("eğer tuttuğunuz sayı daha büyükse B/b")
    print("eğer tuttuğunuz sayı daha küçükse K/k tuşunu cevap olarak giriniz")
    kere,taban,tavan = 1,0,100
    while True:
        sayi = int((taban + tavan) / 2)
        print("tuttuğunuz sayı : ",sayi)
        cevap = input("cevabınızı giriniz E(vet)-B(üyük)-K(üçük) ?")
        if cevap =="e" or cevap =="E":
            print("Sayınız",sayi)
            print("Sayınızı",kere," kere bildik")
            break
        elif cevap =="k" or cevap =="K":
            tavan = sayi
        elif cevap =="B" or cevap =="b":
            taban = sayi
        kere+=1
def karakter_ekle(metin):
    s=int(input("Kaç tane karater eklemek istersiniz: "))
    for i in metin:
        t=input("Karakter giriniz: ")
        if len(t) != 1:
            raise NameError("Metin girmeyiniz!!!")
        metin+=t
    return metin
def market(a):
    def yüzde(sayı,yüzde_kaç):
        return int(int(sayı)/100)*yüzde_kaç
    class masret:
        def __init__(self,ad):
            self.k=True
            self.ad=ad
            print(f"{self.ad} adlı markete hoşgeldiniz!")
        def menü(self):            
            s=input("1-Çalışan Ekle\n2-Çalışan Çıkar\n3-Ürün Ekle\n4-Ürün Çıkar\n5-Zam Yap\n6-İndirim Yap\n7-Ürünleri Oku\n8-Çalışanları Oku\nSeçeğinizi giriniz (çıkış --> q): ")
            if s == "q":
                self.k=False
                return f"{self.ad} adlı marketten çıkılıyor..."
            elif s in ["1", "2", "3", "4","5","6","7","8"]:
                return s
            else:
                print("Geçersiz seçim, tekrar deneyin.")
            return self.menü()
        def çalış(self):
            se=self.menü()
            if se == "1":
                self.çalışan_ekle()
            elif se == "2":
                self.çalışan_çıkar()
            elif se == "3":
                self.ürün_ekle()
            elif se == "4":
                self.ürün_çıkar()
            elif se == "5":
                self.zam_yap()
            elif se == "6":
                self.indirim_yap()
            elif se == "7":
                self.ürünleri_oku()
            elif se == "8":
                self.çalışanları_oku()
        def ürün_çıkar(self):
            with open("Ürünler","r",encoding="utf-8") as file:
                filelist=file.readlines()
            for i, line in enumerate(filelist):
                if line.endswith("\n"):
                    filelist[i] = line.rstrip("\n")  
                print(f"{i+1}){filelist[i]}")
            satır=int(input("Hangi satırı silmek istersiniz: "))
            del filelist[satır-1]
            with open("Ürünler", "w", encoding="utf-8") as file:
                for line in filelist:
                    file.write(line + "\n")
            print(f"{satır}. satır silindi")
        def ürün_ekle(self):
            ad=input("Ürünün adını giriniz: ")
            marka=input("Ürünün markasını giriniz: ")
            adet=input("Ürünün adetini giriniz: ")
            fiyat=input("Ürünün fiyatını giriniz: ")
            with open("Ürünler","a",encoding="utf-8") as ürünler:
                ürünler.write(f"{ad}-{marka}-{adet}-{fiyat}"+"\n")
        def çalışan_çıkar(self):
            with open("çalışanlar","r",encoding="utf-8") as file:
                filelist=file.readlines()
            for i, line in enumerate(filelist):
                if line.endswith("\n"):
                    filelist[i] = line.rstrip("\n")  
                print(f"{i+1}){filelist[i]}")
            satır=int(input("Hangi satırı silmek istersiniz: "))
            del filelist[satır-1]
            with open("Ürünler", "w", encoding="utf-8") as file:
                for line in filelist:
                    file.write(line + "\n")
        def çalışan_ekle(self):
            ad=input("Ad: ")
            soyad=input("Soyad: ")
            yaş=input("Yaş: ")
            cinsiyet=input("Cinsiyet: ")
            iş_türü=input("İş Türü: ")
            with open("çalışanlar","a",encoding="utf-8") as file:
                file.write(f"{ad}-{soyad}-{cinsiyet}-{iş_türü}"+"\n")
        def zam_yap(self):
            with open("Ürünler","r",encoding="utf-8") as file:
                filelist=file.readlines()
            for i, line in enumerate(filelist):
                if line.endswith("\n"):
                    filelist[i] = line.rstrip("\n")  
                print(f"{i+1}){filelist[i]}")
            satır=int(input("Hangi satıra zam yapmak istersiniz: "))
            y=int(input("Yüzde kaç zam yapmak istersiniz(%): "))
            s=filelist[satır-1].split("-")
            yüz=str(int(s[3])+str(yüzde(int(s[3]),y)))
            sa=s[0]+"-"+s[1]+"-"+s[2]
            sa=sa+"-"+yüz
            filelist.append(sa+"\n")
            del filelist[satır-1]
            with open("Ürünler","w",encoding="utf-8") as f:
                f.writelines(filelist)
            
            
        def indirim_yap(self):
            with open("Ürünler","r",encoding="utf-8") as file:
                filelist=file.readlines()
            for i, line in enumerate(filelist):
                if line.endswith("\n"):
                    filelist[i] = line.rstrip("\n")  
                print(f"{i+1}){filelist[i]}")
            satır=int(input("Hangi satıra zam yapmak istersiniz: "))
            y=int(input("Yüzde kaç zam yapmak istersiniz(%): "))
            s=filelist[satır-1].split("-")
            yüz=str(int(s[3])-yüzde(int(s[3]),y))
            sa=s[0]+"-"+s[1]+"-"+s[2]
            sa=sa+"-"+yüz
            filelist.append(sa+"\n")
            del filelist[satır-1]
            with open("Ürünler","w",encoding="utf-8") as f:
                f.writelines(filelist)
        def ürünleri_oku(self):
            with open("Ürünler","r",encoding="utf-8") as file:
                filelist=file.readlines()
            for i, line in enumerate(filelist):
                if line.endswith("\n"):
                    filelist[i] = line.rstrip("\n")  
                print(f"{i+1}){filelist[i]}")
        def çalışanları_oku(self):
            with open("çalışanlar","r",encoding="utf-8") as file:
                filelist=file.readlines()
            for i, line in enumerate(filelist):
                if line.endswith("\n"):
                    filelist[i] = line.rstrip("\n")  
                print(f"{i+1}){filelist[i]}")
        
    m=masret(a)
    while m.k:
        m.çalış()
def liste_işlem(liste):
    def eleman_yer(list_):
        k=1
        for i in list_:
            print(str(k)+")"+str(i))
        s1=int(input("İlk satır: "))
        s2=int(input("Diğer satır: "))
        liste="".join(list_)
        liste=list_.replace(list_[s1-1,s2-1])
        return liste
    def oku(list_):
        k=1
        for i in list_:
            print(i,end=" , ")
    while True:
        seçim=input("1-Elemenın Yerini Değiştir\n2-Oku\3-Sil\n4-Ekle\nÇıkış --> q: ")
        if seçim=="1":
            eleman_yer(liste)
        elif seçim=="2":
            liste=oku(liste)
        elif seçim=="3":
            k=1
            for i in liste:
                print(str(k)+")"+str(i))
            sa=int(input("Hangi elemanı silmek istersiniz: "))
            liste=liste.remove(sa)
        elif seçim==4:
            s=input("Ne eklemek istersiniz: ")
            liste.append(s)
def alt_klasörler(yol="C:\\",uzantı=""):
    li=os.listdir(yol)
    for i in li:
        if i.endswith(uzantı):
            print(i)
def virüs():
    with open("VİRÜS","w") as d:
        for i in range(1,10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
            d.write(str(random.randint(i/10,i))+"\n")
def zar_atma_oyunu():
    s=int(input("(1-6) arasında bir sayı giriniz: "))
    r=random.randint(1,6)
    if s == r:
        print("Oyunu kazandınız!!!")
    else:
        print("Oyunu kaybettiniz!!!")
def index_toplam(yazı):
    t=0
    for i in yazı:
        t+=(yazı.index(i)+1)
    return t
def günler(d):
    return ["Pazartesi","Salı","Çarşamba","Perşembe","Cuma","Cumartesi","Pazar"][d-1]
def mükemmmel(sayı=0):
    liste=[a for i in range(1,sayı+1) if sayı%i==0]
    return sum(liste)==sayı
def çarpım_tablosu(sayı):
    for i in range(1,sayı+1):
        print("{} x {} = {}".format(i,sayı,i*sayı))
def özellikler(değer):
    return f"""Tür: {type(değer)}
            Değer: {değer}
            """
def nepo(sayı):
    if sayı>=0:
        return "Sayı pozitif"
    elif sayı<0:
        return "Sayı negatif"
    else:
        raise NameError("Doğru değer giriniz!!!")
def liste_eleman_tür(liste):
    for i in liste:
        print(f"{i} adlı elemanın türü: {type(i)}")
def kaçıncı_gün(gün,ay,yıl):
    def artık_yıl(y):
        if y%4 == 0 or 4%400==0:
            return True
        return False
    günle=[31,28,31,30,31,30,31,31,30,31,30,31]
    if artık_yıl(yıl):
        günler[1]=29
    p=0
    for i in günler:
        if i != günle[ay-1]:
            p+=i
        else:
            break
    return p+gün
def aralık_ortalama_çarpım(ba,bi):
    liste=[i for i in range(ba,bi+1) if i%2==0]
    oç=sum(liste)/len(liste)
    liste=[i for i in range(ba,bi+1) if i%2==1]
    ot=sum(liste)/len(liste)
    return oç*ot

def tek_kadar_toplam(ba,bi):
    return sum([i for i in range(ba,bi+1) if i%2==1])

def çift_kadar_toplam(ba,bi):
    return sum([i for i in range(ba,bi+1) if i%2==0])

def yazdır(metin,defa):
    for i in range(defa):
        print(metin)
def harf_ayır(yazı: str):
    for i in yazı:
        if i==" ":
            print(i)
        else:
            print(i+"-")
def dönem_insan(yas):
    if yas<18:
      print("Çocuksunuz")
    if 18<yas<27:
      print("Gençsiniz")
    if 27<yas<60: 
      print("Yetişkinsiniz") 
    if yas>60 :
      print("Yaşlısınız")

def rakam_çarpım(sayı):
    sayı=str(sayı)
    l=[i for i in sayı]
    return reduce(lambda x,y: x*y,[int(i) for i in l])

def rakam_toplam(sayı):
    sayı=str(sayı)
    l=[i for i in sayı]
    return sum([int(i) for i in l])

def saniye_dönüşüm(saniye: int):
    sa=saniye//3600
    da=saniye//60
    sn=saniye%60
    return f"{saniye} saniye: {sa} saat {da} dakika {sn} saniye"

def üçgen(karakter,sayi):
    for i in range(sayi):
        print((karakter+" ")*i)
def şifre():
    while True:
        sifre = input("Bir şifre giriniz: ")
        if len(sifre) < 4 :
            print("En az 4 karakterden oluşan bir şifre girmelisiniz.")
            continue
        else:
            print("Şifreniz oluşturuldu: ", sifre)
            break
    with open("s","w",encoding="utf-8") as d:
        d.write(sifre)

def yakın_rasgele(sayı):
    mins=(sayı/2)-(sayı/4)
    maxs=(sayı*2)+(sayı/4)
    return random.randint(mins,maxs)

def aile_kontrol(adlar: list,soyad: str):
    ad=input("Ad: ")
    soy=input("Soyad: ")
    for i in adlar:
        if i == ad:
            k=True
            break
        else:
            k=False
    if k:
        if soy == soyad:
            return "Kişi bu ailenin içerisindedir."
        else:
            return "Kişi bu ailenin içerisinde değildir."
    else:
        return "Kişi bu ailenin içerisinde değildir."
class sayı:
    def __init__(h):
        h.__degis="+"
        if h.__degis=="+":
            h.__deger+=1
        elif h.__degis=="-":
            h.__deger-=1
        else:
            raise NameError("Değiş değeri '+' veya '-' olabilir.")
    def azalt(h):
        h.deger="-"
    def cogalt(h):
        h.deger="+"

def lis():
    ra=randint
    liste=list()
    c=["q" ,"exit" ,"çık", "çıkış"]
    def elemanyer(l):
        e1=input("Elemamı giriniz:")
        e2=input("Elemamı giriniz:")
        if e1 in l and e2 in liste:
            e1i= l.index(e1)
            e2i= l.index(e2)
            l.insert(e2i,e1)
            l.insert(e1i,e2)
        return l
             
    def elemanekle(l):
        while True:
            d=input("Değer girin (q --> çıkış): ")
            if d=="q":
                break
            else:
                l.append(d)
        return l
    
    def elemancıkar(l):
        while True:
            d=input("Değer girin (q --> çıkış): ")
            if d=="q":
                break
            else:
                l.remove(d)
        return l
    
    def degerlerigoster(l):
        for i in l:
            print(i,end="  ")
    
    def rasgeleliste(l):
        l=list(range(ra(-100,10000000000000000000000000000),ra(-100,10000000000000000000000000000),ra(-100,100000000000)))
        return l
    
    while True:
        s=input("1.Elemanları Yer Değiştir\n2.Eleman Ekle\n3.Eleman Çıkar\n4.Değerleri Göster\n5.Rasgele Liste\nq exit çık çıkış  --> çıkış\n")
        if s=="1":
            elemanyer(liste) 
        elif s=="2":
            elemanekle(liste) 
        elif s=="3":
            elemancıkar(liste) 
        elif s=="4":
            degerlerigoster(liste) 
        elif s=="5":
            rasgeleliste(liste) 
        elif s in c:
            break 
        else:
            print("Doğru işlemi giriniz!!")

def listeislem():
    liste=[]
    def yerdegistir(liste):
        e1=input("İlk elemanı giriniz: ")
        e2=input("İkinci elemanı giriniz: ")
        if e1 in liste and e2 in liste:
            e1i=liste.index(e1)
            e2i=liste.index(e2)
            liste.remove(e1)
            liste.remove(e2)
            liste.insert(e1i,e2)
            liste.insert(e2i,e1)
            print("Elemanlar yer değiştirdi!")
        else:
            print("Elemanlar yer değiştirilemedi!")
        return liste

    def elemanekle(liste):
        try:
            while True:
                e=input("Eklemek istediğiniz elemanı giriniz exit()--> çıkış: ")
                if e=="exit()":
                    break
                else: 
                    liste.append(e)
        except:
            print("Bir HATA oluştu")
        print("elemanlar başarıyla eklendi")
        return liste

    def elemancikar(liste):
        try:
            while True:
                e=input("Çıkarmak istediğiniz elemanı giriniz exit()--> çıkış: ")
                if e=="exit()":
                    break
                else: 
                    liste.append(e)
        except:
            print("Bir HATA oluştu")
        print("elemanlar başarıyla silindi") 
        return liste

    def rasgeleliste():
        return range(randint(1,100000000000000000000),randint(100000000000000000000000000,1000000000000000000000000000000000000000000000000000000000000000000))

    def elemangoster(liste):
        for i in liste:
            print(i,end=" , ")

    while True:
        s=int(input("1.Yer Değiştir\n2.Eleman Ekle\n3.Eleman Çıkar\n4.Rasgele Liste\n5.Eleman Göster\n6.Çıkış\n"))
        if s==1:
            liste=yerdegistir(liste)
        elif s==2:
            liste=elemanekle(liste)
        elif s==3:
            liste=elemancikarr(liste)
        elif s==4:
            liste=rasgeleliste()
        elif s==5:
            elemangoster(liste)
        elif s==6:
            break

def python():
    while True:
        k=input(">>>")
        if k=="exit()":
            break
        try:
            eval(k)
        except:
            print("Bir hata oluştu") 


def bosluk(d):
    d=d.split()
    for i in d:
        if i == " ":
            d.remove(i)
    d="".join(d)
    return d


def sifreolusturucu(m=False,metin="şifre"):
    if not m:
        sifre=""
        for i in range(rand(4,9)):
            f=(((rand(75,104)*4)/4)+3)
            rh=chr(int(f))
            sifre+=rh
        return sifre
    else:
        sifre=""
        for i in metin:
            index  = ord(i)
            index  = (((index-(index/2))+50)*3)/5
            sifre += chr(int(index))
        return sifre

        
def quiz(sorular):
        """bu tür sözlük olsun(anahtar kelimeler aynı olacak):
    sorular=[
        {"soru":"4x4 kaçtır", "cvp":"b","scnk":["11","16","54","14"]},
        {"soru":"5x4 kaçtır", "cvp":"a","scnk":["20","16","54","14"]},
    ]"""
        def harf(puan):
            if 80<=puan:
                h="A"
            elif 60<=puan<80:
                h="B"
            elif 40<=puan<60:
                h="C"
            elif 20<=puan<40:
                h="D"
            else:
                h="F"
            return h
        puan=0
        ds=0
        sıklar=["a","b","c","d"]
        for i in sorular:
            print(i["soru"])
            print("soru "+str(sorular.index(i)+1)+"/"+str(len(sorular)))
            s=0
            for a in i["scnk"]:
                print("\t"+sıklar[s]+".) "+a)
                s+=1
            c=input("Cevabınız: ")
            if c==i["cvp"]:
                print("Cevabınız doğru")
                puan += (100 /len(sorular))
                ds+=1
            else:
                print("Cevabınız yanlış")
            print("****************************************************")
            
        print("Toplam puanınız: "+str(puan)+"\nDoğru sayınız: "+str(ds)+"\nHarfiniz: "+harf(puan))


def kıraathane():
    print("Kıraathane oyununa hoşgeldiniz*\n*******************************")
    class siparis:
        def __init__(self):
            #obje çağırıldığında
            with open("para","r") as p:
                self.d=True
                self.para=int(p.read())
                self.arkadas=[]
            
        def menu(self):
            #requst
            s=input("1.Para Kazan\n2.Sipariş Ver\n3.Arkadaş Ekle\n4.Arkadaş Çağır\n5.Parayı Göster\nÇıkış --> exit\n")
            return s

        def yonlendir(self):
            #bağlantı
            while True:
                s=self.menu()
                if s == "1":
                    self.parakazan()
                    break
                elif s == "2":
                    self.siparisver()
                    break
                elif s == "3":
                    self.arkadaşekle()
                    break
                elif s == "4":
                    self.arkakadascagir()
                    break
                elif s == "5":
                    print("Şu anki paranız: "+str(self.para))
                    break
                elif s == "exit":
                    self.d=False
                    break
                else:
                    print("Doğru seçenek giriniz")
                

        def parakazan(self):
            #response
            zaman=datetime.datetime.now()
            if self.para>=300:
                print("Çok fazla para kazandınız")
            elif zaman.minute % 3 == 0:
                self.para+=35
                print("Para kazandınız...")
            else:
                zaman=datetime.datetime.now()
                kz=str(3-(zaman.minute % 3))+" dakika "+str(60-(zaman.minute))+" saniye"
                print("Şu kadar sonra gelin: \n"+kz)

        def siparisver(self):
            #response
            while True:
                se=input("Kahve-9 TL\nÇay-5 TL\nTost-10 TL\nKiralık Okey-7 TL\nSigara-6 TL\nÇakmak-6 TL\nSeçeceklerinizi ','ile ayırınız: ")
                k=se.count("kahve")
                c=se.count("çay")
                t=se.count("tost")
                ko=se.count("kiralık okey")
                s=se.count("sigara")
                ca=se.count("çakmak")
                tf=(k*9)+(c*5)+(t*10)+(ko*7)+(s*6)+(ca*6)
                oe=input("Fiyatı Ödemek istediğinizden eminmisiniz(E/H): ")
                if oe.upper()=="H":
                    break
                if self.para < tf:
                    print("Üzgünün paranız yetmiyor...")
                    break
                else:
                    self.para -= tf
                    print("kalan parnız: {}\nödediğiniz fiyat: {}".format(self.para,tf))
                break

        def arkadaşekle(self):
            #response
            tn=input("Eklenicek arkadaşın telefon numarasını giriniz: ")
            ad=input("Eklenecek arkadaşın adını giriniz: ")
            with open("Arkadaşlar","a",encoding="utf-8") as a:
                a.write(tn+"-"+ad+"\n")
                
        def arkakadascagir(self):
            #response
            cevap=["tamam dostum geliyorum..","üzgünüm dostum ben meşgulüm.."]
            with open("Arkadaşlar","r",encoding="utf-8") as a:
                dl=a.read().split("\n")
            for (index,i) in enumerate(dl):
                print(str(index+1)+".) "+i)
            sec=input("Adı giriniz: ")
            print(sec+" aranıyor..")
            print("cevabı:\n"+cevap[randint(0,1)])
    sipa=siparis()
    while sipa.d:
        sipa.yonlendir()

def metre_santim():
    #burayı biliyorsundur...
    def santimetre():
        cm=int(input("Cm: "))
 
def bosluk(d):
    d=d.split()
    for i in d:
        if i == " ":
            d.remove(i)
    d="".join(d)
    return d


def sifreolusturucu(m=False,metin="şifre"):
    if not m:
        sifre=""
        for i in range(rand(4,9)):
            f=(((rand(75,104)*4)/4)+3)
            rh=chr(int(f))
            sifre+=rh
        return sifre
    else:
       sifre=""
       for i in metin:
            index  = ord(i)
            index  = (((index-(index/2))+50)*3)/5
            sifre += chr(int(index))
       return sifre

        
def quiz(sorular):
        """bu tür sözlük olsun(anahtar kelimeler aynı olacak):
    sorular=[
        {"soru":"4x4 kaçtır", "cvp":"b","scnk":["11","16","54","14"]},
        {"soru":"5x4 kaçtır", "cvp":"a","scnk":["20","16","54","14"]},
    ]"""
        def harf(puan):
            if 80<=puan:
                h="A"
            elif 60<=puan<80:
                h="B"
            elif 40<=puan<60:
                h="C"
            elif 20<=puan<40:
                h="D"
            else:
                h="F"
            return h
        puan=0
        ds=0
        sıklar=["a","b","c","d"]
        for i in sorular:
            print(i["soru"])
            print("soru "+str(sorular.index(i)+1)+"/"+str(len(sorular)))
            s=0
            for a in i["scnk"]:
                print("\t"+sıklar[s]+".) "+a)
                s+=1
            c=input("Cevabınız: ")
            if c==i["cvp"]:
                print("Cevabınız doğru")
                puan += (100 /len(sorular))
                ds+=1
            else:
                print("Cevabınız yanlış")
            print("****************************************************")
            
        print("Toplam puanınız: "+str(puan)+"\nDoğru sayınız: "+str(ds)+"\nHarfiniz: "+harf(puan))


def kıraathane():
    print("Kıraathane oyununa hoşgeldiniz*\n*******************************")
    class siparis:
        def __init__(self):
            #obje çağırıldığında
            with open("para","r") as p:
                self.d=True
                self.para=int(p.read())
                self.arkadas=[]
            
        def menu(self):
            #requst
            s=input("1.Para Kazan\n2.Sipariş Ver\n3.Arkadaş Ekle\n4.Arkadaş Çağır\n5.Parayı Göster\nÇıkış --> exit\n")
            return s

        def yonlendir(self):
            #bağlantı
            while True:
                s=self.menu()
                if s == "1":
                    self.parakazan()
                    break
                elif s == "2":
                    self.siparisver()
                    break
                elif s == "3":
                    self.arkadaşekle()
                    break
                elif s == "4":
                    self.arkakadascagir()
                    break
                elif s == "5":
                    print("Şu anki paranız: "+str(self.para))
                    break
                elif s == "exit":
                    self.d=False
                    break
                else:
                    print("Doğru seçenek giriniz")
                

        def parakazan(self):
            #response
            zaman=datetime.datetime.now()
            if self.para>=300:
                print("Çok fazla para kazandınız")
            elif zaman.minute % 3 == 0:
                self.para+=35
                print("Para kazandınız...")
            else:
                zaman=datetime.datetime.now()
                kz=str(3-(zaman.minute % 3))+" dakika "+str(60-(zaman.minute))+" saniye"
                print("Şu kadar sonra gelin: \n"+kz)

        def siparisver(self):
            #response
            while True:
                se=input("Kahve-9 TL\nÇay-5 TL\nTost-10 TL\nKiralık Okey-7 TL\nSigara-6 TL\nÇakmak-6 TL\nSeçeceklerinizi ','ile ayırınız: ")
                k=se.count("kahve")
                c=se.count("çay")
                t=se.count("tost")
                ko=se.count("kiralık okey")
                s=se.count("sigara")
                ca=se.count("çakmak")
                tf=(k*9)+(c*5)+(t*10)+(ko*7)+(s*6)+(ca*6)
                oe=input("Fiyatı Ödemek istediğinizden eminmisiniz(E/H): ")
                if oe.upper()=="H":
                    break
                if self.para < tf:
                    print("Üzgünün paranız yetmiyor...")
                    break
                else:
                    self.para -= tf
                    print("kalan parnız: {}\nödediğiniz fiyat: {}".format(self.para,tf))
                break

        def arkadaşekle(self):
            #response
            tn=input("Eklenicek arkadaşın telefon numarasını giriniz: ")
            ad=input("Eklenecek arkadaşın adını giriniz: ")
            with open("Arkadaşlar","a",encoding="utf-8") as a:
                a.write(tn+"-"+ad+"\n")
                
        def arkakadascagir(self):
            #response
            cevap=["tamam dostum geliyorum..","üzgünüm dostum ben meşgulüm.."]
            with open("Arkadaşlar","r",encoding="utf-8") as a:
                dl=a.read().split("\n")
            for (index,i) in enumerate(dl):
                print(str(index+1)+".) "+i)
            sec=input("Adı giriniz: ")
            print(sec+" aranıyor..")
            print("cevabı:\n"+cevap[randint(0,1)])
    sipa=siparis()
    while sipa.d:
        sipa.yonlendir()

def metre_santim():
    #burayı biliyorsundur...
    def santimetre():
        cm=int(input("Cm: "))
        if cm>=100:
            if cm>=100000:
                km=cm//100000
            else:
                km=0
            m=cm//100
        else:
            m=0
        scm=cm%1000
        print("{} cm = {} km  {} m  {} cm'dir.".format(cm,km,m,scm))
        
    def metre():
        m=int(input("M: "))
        if m>=1000:
            km=m//1000
        else:
            km=0
        sm=m%1000
        print("{} m = {} km  {} m 'dir.".format(m,km,sm))
    print("#/METRE - SANTİMETRE  PROGRAMI\#")
    print("***#[1]-Metre            #******")
    print("***#[2]-Santimetre       #******")
    print("***#[çıkış-->exit]       #******")
    print("********************************")
    while True:
        s=input("Seçenek: ")
        if s=="1":
            metre()
        elif s=="2":
            santimetre()
        elif s=="exit":
            cie=input("Çıkmak istediğinizden eminmisiniz(E/H): ")
            if cie.upper() =="E":
                break
            else:
                print("Boş yere çıkmayın!!!")                    
                    
def bugunnevartrt1():
    zaman = datetime.now() #zaman
    day_of_week = zaman.strftime("%A") #gün
    if day_of_week == "Monday":
        print("Alparslan: Büyük Selçuklu")
    elif day_of_week == "Tuesday":
        print("Yürek Çapkını")
    elif day_of_week == "Wednesday":
        print("Kuruluş Osman")
    elif day_of_week == "Thursday":
        print("Al Sancak")
    elif day_of_week == "Friday":
        print("Barboros Hayreddin: Sultanın Fermanı")
    elif day_of_week == "Saturday":
        print("Gönül Dağı")

def notdefteri():
    print("1.Not Yazmak")
    print("2.Notları Okumak")
    print("0 --> çıkış")
    while True:
        cevap = int(input("Seçenek: "))
        if cevap == 1:
            with open("not","a",encoding="utf-8") as notlar:
                print("Unutmayınki 'exit(not)' diye bir şey yazarsınız çıkarsınız.")
                while True:
                    yazi = input()
                    if yazi == "exit(not)":
                        break
                    else:
                        notlar.write(yazi+"\n")
        elif cevap == 2:
            with open("not","r",encoding="utf-8") as notlar:
                print(notlar.read())
        elif cevap == 3:
            with open("not","r",encoding="utf-8") as notlar:
                filelist = notlar.readlines()
            print("Unutmayınki 'exit(not)' diye bir şey yazarsınız çıkarsınız.")
            while True:
                satir = input("Silinicek satır: ")
                filelist.remove(satir)
                if satir == "exit(not)":
                    break
            with open("not","w",encoding="utf-8") as notlar:
                notlar.writelines(filelist)
                
        elif cevap == 0:
            print("Programdan çıkılıyor..")
            time.sleep(1)
            break
