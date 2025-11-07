import tkinter as tk
import tkinter
import mido
import sqlite3
from tkinter import messagebox

# Variaveis Globais
global gbg, gbgbt, gbgmt

# Definicao Temas
gbg="gray30"
gbgbt="khaki4"
gbgmt="aquamarine2"
gbgbtplay="aquamarine2"
gbgbtpause="aquamarine2"


def pref():
    pass

def tema():
    pass

def versao():
    global root
    janelaversao = tk.Toplevel(root)
    janelaversao.title("Versão")
    janelaversao.geometry("150x150")
    janelaversao.transient(root)
    janelaversao.grab_set()

    janelaversaoframe = tk.Frame(janelaversao)
    janelaversaoframe.pack()

    janelaversaotexto = tk.Label(janelaversaoframe,text="Versão: 0.0.1")
    janelaversaotexto.pack(pady=20)

    janelaversaobotao = tk.Button(janelaversao,text="OK", command=janelaversao.destroy)
    janelaversaobotao.pack(pady=30)

    root.wait_window(janelaversao)
    #messagebox.showinfo("Versão:", "0.0.1 Beta")



# Funcao Criar Menu Principal
def criar_gui():
    global root
    # Cria Janela
    root = tk.Tk()
    root.geometry("800x600") # Tamanho Janela
    root.title("Controlador KFX CR9") # Titulo Janela
    root.bind("<Escape>", quit) # Comportamento ao Teclar ESC
    root.config(bg=gbg) # Configurações fundo

    # Conecta Banco
    conn = sqlite3.connect('./conf/menu.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM menu order by col_menu, pos_menu")
    rows = cursor.fetchall()


    # Cria Menu Principal
    menubar = tk.Menu(root)
    menubar.config(bg=gbgbt)
    root.config(menu=menubar)


    # Criar Lista Menu Secundarios
    #cursor.execute("SELECT * FROM menu where pos_menu != 0 order by col_menu, pos_menu")
    #rows = cursor.fetchall()
    #print(rows)

    #for imen in rows:
    #    i = 0
    #   file_menu = tk.Menu(menubar, tearoff=0) # tearoff=0 remove a linha pontilhada que permite "desligar" o menu
    #    file_menu.add_command(label=imen, menu=file_menu)

    #file_menu = tk.Menu(menubar, tearoff=0) # tearoff=0 remove a linha pontilhada que permite "desligar" o menu

    # Cria Lista Menu BaseException
    for row in rows:
        if row[3] == 0:
            mp = f'{row[4]} = tk.Menu(menubar, tearoff=0)' # tearoff=0 remove a linha pontilhada que permite "desligar" o menu
            print(mp)
            exec(mp)
            #print(f'{row[4]} = tk.Menu(menubar, tearoff=0)')
            x = f'menubar.add_cascade(label="{row[0]}", menu={row[4]})'
            exec(x)
            print(x)
        #    print(row[4])
        else:
            mm = f'{row[4]}.add_command(label="{row[0]}", command={row[1]})'
            exec(mm)
            print(mm)
            #print(row)
            #print(f'{row[4]}.add_command(label="Texto")')
            #f'{row[4]}.add_command(label="Texto")'


    root.config(menu=menubar)











    root.mainloop()


if __name__ == "__main__":
    criar_gui()

