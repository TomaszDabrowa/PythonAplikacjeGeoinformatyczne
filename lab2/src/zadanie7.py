"""Mając listę oceny = [4, 3, 5, 2, 5, 4], przypisz pierwszą wartość do zmiennej pierwsza, 
ostatnią do ostatnia, a pozostałe do listy srodek. Wykorzystaj * do zgromadzenia 
środkowych wartości. Wyświetl te zmienne."""
oceny = [4, 3, 5, 2, 5, 4]
pierwsza, *srodek, ostatnia = oceny
print(pierwsza)
print(ostatnia)
print(srodek)