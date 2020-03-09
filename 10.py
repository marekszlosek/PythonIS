rok = input("Podaj rok: ")
rok = int(rok)
czy_przestepny = rok % 4

if(czy_przestepny == 0):
    print("Tak! Podany rok jest przestępny")

else:
    print("Podany rok nie jest przestępny")