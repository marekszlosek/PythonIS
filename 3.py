print("KALKULATOR DO OBLICZENIA POLA POWIERZCHNI KOŁA \n")
promien = input("Wprowadz promień koła r: ")
promien = float(promien)
promien = promien**2
pole_kola = 3.14 * promien
pole_kola = str(pole_kola)
promien = str(promien)
print("Wzór: Pole koła = Pi * r^2")
print(promien + " * Pi = " + pole_kola)