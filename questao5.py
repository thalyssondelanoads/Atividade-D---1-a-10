def main():
  if num1 > num2 > num3:
    print(f' Ordem : {num3},{num2},{num1} ')
  elif num3 > num2 > num1:
    print(f' Ordem : {num1},{num2},{num3} ')
  elif num2 > num1 > num3:
    print(f' Ordem : {num1}, {num3}, {num2} ')
  elif num1 > num3 > num2:
    print(f' Ordem : {num2}, {num3}, {num1} ')
  else:
    print(f' Ordem : {num1}, {num3}, {num2} ')
   
#-------------------

print('3 Números em Ordem Crescente')
print('-------------')

num1 = int(input('Digite o 1º Número: '))
num2 = int(input('Digite o 2º Número: '))
num3 = int(input('Digite o 3º Número: '))

print('-------------')
main()
