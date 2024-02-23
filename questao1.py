def main():
    if num1 == num2 == num3:
        print(' 3 Números Iguais! ')
    elif num1 == num2:
        print(' 2 Números Iguais! ')
    elif num1 == num3:
        print(' 2 Números Iguais! ')
    elif num3 == num2:
        print(' 2 Números Iguais! ')
    else:
        print(' Nenhum número igual! ')
    
#-------------------

print('Números Iguais em 3 Números')
print('------------')

num1 = int(input('Digite o 1º Número: '))
num2 = int(input('Digite o 2º Número: '))
num3 = int(input('Digite o 3º Número: '))

print('-------------')
main()
