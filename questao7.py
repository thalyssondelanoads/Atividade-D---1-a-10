def main():
  if (lado1 + lado2) < lado3 or (lado1 + lado3) < lado2 or (lado2 + lado3) < lado1: 
    print('NÃO é um Triângulo')
  elif lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
    print('É um Triângulo Equilátero')
  elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('É um Triângulo Isósceles')
  else:
    print('É um Triângulo Escaleno')
    
#--------------------

print('Identificar e Definir um Triângulo')
print('-------------')

lado1 = int(input('Digite o valor do 1º lado: '))
lado2 = int(input('Digite o valor do 2º lado: '))
lado3 = int(input('Digite o valor do 3º lado: '))

print('-------------')
main()
