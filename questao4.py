def main():
  if dez == uni:
    print(' A Dezena e a Unidade são iguais! ')
  else:
    print(' A Dezena e a Unidade são diferentes! ')
    
#------------------

print('Dezena e Unidade =/≠ ')
print('-------')

num = int(input('Digite o Número ( 2 dígitos ) : '))

dez = num // 10
uni = num % 10

print('--------')
main()
