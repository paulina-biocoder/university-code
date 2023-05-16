'''Program pobiera od użytkownika słowo, następnie zamienia je na małe litery, potem sprawdza długość tekstu i oblicza połowę tej długości.
Potem za pomocą pętli sprawdzamy, czy znak pozycji w tekście nie jest równy długości - pozycja znaku - 1.
Jeśli nie są sobie równe - wyraz nie jest palindromem, funkcją break kończymy działanie pętli i następnie program wypisuje czy słowo jest palindromem, czy nie'''

tekst = input('Podaj tekst: ')
tekst = tekst.lower() 
dlugosc = len(teskt)
polowa_dlugosci = dlugosc // 2 

palindrom = True
for i in range(polowa_dlugosci):
    if tekst[i] != tekst[dlugosc - i - 1]:
        palindrom = False
        break

if palindrom:
    print('Podany tekst jest palindromem.')
else:
    print('Podany tekst nie jest palindromem.')
