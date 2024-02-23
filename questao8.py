def main_idade():
  dif_ano = ano_atual - ano_nasc
  dif_ano1 = (ano_atual - ano_nasc) - 1
  
  if mes_atual > mes_nasc:
    print(f'Sua idade é {dif_ano} ')
  elif mes_atual < mes_nasc:
    print(f'Sua idade é {dif_ano1}')
  elif dia_atual > dia_nasc:
    print(f'Sua idade é {dif_ano}')
  else:
    print(f'Sua idade é {dif_ano1}')

#---------------------

print('Sua Idade!')
print('-----------')
      
dia_atual = int(input('Digite o Dia atual: '))
mes_atual = int(input('Digite o Mês atual: '))
ano_atual = int(input('Digite o Ano atual: '))

print('-----------')
dia_nasc = int(input('Digite o Dia que vc nasceu: '))
mes_nasc = int(input('Digite o Mês que vc nasceu: '))
ano_nasc = int(input('Digite o Ano que vc nasceu: '))

print('-----------')
main_idade()
