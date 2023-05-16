a = int(input('Podaj liczbę a: '))

print('Sprawdzam, czy liczba jest liczbą pierwszą')

k = 0
while k % a == 0 and k % 1 == 0:
 print('Podana liczba jest liczbą pierwszą')
 k = a + 1 
 k == a