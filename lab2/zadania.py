import this
#Mając daną krotkę dane = (2024, 'Python', 3.8), przypisz każdy element krotki do 
#odpowiednich zmiennych: rok, jezyk i wersja. Wyświetl te zmienne

dane = (2024, 'Python', 3.8)
rok = dane[0]
jezyk = dane[1]
wersja = dane[2]
print(rok, jezyk, wersja)

"""Mając listę oceny = [4, 3, 5, 2, 5, 4], przypisz pierwszą wartość do zmiennej pierwsza, 
ostatnią do ostatnia, a pozostałe do listy srodek. Wykorzystaj * do zgromadzenia 
środkowych wartości. Wyświetl te zmienne."""
oceny = [4, 3, 5, 2, 5, 4]
pierwsza, *srodek, ostatnia = oceny
print(pierwsza)
print(ostatnia)
print(srodek)

"""Dla krotki info = ('Jan', 'Kowalski', 30, 'Polska', 'programista'), przypisz imię do zmiennej 
imie, nazwisko do nazwisko, a zawód do zawod, ignorując pozostałe wartości. Doignorowania 
wykorzystaj znak _. Wyświetl przypisane zmienne"""

info = ('Jan', 'Kowalski', 30, 'Polska', 'programista')
imie, nazwisko, *_ , zawod = info
print(imie)
print(nazwisko)
print(zawod)

"""Mając zagnieżdżoną strukturę dane = (2024, ['Python', 3.8, ('Stabilna', 'Wersja')]), przypisz 
rok do zmiennej rok, nazwę języka do jezyk, wersję do wersja i opis wersji do zmiennej opis. 
Wyświetl te zmienne.
"""
dane = (2024, ['Python', 3.8, ('Stabilna', 'Wersja')])

rok, [jezyk, wersja, (opis, _)] = dane

#Przypisania z wieloma celami i współdzielone referencje

"""Stwórz zmienną a oraz b, użyj przypisania z wieloma celami i przypisz im listę [1, 2, 3]: a = b = 
[1, 2, 3]. Zmodyfikuj pierwszy element listy b przez przypisanie b[0] = 'zmieniono'. Wyświetl 
obie listy a i b, a następnie wyjaśnij, dlaczego zmiana w b wpłynęła również na a. Czy listy są 
obiektami mutowalnymi?"""

a = b = [1, 2, 3]
print(a)
print(b)

b[0] = 'zmieniono'
print(a)
print(b)
#są obiektami mutowalnymi, bo można je zmieniać w późniejszym czasie

"""Korzystając z poprzedniego przykładu, utwórz zmienną c i przypisz jej kopię listy a (możesz 
użyć metody list() lub składni a[:]). Następnie zmodyfikuj pierwszy element w c i przypisz mu 
wartość 'nowa wartość'. Wyświetl listy a, b i c, zauważając, że tym razem zmiana w c nie 
wpłynęła na a ani b. Wyjaśnij, dlaczego kopiowanie listy zapobiegło współdzieleniu 
referencji"""

c = a[:]
c[0] = 'nowa wartość'
print(c)
#c to już nie jest wskaźnik

"""Utwórz zmienną x oraz y, przypisz im wartość 10 poprzez x = y = 10. Zwiększ wartość y o 1 
(np. y = y + 1). Wyświetl wartości x i y, a następnie wyjaśnij, dlaczego modyfikacja y nie 
wpłynęła na wartość x. Czy integery są obiektami mutowalnymi?"""

x = y = 10
y = y + 1
print(x)
print(y)
#Integery w pythonie nie są obiektami mutowalnymi

#Przypisania rozszerzone i współdzielone referencje

"""Wyzwól następujący kod, wyświetl K, L, M i N. Wyjaśnij w jaki sposób konkatenacja 
zachowuje się inaczej od przypisania rozszerzonego."""

K = [1, 2]
L = K
K = K + [3, 4]
M = [1, 2]
N = M
M += [3, 4]

print(K)
print(L)
print(M)
print(N)

#Techniki tworzenia pętli - uzupełnienie
"""Mając dwie listy, imiona = ['Anna', 'Jan', 'Ewa'] i oceny = [5, 4, 3], użyj zip do stworzenia 
pary każdego imienia z odpowiadającą mu oceną. Następnie, iteruj przez te pary, 
wyświetlając imię wraz z oceną. Co się stanie, jeśli listy będą miały różne długości?"""

imiona = ['Anna', 'Jan', 'Ewa']
oceny = [5, 4, 3]

zipped = zip(imiona, oceny)
print(zipped)

for imie, ocena in zipped:
    print(imie, ' ', ocena)

