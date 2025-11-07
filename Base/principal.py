import tkinter as tk
from tkinter import colorchooser
#import tkinter
#import mido
import sqlite3
#from tkinter import messagebox

# Variaveis Globais
global gbg, gbgbt, gbgmt, conn, cursor, gfg

# Conecta Banco
def conecta():
    global conn, cursor
    conn = sqlite3.connect('./conf/menu.db')
    cursor = conn.cursor()

# Desconecta Banco
def desconecta():
    global conn
    conn.close()

# Definicao Temas
gbg="gray30"
gbgbt="khaki4"
gbgmt="aquamarine2"
#gbgbtplay="aquamarine2"
#gbgbtpause="aquamarine2"


def esc_color():
    xpaleta = colorchooser.askcolor(title="Escolha uma cor")
    if xpaleta[1]:
        gbg=xpaleta[1]
        root.config(bg=gbg)
        tit_tema.config(bg=gbg)
        id_tema.config(bg=gbg)
        id_tema2.config(bg=gbg)
        listatemas.config(bg=gbg)
        root.update()
        tit_tema.update()
        id_tema.update()
        id_tema2.update()
        listatemas.update()
        



def pref():
    pass

def tema():
    global tit_tema, id_tema, listatemas, id_tema2
    ### Titulo
    tit_tema = tk.Label(root,text="TEMAS",bg=gbg,fg=gfg,font=["Courier",24,"bold"])
    tit_tema.place(x=30,y=20)

    ###Mostra tema atual
    id_tema = tk.Label(root,text=f'Ativo:',bg=gbg,fg=gfg,font=["Courier", 18,"bold"])
    id_tema.place(x=30,y=50)
    id_tema2 = tk.Label(root,text=f'{gconf_tema[0]} - {gconf_tema[1]}',bg=gbg,fg=gfg,font=["Courier", 18])
    id_tema2.place(x=150,y=50)


    ### ListBox Trocar Tema para Trocar tema 
    conecta() # Conecta Banco para Configuraçoes
    cursor.execute(f"SELECT id,nome FROM tema") # Busca Informacoes Tema
    xlistboxtema = cursor.fetchall()
    listatemas = tk.Listbox(root,width=50,height=5,bg=gbgbt,fg=gfg)
    listatemas.place(x=150,y=100)

    for temas in xlistboxtema:
        listatemas.insert(tk.END,temas)

    desconecta()

    bt_trocatema = tk.Button(root,text="Trocar",bg=gbgmt,fg=gfg)
    bt_trocatema.place(x=30,y=100)

    xc = esc_color()
    
    
    pass

    """
    def escolher_cor():
    # Retorna uma tupla: ((r, g, b), hexadecimal)
    cor_escolhida = colorchooser.askcolor(title="Escolher Cor")
    if cor_escolhida[1]: # Verifica se uma cor foi selecionada
        print(f"Cor hexadecimal selecionada: {cor_escolhida[1]}")
        label_seletor.config(bg=cor_escolhida[1])

    root_chooser = tk.Tk()
    label_seletor = tk.Label(root_chooser, text="Cor do Seletor", width=20, height=5)
    label_seletor.pack(pady=10)

    botao_cor = tk.Button(root_chooser, text="Abrir Seletor de Cores", command=escolher_cor)
    botao_cor.pack(pady=10)

    root_chooser.mainloop()
    """

def versao():
    global root
    janelaversao = tk.Toplevel(root)
    janelaversao.title("Versão")
    janelaversao.geometry("150x150")
    janelaversao.transient(root)
    #janelaversao.grab_set()

    janelaversaoframe = tk.Frame(janelaversao)
    janelaversaoframe.pack()

    janelaversaotexto = tk.Label(janelaversaoframe,text="Versão: 0.0.1")
    janelaversaotexto.pack(pady=20)

    janelaversaobotao = tk.Button(janelaversao,text="OK", command=janelaversao.destroy)
    janelaversaobotao.pack(pady=30)

    root.wait_window(janelaversao)

# Clicar Botao Direito
def bt_dir(event):
    xbotdir = versao()
    
# Funcao Criar Menu Principal
def criar_gui():
    global root
    # Cria Janela
    root = tk.Tk()
    largura = root.winfo_screenwidth()              
    altura = root.winfo_screenheight()              
    root.geometry("%dx%d" % (largura, altura))
    #root.geometry("800x600") # Tamanho Janela
    #root.attributes('-fullscreen', True)
    root.title(f'{gtitulo}') # Titulo Janela
    #root.title("Base && Nome Aplicativo") # Titulo Janela
    root.bind("<Escape>", quit) # Comportamento ao Teclar ESC
    root.bind("<Button-3>", bt_dir) # Comportamento ao Clicar Botao Direito
    root.config(bg=gbg) # Configurações fundo

    # Conecta Banco
    conn = sqlite3.connect('./conf/menu.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM menu order by col_menu, pos_menu")
    rows = cursor.fetchall()
    conn.close()


    # Cria Menu Principal
    menubar = tk.Menu(root)
    menubar.config(bg=gbgbt)
    root.config(menu=menubar)


    # Cria Lista Menu Base
    for row in rows:
        if row[3] == 0:
            mp = f'{row[4]} = tk.Menu(menubar, tearoff=0)' # tearoff=0 remove a linha pontilhada que permite "desligar" o menu
            exec(mp)
            x = f'menubar.add_cascade(label="{row[0]}", menu={row[4]})'
            exec(x)
        else:
            mm = f'{row[4]}.add_command(label="{row[0]}", command={row[1]})'
            exec(mm)
            

    root.config(menu=menubar)

    root.mainloop()


if __name__ == "__main__":
    conecta() # Conecta Banco para Configuraçoes
    cursor.execute("SELECT * FROM configura") # Busca Informações
    gconfs = cursor.fetchone()
    
    gtema = gconfs[0] # Define Tema
    gtitulo = gconfs[1] # Define Titulo Aplicativo

    
    cursor.execute(f"SELECT * FROM tema WHERE id = { gtema }") # Busca Informacoes Tema
    gconf_tema = cursor.fetchone()


    #### Define Cores
    gbg=gconf_tema[2]
    gbgbt=gconf_tema[3]
    gbgmt=gconf_tema[4]
    gfg =gconf_tema[5]

    ### Desconecta SQL Lite
    desconecta()

    ### Chama Principal
    criar_gui()

