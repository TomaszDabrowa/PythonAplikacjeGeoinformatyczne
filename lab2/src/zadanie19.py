"""Napisz funkcję fabrykującą stworz_funkcje_potegujaca(wykladnik), która przyjmuje jeden 
argument: wykładnik potęgi. Zwracana przez nią funkcja zagnieżdżona poteguj(podstawa)
powinna również przyjmować jeden argument (podstawę potęgi) i zwracać wynik 
podniesienia tej podstawy do potęgi określonej przez wykładnik przekazany do funkcji 
zewnętrznej"""

def stworz_funkcje_potegujaca(wykladnik):
    
    def poteguj(podstawa):
        return podstawa ** wykladnik
    
    return poteguj

potega_2 = stworz_funkcje_potegujaca(2) # Tworzy funkcję potęgującą do kwadratu
print(potega_2(4)) # Wynik: 16