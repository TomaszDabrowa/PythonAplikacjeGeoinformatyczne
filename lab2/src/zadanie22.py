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
