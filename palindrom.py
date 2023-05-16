tekst = input("Podaj tekst: ")
dlugosc = len(tekst)
polowa_dlugosci = dlugosc // 2  # Obliczenie połowy długości tekstu

palindrom = True
for i in range(polowa_dlugosci):
    if tekst[i] != tekst[dlugosc - i - 1]:
        palindrom = False
        break

if palindrom:
    print("Podany tekst jest palindromem.")
else:
    print("Podany tekst nie jest palindromem.")