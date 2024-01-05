import tkinter as tk
from tkinter import ttk, Label, Canvas
import datetime

cor1 = "#3d3d3d"  # preta
cor2 = "#fafcff"  # branca
cor3 = "#808080"  # cinza

# Função para atualizar o relógio
def update_relogio():
    tempo = datetime.datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b")
    ano = tempo.strftime("%Y")

    label_relogio_hora.config(text=hora)
    label_relogio_data.config(text=dia_semana + "  "
                              + str(dia) + "/" + str(mes) + "/" + str(ano))
    label_relogio_hora.after(200, update_relogio)

# Funções para controlar o cronômetro
def iniciar_cronometro():
    def cronometro():
        if cronometro_ligado:
            tempo_atual = datetime.datetime.now()
            diferenca = tempo_atual - tempo_inicial
            tempo_texto = str(diferenca).split(".")[0]
            cronometro_label.config(text=tempo_texto)
            cronometro_label.after(200, cronometro)

    global cronometro_ligado, tempo_inicial
    cronometro_ligado = True
    tempo_inicial = datetime.datetime.now()
    cronometro()

def parar_cronometro():
    global cronometro_ligado
    cronometro_ligado = False

def reiniciar_cronometro():
    global tempo_inicial
    tempo_inicial = datetime.datetime.now()
    cronometro_label.config(text="00:00:00")

# Função para alternar entre as janelas
def alternar_janela(janela_atual):
    if janela_atual == "relogio":
        janela_cronometro.withdraw()
        janela_relogio.deiconify()
    else:
        janela_relogio.withdraw()
        janela_cronometro.deiconify()

# Criar janelas principais
janela_relogio = tk.Tk()
janela_relogio.title("Relógio")
janela_relogio.geometry("440x220")
janela_relogio.resizable(width=False, height=False)
janela_relogio.configure(bg=cor1)


janela_cronometro = tk.Tk()
janela_cronometro.title("Cronômetro")
janela_cronometro.geometry("440x220")
janela_cronometro.resizable(width=False, height=False)
janela_cronometro.configure(bg=cor1)
janela_cronometro.withdraw()

# Criar frames para o relógio
frame_relogio = tk.Frame(janela_relogio, bg=cor1)
frame_relogio.grid(row=0, column=0, padx=10)

# Widgets para o relógio
label_relogio_hora = Label(frame_relogio, text="", font=("digital-7", 90), bg=cor1, fg=cor2)
label_relogio_hora.grid(row=0, column=0, sticky=tk.NW, padx=50)

label_relogio_data = Label(frame_relogio, text="", font=("digital-7", 20), bg=cor1, fg=cor2)
label_relogio_data.grid(row=1, column=0, sticky=tk.NW, padx=90)

# Iniciar a atualização do relógio
update_relogio()


button_cronometro = ttk.Button(janela_relogio, text="Cronômetro", command=lambda: alternar_janela("cronometro"))
button_cronometro.grid(row=3, column=0, sticky=tk.NW , padx=20, pady=10)

# Criar frames para o cronômetro
frame_cronometro = tk.Frame(janela_cronometro, bg=cor1)
frame_cronometro.grid(row=0, column=0, padx=10, pady=20)

# Widgets para o cronômetro
start_button = ttk.Button(frame_cronometro, text="Iniciar Cronômetro", command=iniciar_cronometro)
start_button.grid(row=0, column=0, padx=10, pady=5)

stop_button = ttk.Button(frame_cronometro, text="Parar Cronômetro", command=parar_cronometro)
stop_button.grid(row=0, column=1, padx=10, pady=5)

reset_button = ttk.Button(frame_cronometro, text="Reiniciar Cronômetro", command=reiniciar_cronometro)
reset_button.grid(row=0, column=2, padx=10, pady=5)

cronometro_label = Label(frame_cronometro, text="00:00:00", font=("digital-7", 50), bg=cor1, fg=cor2)
cronometro_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Botão para alternar para o relógio
button_relogio = ttk.Button(janela_cronometro, text="Relógio", command=lambda: alternar_janela("relogio"))
button_relogio.grid(row=2, column=0, pady=0)

janela_relogio.mainloop()



