
litery = 0
cyfry = 0
spacje = 0
znaki_interpunkyjne = 0
male_litery = 0
duze_litery = 0
cyfr_w_liczbie = 0

with open("test.txt", "r+") as plik:
    caly_tekst = plik.read()
    ile_znakow = len(caly_tekst)
    ile_wyrazow = len(caly_tekst.split())
    ile_zdan = len(caly_tekst.split('.')) - 1 + len(caly_tekst.split('!')) - 1 + len(caly_tekst.split('?')) - 1
    for i in caly_tekst:
        if i.isalpha():
            litery += 1
            if i.islower():
                male_litery += 1
            else:
                duze_litery += 1
        elif i.isnumeric():
            cyfry += 1
        elif i.isspace():
            spacje += 1
        else:
            znaki_interpunkyjne += 1

print(f"Liczba znalezionych w tekście wszystkich znaków: {ile_znakow}")
print(f"Liczba znalezionych w tekście wyrazów: {ile_wyrazow}")
print(f"Liczba znalezionych w tekście zdan: {ile_zdan}")
print(f"Liczba znalezionych w tekście liter: {litery}")
print(f"Liczba znalezionych w tekście cyfr: {cyfry}")
print(f"Liczba znalezionych w tekście spacjii: {spacje}")
print(f"Liczba znalezionych w tekście znaków interpunkcyjnych: {znaki_interpunkyjne}")
print(f"Liczba znalezionych w tekście małych liter: {male_litery}")
print(f"Liczba znalezionych w tekście dużych liter: {duze_litery}")

