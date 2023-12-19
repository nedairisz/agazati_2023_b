"""
I/A, B:
    Hét napja: Hétfő
    Óra neve: Programozás alapjai
    Értékelés (0-5): 5
 
I/C:
    Köszönjük az értékelést! 
	Összefoglaló: ’Hétfő’, ’Programozás alapjai’, 5 érték

A.	Kérje be az alábbi adatokat a fenti mintának megfelelően:
    hét napja, óra neve és értékelés!  (2p)
B.	A program az adatbekérés után írja ki, ha az értékelés nem a megfelelő határokon belül lett megadva ( [0,5], zárt intervallum értendő):
    Amennyiben negatív számot adott meg:
    “Az értékelés nem lehet negatív!”,
    Amennyiben 5 feletti egész számot adott meg:
    “5 pont feletti értékelés nem elfogadható!”
    Helyes pont-adat esetén:
    “Köszönjük az értékelést!” 
    Feltételezzük, hogy csak egész számokat adnak meg. (4p)
C.	A mintának megfelelően írassa ki az eredményt! (1p)

"""
def ertekeles():
    i:int=0
    nap:str= str(input("Hét napja: "))
    ora:str=str(input("Óra neve: "))
    ert:int=int(input("Értékelés: "))
    while not(0<=ert<=5):
        if ert<0:
            print("Az értékelés nem lehet negatív!")
            ert:int=int(input("Értékelés: "))
        elif ert>5:
            print("5 pont feletti értékelés nem elfogadható!")
            ert:int=int(input("Értékelés: "))
        i+=1
    print()
    print("I/C:")
    print("\t Köszönjük az értékelést!")
    print(f"\t Összefoglaló: {nap}, {ora}, {ert} érték")
