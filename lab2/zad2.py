a = [1,2,3,4]
b = 12

def funkcja1(*args,**kwargs):
    #x[0] = "123"
    #y = 321432
    #print(f"Wewnątrz funkcji: {x} {y}")
    print(args)
    print(kwargs)
    #return x
print(a,b)
print(funkcja1(a,b))
print(a,b)
funkcja1(1,2,3,4,5,6,7, b="123", c="sd")

def funkc1(a = [1,2,3,4]):
    for i in a:
        return i ** 2

print(funkc1([2,3,4]))

