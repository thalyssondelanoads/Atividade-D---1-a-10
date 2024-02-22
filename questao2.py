def main():
    print(f' Maior : {num1}, Menor : {num2}')

def main_2():
    print(f' Maior : {num2}, Menor : {num1}')

#-----------------------

print('Maior e menor número')
print('----------')

num1 = int(input('Digite o 1° Número: '))
num2 = int(input('Digite o 2° Número: '))

print('-----------')
if num1 > num2:
    main()
elif num2 > num1:
    main_2()
else:
    print(f' Os números são iguais! ')
