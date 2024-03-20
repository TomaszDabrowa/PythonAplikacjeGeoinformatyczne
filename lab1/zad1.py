import json
"""Wczytaj jako słownik plik z rozszerzeniem JSON (przydatny może okazać się pakiet json). Zapisz do 
zmiennej połączone wszystkie teksty z pliku"""
with open("teksty.json", 'r', encoding='utf-8') as plik:
        teksty = json.load(plik)
print(teksty)
print(dir(teksty))
"""Zamień wszystkie duże litery na małe"""
for klucz, wartosc in teksty.items():
        if isinstance(wartosc, str):
                teksty[klucz] = wartosc.lower()
print(teksty)
#Podziel go na wyrazy - będzie to najprawdopodobniej lista
teksty_nowe = {}
for klucz, wartosc in teksty.items():
        if isinstance(wartosc, str):
            teksty_nowe[klucz] = wartosc.split()
print(teksty_nowe)
print(type(teksty_nowe))
