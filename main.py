from tkinter import *
import tkinter
from datetime import datetime
import pyglet  # para poder importar fontes

pyglet.font.add_file("digital-7.ttf")  # Importar fonte

################ Cores################
cor1 = "#3d3d3d"  # preto
cor2 = "#fafcff"  # branco
cor3 = "#21c25c"  # verde
cor4 = "#eb463b"  # vermelho
cor5 = "#dedcdc"  # cinza
cor6 = "#3080f0"  # azul

fundo = cor1  # Cor do fundo
cor = cor2  # Cor da letra

janela = Tk()
janela.title("")
janela.geometry("440x180")  # Tamanho da janela
# Para não poder mudar a altura e comprimento da janela
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=cor1)


def relogio():
    tempo = datetime.now()  # Obetendo a hora do pc

    hora = tempo.strftime("%H:%M:%S")  # Obetendo hora , minutos e segundos
    dia_semana = tempo.strftime("%A")  # Obtendo o dia da semana
    dia = tempo.day
    mes = tempo.strftime("%b")  # B para o nome completo do mês
    ano = tempo.strftime("%Y")

    l1.config(text=hora)
    # para a cada 200 milecimos de segundo rexecutar o relogio
    l1.after(200, relogio)
    l2.config(text=dia_semana + " " + str(dia) +
              "/" + str(mes) + "/" + str(ano))


l1 = Label(janela, text="", font=("digital-7 80"),
           bg=fundo, fg=cor)  # Mostrar de facto a hora
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(janela, text="", font=("digital-7 20"),
           bg=fundo, fg=cor)  # Mostrar de facto a hora
l2.grid(row=1, column=0, sticky=NW, padx=5)  # row é posição

relogio()
janela.mainloop()
