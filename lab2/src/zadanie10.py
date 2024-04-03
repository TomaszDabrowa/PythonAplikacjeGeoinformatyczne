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
