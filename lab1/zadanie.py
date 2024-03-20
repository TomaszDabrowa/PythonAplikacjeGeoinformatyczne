import json
import string
with open('teksty.json', 'r') as file:
    dane = json.load(file)
    teksty = [tekst_dict.values() for tekst_dict in dane["teksty"]]

lacznyTekst = ' '.join([' '.join(tekst) for tekst in teksty])
laczny_tekst = lacznyTekst.lower() 
wyrazy = lacznyTekst.split()  
lacznyTekst = lacznyTekst.replace('.', '').replace(',', '') 
tempWyrazy = lacznyTekst.split()  
modWyrazy = []
for wyraz in tempWyrazy:
    wyraz_modyfikowany = wyraz[:-1] + wyraz[-1].upper()  
    modWyrazy.append(wyraz_modyfikowany)
modWyrazy = [wyraz for wyraz in modWyrazy if 'a' in wyraz or 'A' in wyraz]
countWystapienia = {}
for wyraz in modWyrazy:
    if wyraz in countWystapienia:
        countWystapienia[wyraz] += 1
    else:
        countWystapienia[wyraz] = 1
unikatowe_wyrazy = [wyraz for wyraz, wystapienia in countWystapienia.items() if wystapienia == 1]
data_to_save = {
    "wyrazy": wyrazy,
    "modWyrazy": modWyrazy,
    "unikatowe_wyrazy": unikatowe_wyrazy,
    "countWystapienia": countWystapienia
}
with open('wyniki.json', 'w') as json_file:
    json.dump(data_to_save, json_file, indent=4)
