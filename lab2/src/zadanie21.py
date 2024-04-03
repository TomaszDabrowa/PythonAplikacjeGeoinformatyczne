"""Dodaj adnotacje typów argumentów oraz wartości zwracanej do wybranej przez siebie 
funkcji."""

def licznik_funkcja() -> int:
    if not hasattr(licznik_funkcja, 'licznik'):
        licznik_funkcja.licznik = 0
    licznik_funkcja.licznik += 1
    return licznik_funkcja.licznik


print(licznik_funkcja())  # Wynik: 1
print(licznik_funkcja())  # Wynik: 2