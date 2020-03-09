print("KALKULATOR PRZELICZANIA STOPNI FARENHEITA NA CELSJUSZA \n")
farenheit = input("Wpisz stopnie Farenheita: ")
farenheit = float(farenheit)
celsjusz = (farenheit-32)/1.8
celsjusz = str(celsjusz)
farenheit = str(farenheit)
print("Wzór: (Stopnie Farenheita -32)/1.8 = Stopnie Celsjusza ")
print( "(" + farenheit + " - 32) / 1.8 = " + celsjusz )