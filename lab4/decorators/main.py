import time

def dekorator(funkcja):
    def wewnetrzna_funkcja(**kwargs):
        print("Rozpoczęcie wykonywania funkcji")
        unit = "seconds"  # Domyślna wartość jednostki czasu
        if 'unit' in kwargs:  # Sprawdzenie, czy 'unit' został przekazany jako argument kwargs
            unit = kwargs['unit']

        timestampBefore = time.time()
        funkcja()
        timestampAfter = time.time()
        print("Zakończenie wykonywania funkcji")
        czasWykonania = timestampAfter - timestampBefore
        if unit == "seconds":
            print(f"Czas wykonania: {czasWykonania} s")
        elif unit == "miliseconds":
            print(f"Czas wykonania: {czasWykonania*1000} ms")
        else:
            print(f"Czas wykonania: {czasWykonania} s")

    return wewnetrzna_funkcja

@dekorator
def moja_funkcja():
    for i in range(5):
        print(i)
    time.sleep(1)

moja_funkcja(unit="seconds")
moja_funkcja(unit="miliseconds")