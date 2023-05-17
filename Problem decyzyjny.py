#Program ma za zadanie pobrać od użytkownika trzy dowolne liczby, a następnie sprawdzić, czy druga liczba mieści się pomiędzy pierwszą, a trzecią.

a = input('Podaj pierwszą liczbę: ')
b = input('Podaj drugą liczbę: ')
c = input('Podaj trzecią liczbę: ')

print('Druga liczba leży między pierwszą a trzecią?')

if a < b < c:
 print('Tak')
else: 
 print('Nie')
