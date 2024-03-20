#Napisz program, który iteruje przez listę imion używając pętli for oraz funkcji enumerate(), 
#aby wyświetlić indeks każdego imienia wraz z samym imieniem
imiona = [
    [123456, "Tomasz"],
    [789065, "Sławomir"],
    [365523, "Jakub"]
]

for i in enumerate(imiona):
    print(i)

"""
Stwórz przykłady dla testów if:
a. Gdzie wystąpią dwa warunki - napisz program sprawdzający czy dana liczba jest 
dodatnia i parzysta. Jeśli tak, program powinien wydrukować "Liczba jest dodatnia i 
parzysta".
b. Gdzie wykorzystane zostanie zaprzeczenie not lub =! - napisz program, który 
sprawdza, czy wprowadzona przez użytkownika liczba nie jest równa zero. Jeśli nie 
jest, wydrukuj "Liczba jest różna od zera".
c. Gdzie wykorzystane będzie słowo in - napisz program, który sprawdza, czy 
wprowadzony przez użytkownika owoc znajduje się na liście dostępnych owoców 
(np. ['jabłko', 'banan', 'pomarańcza']). Jeśli tak, program powinien wydrukować 
"Owoc jest dostępny".
"""

liczba = int(input())
#print(type(liczba))
if (liczba % 2 == 0) & (liczba > 0):
    print("Liczba jest dodatnia i parzysta")
else:
    print("Nie jest")

if liczba is not 0:
    print("Liczba jest różna od zera")

owoce = ['jabłko', 'banan', 'pomarańcza']
owoc = input()
if owoce.__contains__(owoc):
    print("Owoc jest dostępny")

"""Stwórz przykład z pętlą while - Stwórz program, który będzie ciągle prosił użytkownika o 
wprowadzenie liczby. Program powinien sumować wprowadzone liczby i kończyć działanie, 
gdy suma przekroczy 100. Po zakończeniu pętli, program powinien wydrukować sumę 
wprowadzonych liczb."""

suma = 0
liczba1 = 0
liczba2 = 0
while(suma <= 100):
    print("Pierwsza liczba: ")
    liczba1 = int(input())
    print(liczba1)
    print("Druga liczba: ")
    liczba2 = int(input())
    suma = liczba1 + liczba2 + suma
print(suma)


