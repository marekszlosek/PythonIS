import random
import sys

def sprawdzenie_czy_liczba(): #Zabezpieczenie przed wpisaniem innych danych z klawiatury niż liczby
    while True:
        wartosc = input("Podaj liczbe odpowiadającą programowi, który chcesz wybrać: ")
        try:
            wartosc = float(wartosc)
            break
        except:
            print("\nERROR!\nWPISANA WARTOSC NIE JEST LICZBĄ! SPRÓBUJ JESZCZE RAZ")
    return wartosc

def wybor_funkcji(): #Interfejs wyboru funkcji
    print("Witaj w Multitool Python Program by iSA - wersja beta ;)")
    print("Wybierz program który cię interesuje:")
    print("    1. Kalkulator pezeliczania stopni Celsjusza na Farenheita")
    print("    2. Kalkulator pezeliczania stopni Farenheita na Celsjusza")
    print("    3. Obliczanie pola powierzchni koła")
    print("    4. Pierwsza i ostatnia cyfra podanej liczby")
    print("    5. Rysowanie prostokata o podanej wysokości i szerokości")
    print("    6. Przelicznik liczb binarnych na dziesiętne")
    print("    7. Rozpoznawanie, czy podana liczba jest parzyta")
    print("    8. Czy podana liczba jest podzielna przez 3 lub 5 lub 7")
    print("    9. Czy podana liczba jest podzielna przez 3 i 5 i 7")
    print("   10. Czy podany rok jest rokiem przestępnym")
    print("   11. Wyświetlanie podanej listy")
    print("   12. Kwota zamieniona na monety")
    print("   13. Rysowanie piramidy o zadanej wysokości")
    print("   14. Obliczanie wieku psa")
    print("   15. Wybierz losowo program")
    print("   16. Wyjście")

    while True:
        wybor = sprawdzenie_czy_liczba()
        if (wybor < 17):
            break
        else:
            print("WPISANEJ WARTOŚCI NIE MA W MENU! PODAJ JESZCZE RAZ!\n")
            continue
    return wybor

def Kalkulator_pezeliczania_stopni_Celsjusza_na_Farenheita():
    print("KALKULATOR PRZELICZANIA STOPNI CELSJUSZA NA FARENHEITA\n")

    def sprawdzenie_czy_liczba():  # Zabezpieczenie przed wpisaniem innych danych z klawiatury niż liczby
        while True:
            wartosc = input("Wpisz stopnie Celsjusza: ")
            try:
                wartosc = float(wartosc)
                break
            except:
                print("\nERROR!\nWPISANA WARTOSC NIE JEST LICZBĄ! SPRÓBUJ JESZCZE RAZ")
        return wartosc

    def kalkulator_celsjusz_farenheit(celsjusz):  # Obliczanie stopni Farenheita
        farenheit = celsjusz * 1.8 + 32
        celsjusz = str(celsjusz)
        farenheit = str(farenheit)
        print("\nWzór: Stopnie Celsjusza * 1.8 + 32 = Stopnie Farenheita ")
        print(celsjusz + " * 1.8 + 32 = " + farenheit)

    wpisana_wartosc = sprawdzenie_czy_liczba()
    kalkulator_celsjusz_farenheit(wpisana_wartosc)

def Kalkulator_pezeliczania_stopni_Farenheita_na_Celsjusza():
    print("KALKULATOR PRZELICZANIA STOPNI FARENHEITA NA CELSJUSZA \n")

    def sprawdzenie_czy_liczba():  # Zabezpieczenie przed wpisaniem innych danych z klawiatury niż liczby
        while True:
            wartosc = input("Wpisz stopnie Farenheita: ")
            try:
                wartosc = float(wartosc)
                break
            except:
                print("\nERROR!\nWPISANA WARTOSC NIE JEST LICZBĄ! SPRÓBUJ JESZCZE RAZ")
        return wartosc

    def kalkulator_farenheit_celsjusz(farenheit):  # Obliczanie stopni Celsjusza
        celsjusz = (farenheit - 32) / 1.8
        celsjusz = str(celsjusz)
        farenheit = str(farenheit)
        print("\nWzór: (Stopnie Farenheita -32)/1.8 = Stopnie Celsjusza ")
        print("(" + farenheit + " - 32) / 1.8 = " + celsjusz)

    wpisana_wartosc = sprawdzenie_czy_liczba()
    kalkulator_farenheit_celsjusz(wpisana_wartosc)

