"""Napisz funkcję zmien_wartosc(arg), która przyjmuje jeden argument i próbuje 
zmodyfikować ten argument w różny sposób w zależności od tego, czy jest on niemutowalny 
(w tym przypadku integerem) czy mutowalny (w tym przypadku listą).
a. Jeśli jest listą, wykonaj arg[0] = 'kalafior '.
b. Jeśli jest integerem, wykonaj arg = 65482652.
"""
def zmien_wartosc(arg):
    if isinstance(arg, list):
        arg[0] = 'kalafior'
    elif isinstance(arg, int):
        arg = 65482652
    return arg

lista_przed = [1, 2, 3]
print(lista_przed)
zmien_wartosc(lista_przed)
print(lista_przed)

int_przed = 123
print(int_przed)
int_po = zmien_wartosc(int_przed)
print(int_po)