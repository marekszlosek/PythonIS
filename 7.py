wartosc = input("Podaj liczbe: ")
wartosc = int(wartosc)
parzysta = wartosc % 2 #Warunek podzielności przez 2
wartosc = str(wartosc)
if(parzysta == 0):
    print("Liczba " + wartosc + " jest parzysta!")
else:
    print("Liczba " + wartosc + " jest nie parzysta!")