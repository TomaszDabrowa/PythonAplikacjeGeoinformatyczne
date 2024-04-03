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