#import pakiet1

#print(dir(pakiet1))

lista =(1,2,"123",123, 3)
a, *b, c = lista

a = 123
b = a

print(a,b)

_ = 123

for x in range(len(lista)):
    print(lista[x])

x = [y for y in [1,2,3,4] if y < 3]

lista1 = [1,2,3,4]
lista2 = ["123","sd","sdf"]

def funkcja1(x):
    return x ** 2

wynik_map = map(funkcja1,lista1)

#for z in map(funkcja1, lista1):
#    print(next(wynik_map))

print(next(wynik_map))
print(next(wynik_map))
print(next(wynik_map))
