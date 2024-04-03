"""Korzystając z poprzedniego przykładu, utwórz zmienną c i przypisz jej kopię listy a (możesz 
użyć metody list() lub składni a[:]). Następnie zmodyfikuj pierwszy element w c i przypisz mu 
wartość 'nowa wartość'. Wyświetl listy a, b i c, zauważając, że tym razem zmiana w c nie 
wpłynęła na a ani b. Wyjaśnij, dlaczego kopiowanie listy zapobiegło współdzieleniu 
referencji"""

c = a[:]
c[0] = 'nowa wartość'
print(c)
#c to już nie jest wskaźnik
