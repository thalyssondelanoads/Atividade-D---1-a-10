def main():
  if num1 > num2:
    print(f' Maior : {num1}, Menor : {num2}')
  elif num2 > num1:
    print(f' Maior : {num2}, Menor : {num1}')
  else:
   print(f' Os números são iguais! ')

#-----------------------

print('Maior e menor número')
print('----------')

num1 = int(input('Digite o 1° Número: '))
num2 = int(input('Digite o 2° Número: '))

print('-----------')
main()