def Obliczanie_pola_powierzchni_kola():
    print("KALKULATOR DO OBLICZENIA POLA POWIERZCHNI KOŁA \n")

    def sprawdzenie_czy_liczba():  # Zabezpieczenie przed wpisaniem innych danych z klawiatury niż liczby
        while True:
            wartosc = input("Wprowadz promień koła r: ")
            try:
                wartosc = float(wartosc)
                break
            except:
                print("\nERROR!\nWPISANA WARTOSC NIE JEST LICZBĄ! SPRÓBUJ JESZCZE RAZ")
        return wartosc

    def pole_kola(promien):  # Obliczanie pola kołą
        promien = promien ** 2
        pole_kola = 3.14 * promien
        pole_kola = str(pole_kola)
        promien = str(promien)
        print("\nWzór: Pole koła = Pi * r^2")
        print(promien + " * Pi = " + pole_kola)

    wpisana_wartosc = sprawdzenie_czy_liczba()
    pole_kola(wpisana_wartosc)

def Pierwsza_i_ostatnia_cyfra_podanej_liczby():
    def sprawdzenie_czy_liczba():  # Zabezpieczenie przed wpisaniem innych danych z klawiatury niż liczby
        while True:
            wartosc = input("Podaj liczbe: ")
            try:
                if ('.' in wartosc):  # Sprawdzenie czy wpisana wartość to int albo float
                    wartosc = float(wartosc)
                else:
                    wartosc = int(wartosc)
                break
            except:
                print("\nERROR!\nWPISANA WARTOSC NIE JEST LICZBĄ! SPRÓBUJ JESZCZE RAZ")
        return wartosc

    def sprawdzenie_czy_ulamek(wartosc):
        if ('.' in wartosc):
            wartosc = float(wartosc)
        else:
            wartosc = int(wartosc)

    def pierwsza_i_ostatnia(liczba):
        liczba = str(liczba)
        print("Pierwsza cyfra tej liczby to: " + liczba[0] + ", a ostatnia cyfra tej liczby to: " + liczba[-1])

    wpisana_wartosc = sprawdzenie_czy_liczba()
    pierwsza_i_ostatnia(wpisana_wartosc)

def Rysowanie_prostokata_o_podanej_wysokosci_i_szerokosci():
    def sprawdzenie_czy_liczba_wysokosc():  # Zabezpieczenie przed wpisaniem innych danych z klawiatury niż liczby
        while True:
            wartosc = input(
                "Podaj wysokosc prostokata (W przypadku podania liczby zmiennoprzecinkowej, będzie ona zaokrąglona w dół): ")
            try:
                wartosc = float(wartosc)
                break
            except:
                print("\nERROR!\nWPISANA WARTOSC NIE JEST LICZBĄ! SPRÓBUJ JESZCZE RAZ")
        return wartosc

    def sprawdzenie_czy_liczba_szerokosc():  # Zabezpieczenie przed wpisaniem innych danych z klawiatury niż liczby
        while True:
            wartosc = input(
                "Podaj szerokość prostokata (W przypadku podania liczby zmiennoprzecinkowej, będzie ona zaokrąglona w dół): ")
            try:
                wartosc = float(wartosc)
                break
            except:
                print("\nERROR!\nWPISANA WARTOSC NIE JEST LICZBĄ! SPRÓBUJ JESZCZE RAZ")
        return wartosc

    def zamiana_na_int(wartosc):
        wartosc = wartosc // 1
        wartosc = int(wartosc)
        return wartosc

    def rysowanie(szerokosc, wysokosc):
        print("+" + '-' * szerokosc + "+")
        print(wysokosc * ("|" + " " * szerokosc + "|\n") + "+" + '-' * szerokosc + "+")

    wysokosc = sprawdzenie_czy_liczba_wysokosc()
    szerokosc = sprawdzenie_czy_liczba_szerokosc()
    wysokosc = zamiana_na_int(wysokosc)
    szerokosc = zamiana_na_int(szerokosc)
    rysowanie(szerokosc, wysokosc)

