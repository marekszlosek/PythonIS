liczba = input("Podaj liczbe (Max 9 cyfr): ")
liczba = int(liczba)

#Podzielność przez 3
przez_3 = liczba % 3

#Podzielna przez 5
przez_5 = liczba % 5

#Podzielna przez 7
przez_7 = liczba % 7

if(przez_3 == 0 and przez_5 == 0 and przez_7 == 0):
    print("Podana liczba jest podzielna przez 3 i 5 i 7")

else:
    print("Podana liczba nie jest podzielna przez 3 i 5 i 7")