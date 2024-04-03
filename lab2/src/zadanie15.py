"""Mając listę liczby = [1, 2, 3, 4, 5], napisz funkcję kwadrat(x), która zwraca kwadrat liczby x. 
Użyj map z tą funkcją, aby stworzyć nową listę, w której każdy element jest kwadratem 
odpowiadającego mu elementu z listy liczby. Wyświetl tą listę."""

liczby = [1, 2, 3, 4, 5]

def kwadrat(x):
    return x ** 2

kwadraty_liczb = list(map(kwadrat, liczby))
print(kwadraty_liczb)