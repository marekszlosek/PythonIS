wysokosc = input("Podaj wysokosc prostokata (W przypadku podania liczby zmiennoprzecinkowej, będzie ona zaokrąglona w dół): ")
wysokosc = float(wysokosc)
wysokosc = wysokosc // 1
wysokosc = int(wysokosc)
szerokosc = input("Podaj szerokość prostokata (W przypadku podania liczby zmiennoprzecinkowej, będzie ona zaokrąglona w dół): ")
szerokosc = float(szerokosc)
szerokosc = szerokosc // 1
szerokosc = int(szerokosc)
kreska_pozioma = '-'
kreska_pionowa = '|'
print("+" + kreska_pozioma*szerokosc + "+")
print(wysokosc*("|" + " "*szerokosc + "|\n") + "+" + kreska_pozioma*szerokosc + "+")