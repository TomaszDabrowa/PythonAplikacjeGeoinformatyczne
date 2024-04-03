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