"""Napisz generator, który iteracyjnie zwraca nazwy dni tygodnia: od poniedziałku do niedzieli. 
Następnie, użyj tego generatora w pętli, aby wyświetlić każdy dzień tygodnia. Dodatkowo, 
zademonstruj, jak można użyć tego generatora do pobrania tylko pierwszych trzech dni 
tygodnia bez konieczności iterowania przez cały tydzień."""

def wypisz_dni(ilosc):
    dni = ['poniedziałek','wtorek','środa','czwartek','piątek','sobota','niedziela']
    for dzien in range(ilosc):
        print(dni[dzien])

wypisz_dni(6)
wypisz_dni(2)