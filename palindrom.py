'''
Dana jest pusta lista X, program najpierw pobiera od użytkownika liczbę elementów tej listy, 
a następnie za pomocą pętli for pobiera odpowiednią ilośĆ jej elementów będących liczbami całkowitymi.
Przy użyciu kolejnej pętli for program sprawdza odpowiednio i-ty element tej listy oraz element od końca odpowiadający pozycji i-tego elementu. 
Jeśli elementy te są równe, lista jest palindromiczna, jeśli nie, nie jest palindromiczna.
'''

X = []
n = int(input('Podaj ilośc elementów listy X: '))

for i in range(n):
    liczba = int(input('Podaj liczbę, która ma zawierać się w liście X: '))
    X.append(liczba)

for i in range(len(X) // 2):
    if X[i] != X[-(i+1)]:
        wynik = 'nie jest'
        print(X[i], X[-(i+1)])
        break
    else:
        wynik = 'jest'
    print(X[i], X[-(i+1)])

komunikat = 'Podana lista {} palindromiczna'

print(komunikat.format(wynik))
