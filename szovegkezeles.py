def szepnapvan():
    szoveg: str = "Szép nap van!"

    '''Íed ki a szöveg első karakterét!'''
    print("1. ",szoveg[0])
    '''Írd ki a szöveg 2. karakterét!'''
    print("2. ",szoveg[1])
    '''Írd ki a szöveg HOSSZÁT!'''
    print("A hossz: ",len(szoveg))
    '''Írd ki a szöveg utolsó karakterét!'''
    print("utolso ",szoveg[len(szoveg)-1])
    """Írd ki a szöveg karaktereit egymás alá betűnként """
    i:int = 0
    while i < len(szoveg):
        print(szoveg[i])
        i += 1

def szovegkezeles():
    szoveg:str = "Ez egy teszt szöveg."
    print(szoveg)
    print(szoveg.upper())

    """Van-e a szövegben 'teszt' szöveg"""
    x:int = szoveg.find("teszt")
    if x >=0:
        print("van benne teszt szöveg")
    else:
        print("nincs benne teszt szöveg")

    
    """A SZOVEG változatban hol szerepel először az 's' betű?"""
    print(szoveg.index("s"), ". helyen szetepel s betű!")

    """Alakytsd át minden szó kezdőbetűjét nagybetűssé!"""
    print(szoveg.title())

    """Cseréld ki a teszt szót 'próba'-ra!"""
    print(szoveg.replace("teszt","proba"))

def a_szoveg_visszafele(szoveg:str):
    '''A paraméterben kapott szöveg visszafelé kiirva egymás mellé a betűket'''
    i:int= len(szoveg)
    while i!=0:
        print(szoveg[i-1], end="")
        i -= 1



def a_betuk_szama(szoveg:str):
    '''Hány "a" betű van a szövegben?'''
    # print(szoveg.count("a"))
    i:int = 0
    a_szam:int = 0
    while i<len(szoveg):
        if szoveg[i] == 'a':
            a_szam += 1
        i += 1
    print("A betűk száma: ",a_szam)