"""Mając listę liczby = [1, 2, 3, 4, 5], napisz funkcję kwadrat(x), która zwraca kwadrat liczby x. 
Użyj map z tą funkcją, aby stworzyć nową listę, w której każdy element jest kwadratem 
odpowiadającego mu elementu z listy liczby. Wyświetl tą listę."""

liczby = [1, 2, 3, 4, 5]

def kwadrat(x):
    return x ** 2

kwadraty_liczb = list(map(kwadrat, liczby))
print(kwadraty_liczb)

#Argumenty
"""Napisz funkcję zmien_wartosc(arg), która przyjmuje jeden argument i próbuje 
zmodyfikować ten argument w różny sposób w zależności od tego, czy jest on niemutowalny 
(w tym przypadku integerem) czy mutowalny (w tym przypadku listą).
a. Jeśli jest listą, wykonaj arg[0] = 'kalafior '.
b. Jeśli jest integerem, wykonaj arg = 65482652.
"""
def zmien_wartosc(arg):
    if isinstance(arg, list):
        arg[0] = 'kalafior'
    elif isinstance(arg, int):
        arg = 65482652
    return arg

lista_przed = [1, 2, 3]
print(lista_przed)
zmien_wartosc(lista_przed)
print(lista_przed)

int_przed = 123
print(int_przed)
int_po = zmien_wartosc(int_przed)
print(int_po)

""" Napisz funkcję zamowienie_produktu, która przyjmuje jeden obowiązkowy argument 
pozycyjny nazwa_produktu i dwa obowiązkowe argumenty nazwane: cena i ilosc. Funkcja 
powinna zwracać tekst podsumowujący zamówienie, zawierające nazwę produktu, łączną 
cenę (cena * ilość) oraz ilość zamówionego produktu.
a. Stwórz pustą listę, do której wstawisz wartości zwracane przez funkcję dla 3 różnych 
produktów.
b. Przeiteruj po wypełnionej liście, wyświetl teksty.
c. Zmodyfikuj funkcję tak, żeby oprócz tekstu podsumowującego zwracała także 
wartość zamówienia.
d. Na koniec wyświetl sumaryczną wartość zamówień (sumę z każdego zamówionego 
produktu).
e. Dodaj wartość domyślną dla argumentu ilosc równą 1."""

def zamowienie_produktu(nazwa_produktu, *, cena, ilosc):
    laczna_cena = cena * ilosc
    podsumowanie = f"Produkt: {nazwa_produktu}, łączna cena: {laczna_cena}, ilość: {ilosc}"
    return laczna_cena, podsumowanie


zamowienia = []
zamowienia.append(zamowienie_produktu('Jabłka', cena = 2, ilosc = 5))
zamowienia.append(zamowienie_produktu('Maliny', cena = 3, ilosc = 4))

print(zamowienia)

for zamowienie in zamowienia:
    print(zamowienie)
suma_wszystkich = 0
for i in zamowienia:
    suma_wszystkich += zamowienie[0]
print(suma_wszystkich)

"""Napisz funkcję stworz_raport, która przyjmuje dowolną liczbę argumentów pozycyjnych 
(*args) i nazwanych (**kwargs). Argumenty pozycyjne powinny reprezentować numery ID 
produktów, a argumenty nazwane - informacje o tych produktach (np. nazwa, cena). Funkcja 
powinna tworzyć i wyświetlać raport, w którym dla każdego ID produktu podane są 
szczegółowe informacje na jego temat"""

def stworz_raport(*args, **kwargs):
    
    for i in args:
        print(f"ID: {i}")
    for klucz, wartosc in kwargs.items():
        print(f"{klucz}: {wartosc}")

stworz_raport(1, 2, 3, imie="Tomek", nazwisko="Dąbrowa", wiek=80)

#FUNKCJE FABRYKUJĄCE
"""Napisz funkcję fabrykującą stworz_funkcje_potegujaca(wykladnik), która przyjmuje jeden 
argument: wykładnik potęgi. Zwracana przez nią funkcja zagnieżdżona poteguj(podstawa)
powinna również przyjmować jeden argument (podstawę potęgi) i zwracać wynik 
podniesienia tej podstawy do potęgi określonej przez wykładnik przekazany do funkcji 
zewnętrznej"""

def stworz_funkcje_potegujaca(wykladnik):
    
    def poteguj(podstawa):
        return podstawa ** wykladnik
    
    return poteguj

potega_2 = stworz_funkcje_potegujaca(2) # Tworzy funkcję potęgującą do kwadratu
print(potega_2(4)) # Wynik: 16

