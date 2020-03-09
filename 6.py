liczba_binarna = input("Podaj liczbe binarną (6 znaków): ")
liczba_1 = int(liczba_binarna[-1]) * 2
liczba_2 = int(liczba_binarna[-2]) * 2
liczba_3 = int(liczba_binarna[-3]) * 2
liczba_4 = int(liczba_binarna[-4]) * 2
liczba_5 = int(liczba_binarna[-5]) * 2
liczba_6 = int(liczba_binarna[-6]) * 2
liczba_dziesietna = liczba_6**5 + liczba_5**4 + liczba_4**3 + liczba_3**2 + liczba_2**1 + liczba_1**0
liczba_dziesietna = str(liczba_dziesietna)
print("Liczba dziesietna: " + liczba_dziesietna)