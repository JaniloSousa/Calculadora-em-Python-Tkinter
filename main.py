# Janilo Paixão de Sousa
# fazendo as importações necessárias para esse projeto
from tkinter import *

# cores que uso no projeto
azul = '#3574a1'
cinza = '#bababa'
roxo = '#5b468c'

# criando e configurando minha janela principal
janela = Tk()
janela.geometry('235x310+1250+200')
janela.title('Calculadora')
janela.resizable(False, False)
janela.iconphoto(False, PhotoImage(file='icon_calculator.png'))

# função para digitar um novo caracter no visor
expressao = ''
def excluirUltimoCaracter():
    global expressao
    nova_expressao = expressao[0:-1]
    limparVisor()
    variavel_visor.set(nova_expressao)
    expressao = nova_expressao

def entrarValor(novo_caracter):
    global expressao
    expressao = expressao + novo_caracter
    variavel_visor.set(expressao)

# função para limpar totalmente o visor
def limparVisor():
    global expressao
    expressao = ''
    variavel_visor.set('')

# função para calcular toda a expressão que está no visor
def calcular():
    global expressao
    resultado = eval(str(expressao)) # função que pega uma expressão matemática em formato de string e calcula o resultado
    limparVisor()
    variavel_visor.set(resultado)

# dividindo a janela em dois frames
# frame aonde vai aparecer a expressão
frame_visor = Frame(janela, width=235, height=50)
frame_visor.grid(row=0, column=0)

# frame aonde vai ficar os botões das operações matemáticas
frame_botoes = Frame(janela, width=235, height=268)
frame_botoes.grid(row=1, column=0)

# TRABALHANDO NO FRAME DA TELA
variavel_visor = StringVar()
lb_visor = Label(frame_visor, width=16, height=2, relief='flat', font=('Ivy 18'), bg=roxo, fg='white', textvariable=variavel_visor, anchor='e', padx=7)
lb_visor.pack()

# TRABALHANDO NO FRAME DOS BOTÕES -------------------------------------------------------------------------------------------
# BOTÕES ESPECIAS (C, %, /) -> linha 0
button_1 = Button(frame_botoes, command= limparVisor, text='C', width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', fg='white')
button_1.grid(row=0, column=0)

button_2 = Button(frame_botoes, command= excluirUltimoCaracter, text='←', width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', fg='black')
button_2.grid(row=0, column=1)

button_3 = Button(frame_botoes, command= lambda: entrarValor('%'), text='%', width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', fg='white')
button_3.grid(row=0, column=2)

button_4 = Button(frame_botoes, command= lambda: entrarValor('/'), text='/', width=5, height=2, bg=azul, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', fg='white')
button_4.grid(row=0, column=3)


# BOTÕES DOS NÚMEROS (7, 8, 9, *) -> linha 1
button_5 = Button(frame_botoes, command= lambda: entrarValor('7'), text='7', width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', fg='white')
button_5.grid(row=1, column=0)

button_6 = Button(frame_botoes, command= lambda: entrarValor('8'), text='8', width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', fg='white')
button_6.grid(row=1, column=1)

button_7 = Button(frame_botoes, command= lambda: entrarValor('9'), text='9', width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', fg='white')
button_7.grid(row=1, column=2)

button_8 = Button(frame_botoes, command= lambda: entrarValor('*'), text='*', width=5, height=2, bg=azul, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', fg='white')
button_8.grid(row=1, column=3)


# BOTÕES DOS NÚMEROS (4, 5, 6, -) -> linha 2
button_9 = Button(frame_botoes, command= lambda: entrarValor('4'), text='4', width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', fg='white')
button_9.grid(row=2, column=0)

button_10 = Button(frame_botoes, command= lambda: entrarValor('5'), text='5', width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', fg='white')
button_10.grid(row=2, column=1)

button_11 = Button(frame_botoes, command= lambda: entrarValor('6'), text='6', width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', fg='white')
button_11.grid(row=2, column=2)

button_12 = Button(frame_botoes, command= lambda: entrarValor('-'), text='-', width=5, height=2, bg=azul, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', fg='white')
button_12.grid(row=2, column=3)


# BOTÕES DOS NÚMEROS (1, 2, 3, +) -> linha 3
button_13 = Button(frame_botoes, command= lambda: entrarValor('1'), text='1', width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', fg='white')
button_13.grid(row=3, column=0)

button_14 = Button(frame_botoes, command= lambda: entrarValor('2'), text='2', width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', fg='white')
button_14.grid(row=3, column=1)

button_15 = Button(frame_botoes, command= lambda: entrarValor('3'), text='3', width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', fg='white')
button_15.grid(row=3, column=2)

button_16 = Button(frame_botoes, command= lambda: entrarValor('+'), text='+', width=5, height=2, bg=azul, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', fg='white')
button_16.grid(row=3, column=3)


# BOTÕES ESPECIAIS (0, ., =) -> linha 4
button_17 = Button(frame_botoes, command= lambda: entrarValor('0'),text='0', width=11, height=2, bg=cinza, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', fg='white')
button_17.grid(row=4, column=0, columnspan=2)

button_18 = Button(frame_botoes, command= lambda: entrarValor('.'), text='.', width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', fg='white')
button_18.grid(row=4, column=2)

button_19 = Button(frame_botoes, command = calcular, text='=', width=5, height=2, bg=azul, font=('Ivy 13 bold'), relief='raised', overrelief='ridge', fg='white')
button_19.grid(row=4, column=3)


janela.mainloop()