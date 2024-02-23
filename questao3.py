def main():
    if num1 == num2 == num3:
        print(' Números Iguais! ')
    elif num1 > num2 and num1 > num3:
        print(f' Maior : {num1} ')
    elif num2 > num1 and num2 > num3 :
        print(f' Maior : {num2} ')
    elif num3 > num1 and num3 > num2:
        print(f' Maior : {num3} ')

#-------------------

print('Número Maior em 3 Números')
print('------------')

num1 = int(input('Digite o 1º Número: '))
num2 = int(input('Digite o 2º Número: '))
num3 = int(input('Digite o 3º Número: '))

print('-------------')
main()