def Przelicznik_liczb_binarnych_na_dziesietne():
    def sprawdzenie_czy_liczba():  # Zabezpieczenie przed wpisaniem innego ciągu znaków niż binarny oraz sprawdzenie czy am 6 znaków
        licznik = 0
        while licznik < 6:
            wartosc = input("Podaj liczbe binarną (6 znaków): ")
            for i in wartosc:
                if (i == '1' or i == '0'):
                    licznik = licznik + 1
                    continue
                else:
                    print("To nie jest liczba binarna! ")
                    licznik = 0
                    break
            if (licznik == 6):
                return wartosc
            else:
                print("Spróbuj ponownie!\n")
                licznik = 0

    def bin_dziesietna(liczba_binarna):
        liczba_1 = int(liczba_binarna[-1]) * 2
        liczba_2 = int(liczba_binarna[-2]) * 2
        liczba_3 = int(liczba_binarna[-3]) * 2
        liczba_4 = int(liczba_binarna[-4]) * 2
        liczba_5 = int(liczba_binarna[-5]) * 2
        liczba_6 = int(liczba_binarna[-6]) * 2
        liczba_dziesietna = liczba_6 ** 5 + liczba_5 ** 4 + liczba_4 ** 3 + liczba_3 ** 2 + liczba_2 ** 1 + liczba_1 ** 0
        liczba_dziesietna = str(liczba_dziesietna)
        print("Liczba dziesietna: " + liczba_dziesietna)

    liczba = sprawdzenie_czy_liczba()
    bin_dziesietna(liczba)

def Rozpoznawanie_czy_podana_liczba_jest_parzyta():
    def sprawdzenie_czy_liczba():  # Zabezpieczenie przed wpisaniem innych danych z klawiatury niż liczby
        while True:
            wartosc = input("Wprowadz liczbe: ")
            try:
                wartosc = float(wartosc)
                break
            except:
                print("\nERROR!\nWPISANA WARTOSC NIE JEST LICZBĄ! SPRÓBUJ JESZCZE RAZ")
        return wartosc

    def czy_parzysta(wartosc):
        parzysta = wartosc % 2  # Warunek podzielności przez 2
        wartosc = str(wartosc)
        if (parzysta == 0):
            print("\nLiczba " + wartosc + " jest parzysta!")
        else:
            print("\nLiczba " + wartosc + " jest nie parzysta!")

    liczba = sprawdzenie_czy_liczba()
    czy_parzysta(liczba)

def Czy_podana_liczba_jest_podzielna_przez_3_lub_5_lub_7():
    def sprawdzenie_czy_liczba():  # Zabezpieczenie przed wpisaniem innych danych z klawiatury niż liczby
        while True:
            wartosc = input("Wprowadz liczbe: ")
            try:
                wartosc = float(wartosc)
                break
            except:
                print("\nERROR!\nWPISANA WARTOSC NIE JEST LICZBĄ! SPRÓBUJ JESZCZE RAZ")
        return wartosc

    def sprawdzenie_podzielnosci(liczba):
        if (liczba % 3 == 0 or liczba % 5 == 0 or liczba % 7 == 0):
            print("\nPodana liczba jest podzielna przez 3 lub 5 lub 7")
        else:
            print("\nPodana liczba nie jest podzielna przez 3 lub 5 lub 7")

    liczba = sprawdzenie_czy_liczba()
    sprawdzenie_podzielnosci(liczba)

def Czy_podana_liczba_jest_podzielna_przez_3_i_5_i_7():
    def sprawdzenie_czy_liczba():  # Zabezpieczenie przed wpisaniem innych danych z klawiatury niż liczby
        while True:
            wartosc = input("Wprowadz liczbe: ")
            try:
                wartosc = float(wartosc)
                break
            except:
                print("\nERROR!\nWPISANA WARTOSC NIE JEST LICZBĄ! SPRÓBUJ JESZCZE RAZ")
        return wartosc

    def sprawdzenie_podzielnosci(liczba):
        if (liczba % 3 == 0 and liczba % 5 == 0 and liczba % 7 == 0):
            print("\nPodana liczba jest podzielna przez 3 i 5 i 7")
        else:
            print("\nPodana liczba nie jest podzielna przez 3 i 5 i 7")

    liczba = sprawdzenie_czy_liczba()
    sprawdzenie_podzielnosci(liczba)

def Czy_podany_rok_jest_rokeim_przestepnym():
    def sprawdzenie_czy_liczba():  # Zabezpieczenie przed wpisaniem innych danych z klawiatury niż liczby
        while True:
            wartosc = input("Wprowadz rok: ")
            try:
                wartosc = float(wartosc)
                break
            except:
                print("\nERROR!\nWPISANA WARTOSC NIE JEST LICZBĄ! SPRÓBUJ JESZCZE RAZ")
        return wartosc

    def czy_przestępny(rok):
        if (rok % 4 == 0):
            print("Tak! Podany rok jest przestępny")

        else:
            print("Podany rok nie jest przestępny")

    rok = sprawdzenie_czy_liczba()
    czy_przestępny(rok)

