import tkinter as tk
import os
from datetime import datetime
import customtkinter as ctk

def apagar_historico():
    with open("Registros.txt", "w") as arquivo:
        arquivo.write("")
    nome.config(text="Historico apagado")

def registrar():
    if log:
        with open("Registros.txt", "a") as arquivo:
            for item in log:
                arquivo.write(item + "\n")
        log.clear()

def historico():
    nome.config(text="Histórico aberto")
    teste=tk.Toplevel()
    teste.geometry("300x300")
    frame = ctk.CTkScrollableFrame(teste, fg_color="white")
    frame.pack(fill="both", expand=True)
    with open("Registros.txt", "r") as arquivo:
        for i, linha in enumerate(arquivo):
            letra = tk.Label(frame, text=linha, bg="white", wraplength=250, justify="left")
            letra.grid(row=i, column=0, sticky="nsew")

            
#função que cria os botoes e verifica se o botão criado é o botão "C" ou o botão "=", para diferenciar a função deles dos outros botões
def criar_botoes():
    i=0
    #preenche um grid de 4x4, como se fosse uma matriz
    for linha in range(4):
        b=tk.Button(layout_botoes, text=vetor_char[i], width=10, height=5, command=lambda i=i:mudar(vetor_char[i]), bg="#9191A0")
        b.grid(row=linha, column=0, padx=3, pady=3)
        for coluna in range(1, 4):

            #faz a verificação na hora de criar o botão de "C"
            if linha==3 and coluna==2:
                i+=1
                b=tk.Button(layout_botoes, text="C", width=10, height=5, command=lambda: nome.config(text=""), bg="#9191A0")
                b.grid(row=linha, column=coluna,padx=3, pady=3)

            #faz a verificação na hora de criar o botão de "="    
            elif linha==3 and coluna==3:
                i+=1
                b=tk.Button(layout_botoes, text="=", width=10, height=5, command=resultado, bg="#9191A0")
                b.grid(row=linha, column=coluna,padx=3, pady=3)
            else:
                i+=1
                b=tk.Button(layout_botoes, text=vetor_char[i], width=10, height=5, command=lambda i=i:mudar(vetor_char[i]), bg="#9191A0")
                b.grid(row=linha, column=coluna,padx=3, pady=3)
        i+=1

#função que verifica se o resultado é diferente de vazio, se for, pega o numero de resultado e a função eval pega a expressão em string e converte em numérico, depois transforma em string novamente para poder exibir
def resultado():
    if nome["text"]=="77//":
        historico()
    elif nome["text"]=="55**":
        apagar_historico()
    else:
        nome_antigo=nome["text"]
        resultado=eval(nome["text"])
        if nome_antigo!="":
            nome.config(text=str(resultado))
            tudo=datetime.now()
            data = tudo.strftime("%d/%m/%Y")
            hora = tudo.strftime("%H:%M")
            log.append(f"Em {data}, as {hora}, o usuario fez a seguinte operacao: {nome_antigo} e o resultado foi: {str(resultado)}")
            registrar()

#função que apaga o resultado na tela
def apagar():
    nome.config(text="")

#funçao que concatena o texto na tela
def mudar(texto):
    nome.config(text=nome["text"]+texto)

#==escopo principal==

#criação da janela da calculdaora
app=tk.Tk()
x=(app.winfo_screenwidth()//2)-(380//2)
y=(app.winfo_screenheight()//2)-(525//2)
app.geometry(f"{380}x{525}+{x}+{y}")
app.config(bg="#1b1b27")
app.resizable(False, False)

#criação do visor
visor=tk.Frame(app, width=340, height=130, bg="#383849")
visor.grid(row=0, column=0, padx=20, pady=10)
nome=tk.Label(visor, text="", font=("Arial", 20), fg="white", bg="#383849")
nome.place(relx=1.0, rely=1.0, x=-5, y=-5, anchor="se")
visor.grid_propagate(False)

#criação do layout dos botões
layout_botoes=tk.Frame(app, width=340, height=370, bg="#1b1b27")
layout_botoes.grid(row=1, column=0)
layout_botoes.grid_propagate(False)

#vetor que armazena os caracteres
vetor_char=['7', '8', '9', '*', '4', '5', '6', '-', '1', '2', '3', '+', '0', '/', 'C', '=']

#vetor que armazena os registros
log=[]

#chama a função de criar botões
criar_botoes()
app.mainloop()

for a in log:
    print(a)