"""
minta
II/A, B, C:
    20;28;124;166;15;188;174;243
II/D, E:
    Tízzel osztható számok száma: 1.  	
    kimutatas.txt tartalma:
II/F:
    Tízzel osztható számok száma: 1. 

⦁	Írasson ki a konzolra pontosvessző jelel (;) elválasztva 8 számból álló véletlen számsorozatot [-100,859] zárt intervallumon 
    a mintának megfelelően! (4p)
⦁	A generált értékeket tárolja lista adatszerkezetben! (1p)
⦁	A ; jel csak az értékek között szerepeljen (a végén, elején ne)! (2p)
⦁	Írjon függvényt tizzel_osztahatoak_szama néven, amiben számolja meg, hogy hány olyan elem van, ami tízzel osztható. 
    A visszatérési érték legyen egy egész szám! (3p)
⦁	A tizzel_osztahatoak_szama függvény eredményét írassa ki a mintának megfelelően a konzolra, amit konzol_ir nevű metódusban 
    fogalmazzon meg! (2p)
⦁	A tizzel_osztahatoak_szama függvény eredményét írassa ki a mintának megfelelően a vegeredmeny.txt nevű fájlba, 
    amit fajlba_ir nevű metódusban fogalmazzon meg! (2p)

"""
import random

def sorozat():
    lista= []
    for i in range(0,8,1):
        szam=random.randint(-100,859)
        lista.append(szam)
        if i < 7:
            print(szam, end=";")
        else:
            print(szam, end="")

def tizzel_osztahatoak_szama(lista):
    i:int=0
    oszthatok_szama:int=0
    for i in range(8):
        if i%10==0:
            oszthatok_szama+=1
    return oszthatok_szama

def fajlba_ir():
    kimutatas = open("kimutatas.txt", "r", encoding='utf-8')
    kimutatas.close()


def konzol_ir(oszthato):
    print(f"Tízzel osztható számok száma: {oszthato}")

