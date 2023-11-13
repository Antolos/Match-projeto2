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


#bibliotecas para interface grafica e mensagem em caixa
from tkinter import *
from tkinter import messagebox

# função do botão
def gera_meta():
    
    #entradas
    meta = float(meta_entry.get().replace(",","."))
    poupa = float(poupa_entry.get().replace(",","."))
    
    #condição de erro se for negativo
    if poupa <= 0 or meta <= 0:
        #caixa de mensagem
        messagebox.showinfo(
            title = "Erro!",
            message=f"Favor insira um valor valido{meta} , {poupa}"
        )
    #condição de acerto
    else:
        
        #Processamento da divisão de meta por valor economizado por mês:
        tempo = meta / poupa + 1 if meta % poupa > 4 else meta / poupa
        tempo = int((tempo))
 
        #Saída de impressão na caixa de mensagem com anos e meses necessários para alcançar meta:
        if (tempo<12):
            messagebox.showinfo(
            title = "Resultado",
            message=f"Perfeito! Com uma meta de R${meta:,.2f} e economizando R${poupa:,.2f} por mês, o tempo de espera será de: {tempo} meses."
            )
        elif(tempo % 12 == 0):
            messagebox.showinfo(
            title = "Resultado",
            message=f"Perfeito! Com uma meta de R${meta:,.2f} e economizando R${poupa:,.2f} por mês, o tempo de espera será de: {int(tempo / 12)} anos."
            )          
        else:
            messagebox.showinfo(
            title = "Resultado",
            message=f"Perfeito! Com uma meta de R${meta:,.2f} e economizando R${poupa:,.2f} por mês, o tempo de espera será de: {int(tempo / 12)} anos e {round(tempo % 12 * 1.2)} meses."
            )

# inicialização da janela do programa
janela = Tk()
janela.title('Calculadora de Meta Financeira com Economia Mensal')
janela.geometry('540x350')
janela.config(padx=10, pady=45, background = "#008888")

# componentes da janela
#texto
meta_label = Label(text="Meta Financeira:", fg="#dddddd", font=('arial', 22,'bold'), bd=20, background = "#008888")
meta_label.grid(row=2, column=0)
#campo de texto com foco(onde começa o cursor)
meta_entry = Entry(width=31)
meta_entry.grid(row=2, column=1, columnspan=2)
meta_entry.focus()
#texto
poupa_label = Label(text="Economia Mensal:", fg="#dddddd", font=('arial', 22,'bold'), bd=20, background = "#008888")
poupa_label.grid(row=4, column=0)
#campo de texto
poupa_entry = Entry(width=31)
poupa_entry.grid(row=4, column=1, columnspan=2)
#botao com função no argumento command
botao = Button(janela,text='Calcular',command=gera_meta,  fg="#008888",font=('arial', 30,'bold'), background = "#dddddd") 
botao.grid(column=2,row=6, pady=20)
janela.mainloop()
