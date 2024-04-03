""" Napisz funkcję zamowienie_produktu, która przyjmuje jeden obowiązkowy argument 
pozycyjny nazwa_produktu i dwa obowiązkowe argumenty nazwane: cena i ilosc. Funkcja 
powinna zwracać tekst podsumowujący zamówienie, zawierające nazwę produktu, łączną 
cenę (cena * ilość) oraz ilość zamówionego produktu.
a. Stwórz pustą listę, do której wstawisz wartości zwracane przez funkcję dla 3 różnych 
produktów.
b. Przeiteruj po wypełnionej liście, wyświetl teksty.
c. Zmodyfikuj funkcję tak, żeby oprócz tekstu podsumowującego zwracała także 
wartość zamówienia.
d. Na koniec wyświetl sumaryczną wartość zamówień (sumę z każdego zamówionego 
produktu).
e. Dodaj wartość domyślną dla argumentu ilosc równą 1."""

def zamowienie_produktu(nazwa_produktu, *, cena, ilosc):
    laczna_cena = cena * ilosc
    podsumowanie = f"Produkt: {nazwa_produktu}, łączna cena: {laczna_cena}, ilość: {ilosc}"
    return laczna_cena, podsumowanie


zamowienia = []
zamowienia.append(zamowienie_produktu('Jabłka', cena = 2, ilosc = 5))
zamowienia.append(zamowienie_produktu('Maliny', cena = 3, ilosc = 4))

print(zamowienia)

for zamowienie in zamowienia:
    print(zamowienie)
suma_wszystkich = 0
for i in zamowienia:
    suma_wszystkich += zamowienie[0]
print(suma_wszystkich)