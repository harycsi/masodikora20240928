#Készíts egy programot, amely beolvas 3 valós számot, majd kiírja őket, mindegyiket egy sorba szóközzel elválasztva!
#függvény(van visszatérési értéke)
def beolvas():
    szam = float(input("Kérem adjon meg egy számot!"))
    return szam

#eljárás(nincsen visszatérési értéke)
def negyedikFeladat():
    szam1 = beolvas()
    szam2 = beolvas()
    szam3 = beolvas()
    #print(szam)
    #print(type(szam))
    print(str(szam1)+ " "+str(szam2)+" "+str(szam3))