"""Napisz funkcję licznik(), która za każdym razem, gdy jest wywoływana, zwiększa swoje 
wewnętrzne liczenie o jeden (licznik stanu). Zaimplementuj cztery wersje tej funkcji, 
wykorzystując:
a. Zmienną nonlocal w zagnieżdżonej funkcji.
b. Zmienną global.
c. Klasę z atrybutem instancji. # Wskazówka: zaimplementowanie w klasie funkcji 
__init__ oraz __call__
d. Atrybut funkcji. # Funkcja, jak każdy inny obiekt, może mieć swoje atrybuty"""

def licznik_nonlocal():
    licznik = 0
    def inkrementuj():
        nonlocal licznik
        licznik += 1
        return licznik
    return inkrementuj


inkrementuj = licznik_nonlocal()
print(inkrementuj())  # Wynik: 1
print(inkrementuj())  # Wynik: 2

licznik_globalny = 0

def licznik_global():
    global licznik_globalny
    licznik_globalny += 1
    return licznik_globalny


print(licznik_global())  # Wynik: 1
print(licznik_global())  # Wynik: 2


class LicznikKlasa:
    def __init__(self):
        self.licznik = 0

    def __call__(self):
        self.licznik += 1
        return self.licznik


inkrementuj_klasa = LicznikKlasa()
print(inkrementuj_klasa())  # Wynik: 1
print(inkrementuj_klasa())  # Wynik: 2


def licznik_funkcja():
    if not hasattr(licznik_funkcja, 'licznik'):
        licznik_funkcja.licznik = 0
    licznik_funkcja.licznik += 1
    return licznik_funkcja.licznik


print(licznik_funkcja())  # Wynik: 1
print(licznik_funkcja())  # Wynik: 2

#ADNOTACJE
"""Dodaj adnotacje typów argumentów oraz wartości zwracanej do wybranej przez siebie 
funkcji."""

def licznik_funkcja() -> int:
    if not hasattr(licznik_funkcja, 'licznik'):
        licznik_funkcja.licznik = 0
    licznik_funkcja.licznik += 1
    return licznik_funkcja.licznik


print(licznik_funkcja())  # Wynik: 1
print(licznik_funkcja())  # Wynik: 2

# Funkcje anonimowe – lambda

"""Masz daną listę słowników reprezentujących informacje o książkach w bibliotece. Każdy 
słownik zawiera klucze: 'tytul', 'autor' oraz 'rok_wydania'. Twoim zadaniem jest napisanie 
kodu, który wykonuje następujące operacje przy użyciu funkcji lambda:
a. Sortowanie książek według roku wydania: Posortuj listę książek w kolejności 
rosnącej według roku ich wydania.
b. Filtracja książek wydanych po 2000 roku: Utwórz nową listę zawierającą tylko te 
książki, które zostały wydane po roku 2000.
c. Transformacja listy do listy tytułów: Przekształć oryginalną listę książek w listę 
zawierającą tylko tytuły książek.
Wykorzystaj funkcje sorted(), filter() oraz map() w połączeniu z funkcjami lambda do realizacji 
zadania.
"""

lista_ksiazek = [
    {'tytul': 'Hekser', 'autor': 'Autor A', 'rok_wydania': 1998},
    {'tytul': 'Pitło z luftym', 'autor': 'Autor B', 'rok_wydania': 2005},
    {'tytul': 'Beboki i kamraty', 'autor': 'Autor C', 'rok_wydania': 2010},
    {'tytul': 'Chopy we czornych ancugach', 'autor': 'Autor D', 'rok_wydania': 1995},
    {'tytul': 'Mały Princ', 'autor': 'Autor E', 'rok_wydania': 2020}
]
#print(lista_ksiazek)
posortowane_ksiazki = sorted(lista_ksiazek, key=lambda x: x['rok_wydania'])
print("Posortowane książki według roku wydania:")
print(posortowane_ksiazki)

książki_po_2000 = list(filter(lambda x: x['rok_wydania'] > 2000, lista_ksiazek))
print("\nKsiążki wydane po 2000 roku:")
print(książki_po_2000)

tytuły_ksiazek = list(map(lambda x: x['tytul'], lista_ksiazek))
print("\nTytuły książek:")
print(tytuły_ksiazek)


#Generatory – funkcje generatorów i wyrażenia generatorów

"""Napisz generator, który iteracyjnie zwraca nazwy dni tygodnia: od poniedziałku do niedzieli. 
Następnie, użyj tego generatora w pętli, aby wyświetlić każdy dzień tygodnia. Dodatkowo, 
zademonstruj, jak można użyć tego generatora do pobrania tylko pierwszych trzech dni 
tygodnia bez konieczności iterowania przez cały tydzień."""

def wypisz_dni(ilosc):
    dni = ['poniedziałek','wtorek','środa','czwartek','piątek','sobota','niedziela']
    for dzien in range(ilosc):
        print(dni[dzien])

wypisz_dni(6)
wypisz_dni(2)

