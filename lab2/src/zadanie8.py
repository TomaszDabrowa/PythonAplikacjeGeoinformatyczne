"""Dla krotki info = ('Jan', 'Kowalski', 30, 'Polska', 'programista'), przypisz imię do zmiennej 
imie, nazwisko do nazwisko, a zawód do zawod, ignorując pozostałe wartości. Doignorowania 
wykorzystaj znak _. Wyświetl przypisane zmienne"""

info = ('Jan', 'Kowalski', 30, 'Polska', 'programista')
imie, nazwisko, *_ , zawod = info
print(imie)
print(nazwisko)
print(zawod)