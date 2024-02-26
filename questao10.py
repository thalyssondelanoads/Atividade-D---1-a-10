def validar_data(ano,mes,dia):
    if dia < 1 or dia > 31:
        print('Data Inválida')
    elif mes < 1 or mes > 12:
        print('Data Inválida')
    elif dia > 30 and mes == 4 or mes == 6 or mes == 9 or mes == 11:
        print('Data Inválida')
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        ... # CONTUINAR DPS
#--------------------

print('Validar Data!')
print('---------------')

dia = int(input('Digite o Dia: '))
mes = int(input('Digite o Mês: '))
ano = int(input('Digite o Ano: '))

print('---------------')
validar_data(ano,mes,dia)