def Wyswietlanie_podanej_listy():

    def podawanie_listy():
        lista = []
        while True:
            element = input("Podaj element listy: ")
            lista.append(element)
            wartosc = input("Wciśnij 0 jeżeli to koniec listy, lub wciśnij dowolny klawisz jeżeli chcesz dodać kolejny element: ")
            if wartosc == '0':
                break
            else:
                continue
        return lista

    def ile_kolumn(lista):
        for indeks, i in enumerate(lista):
            x = indeks
        x = x + 1
        return x

    def najdluzszy_ciag(lista):
        x = 0
        for i in (lista):
            dlugosc = len(i)
            if x <= dlugosc:
                x = dlugosc
        return x

    def rysowanie(poziomo, dlugosc_ciagu, lista):
        if dlugosc_ciagu <= 30:
            print(poziomo * ('+' + dlugosc_ciagu * '-') + '+')
            print('|', end="")
            for i in lista:
                spacje = dlugosc_ciagu - len(i)
                print(i + ' ' * spacje + '|', end="")
            print('\n' + poziomo * ('+' + dlugosc_ciagu * '-') + '+')
        else:
            print(poziomo * ('+' + 30 * '-') + '+')
            print('|', end="")
            for ciag in lista:
                x = 0
                spacje = 30 - len(ciag)
                for i in ciag:
                    print(i, end="")
                    x = x + 1
                    if x == 27:
                        print('...', end="")
                        break
                    else:
                        continue
                print(" " * spacje, end="" + '|')
            print("\n" + poziomo * ('+' + 30 * '-') + '+')

    lista = podawanie_listy()
    dlugosc_ciagu = najdluzszy_ciag(lista)
    poziomo = ile_kolumn(lista)
    rysowanie(poziomo, dlugosc_ciagu, lista)

def Kwota_zamieniona_na_monety():
    def sprawdzenie_czy_liczba():  # Zabezpieczenie przed wpisaniem innych danych z klawiatury niż liczby
        while True:
            wartosc = input("Wprowadz kwote do rozmienienia w złotówkach: ")
            try:
                wartosc = float(wartosc)
                break
            except:
                print("\nERROR!\nWPISANA WARTOSC NIE JEST LICZBĄ! SPRÓBUJ JESZCZE RAZ")
        return wartosc

    def obliczanie_monet(grosze):
        pieciozlotowki = grosze // 500
        reszta = grosze - (pieciozlotowki * 500)
        pieciozlotowki = int(pieciozlotowki)
        dwuzlotowki = reszta // 200
        dwuzlotowki = int(dwuzlotowki)
        reszta = reszta - (dwuzlotowki * 200)
        jednozlotowki = reszta // 100
        jednozlotowki = int(jednozlotowki)
        reszta = reszta - (jednozlotowki * 100)
        piecdziesieciogroszowki = reszta // 50
        piecdziesieciogroszowki = int(piecdziesieciogroszowki)
        reszta = reszta - (piecdziesieciogroszowki * 50)
        dwudziestogroszowki = reszta // 20
        dwudziestogroszowki = int(dwudziestogroszowki)
        reszta = reszta - (dwudziestogroszowki * 20)
        dziesieciogroszowki = reszta // 10
        dziesieciogroszowki = int(dziesieciogroszowki)
        reszta = reszta - (dziesieciogroszowki * 10)
        piec_groszy = reszta // 5
        piec_groszy = int(piec_groszy)
        reszta = reszta - (piec_groszy * 5)
        dwa_grosze = reszta // 2
        dwa_grosze = int(dwa_grosze)
        reszta = reszta - (dwa_grosze * 2)
        jeden_grosz = reszta // 1
        jeden_grosz = int(jeden_grosz)
        suma_monet = pieciozlotowki + dwuzlotowki + jednozlotowki + piecdziesieciogroszowki + dwudziestogroszowki + dziesieciogroszowki + piec_groszy + dwa_grosze + jeden_grosz
        print(
            f"Kwote: {kwota} można rozdzielić na monety po: \n {pieciozlotowki} pięciozłotówek \n {dwuzlotowki} dwuzlotówek \n {jednozlotowki} jednoozłotówek \n",
            end="")
        print(
            f"{piecdziesieciogroszowki} pięćdziesięciogroszówek \n {dwudziestogroszowki} dwudziestogroszówek \n {dziesieciogroszowki} dziesięciogroszówek \n",
            end="")
        print(
            f"{piec_groszy} pięć groszy \n {dwa_grosze} dwa grosze \n {jeden_grosz} jeden grosz \n Suma monet wynosi: {suma_monet}")

    kwota = sprawdzenie_czy_liczba()
    grosze = kwota * 100  # Przeliczenie wartości podanej w złotówkach na grosze
    obliczanie_monet(grosze)

