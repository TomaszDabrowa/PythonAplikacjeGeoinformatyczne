import math
import random
wartosc = 100
print(type(wartosc))
dodawanie = wartosc + 123.15
print(type(dodawanie))
potega = dodawanie ** 12
print(type(potega))
tekst = str(potega)
print(type(tekst))
wartosc_pi = math.pi
print(type(wartosc_pi))
lista = [1,2,3,4,5]
losowa = random.choice(lista)
print(losowa)
print(type(losowa))

tekst = f"Wartosc: {tekst}"
print(tekst)
print(type(tekst))
print(len(tekst))
print(tekst[tekst.find("art"): tekst.find("art") + 3])
print(dir(tekst))
print(tekst.upper())
#tekst[1] = "p"
tekst = tekst.upper()
print(tekst)

#działania na listach

lista = list(tekst)
print(tekst[:8])

lista2 = [1,2,3,4,5]
lista.append(lista2)
print(lista)
print(dir(lista))

lista.remove(":")
print(lista)

#listy składane
lista2 = [1,2,3,"banan",100]
lista3 = []
for i in lista2:
    if i != "banan":
        lista3.append(i**2)
lista4 = []
for i in range(2,16,2):
    lista4.append(i)
print(lista2)
print(lista3)
print(lista4)

#SŁOWNIKI
ja = {}
ja = {
    "imie": "Tomasz",
    "nazwisko": "Machowski",
    "wiek": 18,
    "rodzice": [
        {"imie": "Waleria", "wiek": 78},
        {"imie": "Jerzy", "wiek": 80}
    ]
}
print(ja)

#wypisz wartość klucza rodzice
print(ja["rodzice"])
#Wypisz jedynie imię pierwszego z rodziców
print(ja["rodzice"][0])
#Wypisz wszystkie klucze naszego słownika
print(ja.keys())
#Sprawdź czy nasz słownik posiada klucz rodzenstwo, wypisz zmienną typu boolean
print(dir(ja.keys()))
if ja.keys().__contains__("rodzenstwo") == True:
    print(True)
else:
    print(False)

#KROTKI
krotka1 = (1,2,"3",4,2,5)
print(krotka1)
#Wypisz długość zmiennej i pierwszy wyraz
print(len(krotka1))
print(krotka1[0])
#Sprawdź, ile razy występuje wartość 2 i wypisz
print(dir(krotka1))
print(krotka1.count(2))
#Spróbuj zmienić pierwszy wyraz na wartość 2.
#krotka1[0] = 2

#ZBIORY
#Stwórz dwa zbiory o nazwach X i Y, nadaj im wartości odpowiednio: set("kalarepa") oraz set("lepy")
X = set("kalarepa")
Y = set("lepy")
print(X)
print(Y)
#Wyświetl część wspólną obu zbiorów - można na nich wykonywać podobne operacje jak na 
#zbiorach matematycznych
print(X & Y)

#Napisz program, który iteruje przez listę imion używając pętli for oraz funkcji enumerate(), 
#aby wyświetlić indeks każdego imienia wraz z samym imieniem

