from uteis import numeros


num = int(input('Digite um valor: '))
fat = numeros.factorial(num)
#fat = factorial(num)
print(f'O factorial de {num} é {fat}.')
#print(f'o dobro {num} é {dobro(num)}')
print(f'o dobro {num} é {numeros.dobro(num)}')
#print(f'O triplo {num} é {triplo(num)}')
print(f'O triplo {num} é {numeros.triplo(num)}')