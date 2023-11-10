


#Projeto 6: Calculadora de Meta Financeira com Economia Mensal
#Neste projeto, os alunos criarão uma calculadora em Python que permitirá aos usuários definirem uma meta financeira e calcular quanto tempo levará para atingi-la, com base em uma economia mensal definida. A aplicação seguirá as seguintes etapas:

#Definição da Meta Financeira:
#Os usuários inserirão o valor da meta financeira que desejam atingir. Isso pode ser uma economia para uma viagem, compra importante ou qualquer objetivo financeiro.
#Definição da Economia Mensal:
#Os usuários fornecerão o valor que podem economizar mensalmente para alcançar sua meta. Isso ajudará a calcular o tempo necessário para atingir a meta.
#Cálculo do Tempo Necessário:
#A aplicação calculará o número de meses necessários para atingir a meta financeira com base na economia mensal e no valor da meta.
#Apresentação dos Resultados:
#A aplicação exibirá o tempo estimado para atingir a meta financeira com base nas informações fornecidas pelos usuários.


#Entrada do valor da meta:
valorMeta = float(input("Qual sua meta? "))

#Entrada do valor economizado por mês:
depositoMensal = float(input("Quanto pode poupar por mes? "))

#Processamento da divisão de meta por valor economizado por mês:
if(valorMeta % depositoMensal > 4):
  tempo = valorMeta / depositoMensal + 1
else:
  tempo = valorMeta / depositoMensal
tempo = int((tempo))

#Saída de impressão na tela com anos e meses necessários para alcançar meta:
print(f"Olá! Com uma meta de R${valorMeta:,.2f} e economizando R${depositoMensal:,.2f} por mês, o tempo de espera será de: ")
if (tempo<12):
  print(f"{tempo} meses.")
elif(tempo % 12 == 0):
  print(f"{int(tempo / 12)} anos.")
else:
  print(f"{int(tempo / 12)} anos e {round(tempo % 12 * 1.2)} meses.")
