#A program döntse el, hogy egy egész szám pozitív-e! Először tájékoztassa a felhasználót, hogy mire való a program! Az egész számot a konzolról kérje be! Ha a szám pozitív, akkor ezt írja ki a konzolra, egyébként ne írjon ki semmit!

def elso():
    print("A program eldönti egy egész számról, hogy pozitív-e!")
    szam = int(input("Kérem adjon meg egy egész számot!"))

    if szam > 0:
        print("A szám pozitív.")

#MegelőzőKövetkezőSzám: A program kérjen be a konzolról egy egész számot! Ha a szám egyjegyű, akkor a program írja ki a konzolra a számot megelőző és követő egész számot, egyébként ne írjon ki semmit!

def masodik():
    szam = int(input("Kérem adjon meg egy egész számot!"))

    if (szam >= -9) and (szam <=9):
        megelozo = szam-1
        rakovetkezo = szam+1

    print("A rákövetkező érték:"+str(rakovetkezo)+", a megelőző érték:"+str(megelozo))

