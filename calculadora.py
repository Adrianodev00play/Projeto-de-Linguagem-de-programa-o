import tkinter as tk
import os
from datetime import datetime
import customtkinter as ctk

#função que apaga todo o conteúdo do arquivo de registro
def apagar_historico():
    with open("Registros.txt", "w") as arquivo:
        arquivo.write("")
    nome.config(text="Historico apagado")

#função que adiciona um registro de operação ao arquivo de registro
def registrar():
    if log:
        with open("Registros.txt", "a") as arquivo:
            for item in log:
                arquivo.write(item + "\n")
        log.clear()

#função que cria a janela de exibição do historico
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

    wid=79
    hei=86
    #preenche um grid de 4x4, como se fosse uma matriz
    for linha in range(4):
        b=ctk.CTkButton(layout_botoes, text=vetor_char[i], font=("Arial", 40), width=wid, height=hei, command=lambda i=i:mudar(vetor_char[i]), fg_color="#9191A0")
        b.grid(row=linha, column=0, padx=3, pady=3)
        for coluna in range(1, 4):

            #faz a verificação na hora de criar o botão de "C"
            if linha==3 and coluna==2:
                i+=1
                b=ctk.CTkButton(layout_botoes, text="C", font=("Arial", 40), width=wid, height=hei, command=lambda: nome.config(text=""), fg_color="#9191A0")
                b.grid(row=linha, column=coluna,padx=3, pady=3)

            #faz a verificação na hora de criar o botão de "="    
            elif linha==3 and coluna==3:
                i+=1
                b=ctk.CTkButton(layout_botoes, text="=", width=wid, height=hei, font=("Arial", 40), command=resultado, fg_color="#9191A0")
                b.grid(row=linha, column=coluna,padx=3, pady=3)
            else:
                i+=1
                b=ctk.CTkButton(layout_botoes, text=vetor_char[i], width=wid, font=("Arial", 40), height=hei, command=lambda i=i:mudar(vetor_char[i]), fg_color="#9191A0")
                b.grid(row=linha, column=coluna,padx=3, pady=3)
        i+=1

#função que verifica se o resultado é diferente de vazio, se for, pega o numero de resultado e a função eval pega a expressão em string e converte em numérico, depois transforma em string novamente para poder exibir, també extrai a data e hora real 
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
app.config(bg="#171717")
app.resizable(False, False)

#criação do visor
visor=tk.Frame(app, width=340, height=130, bg="#addbf2")
visor.grid(row=0, column=0, padx=20, pady=10)
nome=tk.Label(visor, text="", font=("Arial", 20), fg="black", bg="#addbf2")
nome.place(relx=1.0, rely=1.0, x=-5, y=-5, anchor="se")
visor.grid_propagate(False)

#criação do layout dos botões
layout_botoes=tk.Frame(app, width=340, height=370, bg="#171717")
layout_botoes.grid(row=1, column=0)
layout_botoes.grid_propagate(False)

#vetor que armazena os caracteres
vetor_char=['7', '8', '9', '*', '4', '5', '6', '-', '1', '2', '3', '+', '0', '/', 'C', '=']

#vetor que armazena os registros
log=[]

#chama a função de criar botões
criar_botoes()
app.mainloop()
