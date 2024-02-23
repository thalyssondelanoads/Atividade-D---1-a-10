def main():
  if angulo1 + angulo2 + angulo3 != 180:
    print('NÃO é um Triângulo!')
  elif angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
    print('O Triângulo é Acutângulo!')
  elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
     print('O Triângulo é Retângulo!')
  elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
   print('O Triângulo é Obtusângulo!')

#--------------------

print('Indentificar e Classificar Triângulos')
print('---------')

angulo1 = int(input('Digite o 1º Ângulo: '))
angulo2 = int(input('Digite o 2º Ângulo: '))
angulo3 = int(input('Digite o 3º Ângulo: '))

print('---------')
main()      