def Rysowanie_piramidy_o_zadanej_wysokosci():
    def sprawdzenie_czy_liczba():  # Zabezpieczenie przed wpisaniem innych danych z klawiatury niż liczby
        while True:
            wartosc = input("Podaj wysokość piramidy: ")
            try:
                wartosc = float(wartosc)
                break
            except:
                print("\nERROR!\nWPISANA WARTOSC NIE JEST LICZBĄ! SPRÓBUJ JESZCZE RAZ")
        return wartosc

    def rysowanie_piramidy(wysokosc):
        max_szerokosc = wysokosc * 2 - 1
        srodek = max_szerokosc // 2
        i = 0
        while i < wysokosc:
            print((srodek - i) * ' ' + i * '#' + '#' + i * '#' + (srodek - i) * ' ')
            i = i + 1

    wysokosc = sprawdzenie_czy_liczba()
    wysokosc = int(wysokosc)
    rysowanie_piramidy(wysokosc)

def Obliczanie_wieku_psa():
    def sprawdzenie_czy_liczba():  # Zabezpieczenie przed wpisaniem innych danych z klawiatury niż liczby
        while True:
            wartosc = input("Podaj ludzkie lata aby obliczyć wiek psa (większa od 1): ")
            try:
                wartosc = float(wartosc)
                break
            except:
                print("\nERROR!\nWPISANA WARTOSC NIE JEST LICZBĄ! SPRÓBUJ JESZCZE RAZ")
        return wartosc

    def obliczanie_wieku(lata):
        pozostałe = lata - 2
        pierwsze_dwa = 2 * 10.5
        reszta = pozostałe * 4
        lata_psa = pierwsze_dwa + reszta
        return lata_psa

    def wywolywanie_funkcji():
        while True:
            lata = sprawdzenie_czy_liczba()
            if (lata > 1):
                wiek_psa = obliczanie_wieku(lata)
                break
            else:
                print("WPISANA WARTOŚĆ JEST MNIEJSZA OD 1! SPRÓBUJ JESZCZE RAZ!\n")
                continue
        print(f"Pies ma {wiek_psa} lat")

    wywolywanie_funkcji()

def losowy_program():
    los = random.randint(1,15)
    return los

def wywolanie_programu(wybor):
    if wybor == 1:
        Kalkulator_pezeliczania_stopni_Celsjusza_na_Farenheita()

    elif wybor == 2:
        Kalkulator_pezeliczania_stopni_Farenheita_na_Celsjusza()

    elif wybor == 3:
        Obliczanie_pola_powierzchni_kola()

    elif wybor == 4:
        Pierwsza_i_ostatnia_cyfra_podanej_liczby()

    elif wybor == 5:
        Rysowanie_prostokata_o_podanej_wysokosci_i_szerokosci()

    elif wybor == 6:
        Przelicznik_liczb_binarnych_na_dziesietne()

    elif wybor == 7:
        Rozpoznawanie_czy_podana_liczba_jest_parzyta()

    elif wybor == 8:
        Czy_podana_liczba_jest_podzielna_przez_3_lub_5_lub_7()

    elif wybor == 9:
        Czy_podana_liczba_jest_podzielna_przez_3_i_5_i_7()

    elif wybor == 10:
        Czy_podany_rok_jest_rokeim_przestepnym()

    elif wybor == 11:
        Wyswietlanie_podanej_listy()

    elif wybor == 12:
        Kwota_zamieniona_na_monety()

    elif wybor == 13:
        Rysowanie_piramidy_o_zadanej_wysokosci()

    elif wybor == 14:
        Obliczanie_wieku_psa()

    elif wybor == 15:
        los = losowy_program()
        wywolanie_programu(los)

    elif wybor == 16:
        sys.exit(0)

def wykonywanie():
    while True:
        wybor = wybor_funkcji()
        wywolanie_programu(wybor)
        koniec = input("\nKoniec wykonywania programu: Kliknij '1' jeżeli chcesz wrócić do menu lub dowolny przycisk jeśli chcesz wyjść: ")
        if koniec == '1':
            continue
        else:
            print("Do zobaczenia!")
            break

wykonywanie()