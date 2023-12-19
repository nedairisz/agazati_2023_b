"""
A huzott.txt forrásállomány, hatos lottó hűzások adatait tartalmazza, a feladatok megoldása során ezeket az adatokat használja!
A huzasok.txt állomány szerkezete:
·         Húzás: pl: 1
·         Év: pl.: 1944
·         Hét: pl.: 11
·         Szám: pl.: 10
Az állomány első sora a mezőneveket tartalmazza kukac jellel elválasztva.

III/A, B:
        A húzások száma: 9612
III/C:
        A 43. héten húzott számok átlaga: 23,02
III/D:
        Az első legnagyobb kihúzott szám értéke: 45, 1990-ben, a 43. héten húzták ki, ez volt a 120. húzás.        

⦁	Olvassa be osztály segítségével (utóbbit hozza létre külön modulban) a huzott.txt fájlból a játékosok adatait, és tárolja el 
    összetett adatszerkezetben, ami elősegíti a további feladatok könnyű megoldását! Ügyeljen arra, hogy az állomány első sora 
    az adatok fejlécét tartalmazza! (7p)
⦁	Írassa ki a húzások számát a mintának megfelelően a konzolra! (2p)
⦁	Határozza meg és írassa ki a konzolra a minta szerint, hogy a 42 héten (huzasid) húzott számoknak mennyi az átlaga, 
    két tizedesjegyre kerekítve. (4p)
⦁	Írassa ki konzolra a mintának megfelelően a legnagyobb kihúzott szám adatait (ha több is van, akkor az első legnagyobb adatait).(4p)

"""
from Huzasok import Huzas

def beolvasas():
    fajl = open("csomag.txt", "r", encoding='UTF-8')
    fajl.readline()
    sorok=fajl.readlines() #ez egy strig lista
    fajl.close()

for i in range(0,len(sorok),1):
        sor= sorok[i]
        sor_lista = sor.strip().split(",") #az elválasztójel mentén szétválasztaja a sorokat
        huzas=int(sor_lista[0])
        ev=int(sor_lista[1])
        het=int(sor_lista[2])
        szam=int(sor_lista[3])
        huzas=Huzas(huzas, ev, het, szam)
        huzasok_lista.append(huzas)