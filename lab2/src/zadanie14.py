"""Mając dwie listy, imiona = ['Anna', 'Jan', 'Ewa'] i oceny = [5, 4, 3], użyj zip do stworzenia 
pary każdego imienia z odpowiadającą mu oceną. Następnie, iteruj przez te pary, 
wyświetlając imię wraz z oceną. Co się stanie, jeśli listy będą miały różne długości?"""

imiona = ['Anna', 'Jan', 'Ewa']
oceny = [5, 4, 3]

zipped = zip(imiona, oceny)
print(zipped)

for imie, ocena in zipped:
    print(imie, ' ', ocena)
