def funkc1(a):
    for i in a:
        yield i **2

generator = funkc1([2,3,4])
generator2 = (x ** 2 for x in [2,3,4,5])
for i in generator:
    print(i)
print(next(generator))
print(next(generator))