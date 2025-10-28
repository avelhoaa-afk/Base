import tkinter as tk
import tkinter
import mido
import sqlite3

# Variaveis Globais
global gbg, gbgbt, gbgmt

# Definicao Temas
gbg="gray30"
gbgbt="khaki4"
gbgmt="aquamarine2"
gbgbtplay="aquamarine2"
gbgbtpause="aquamarine2"


<<<<<<< /tmp/tsoUyM_principal.py

=======
# Funcao para listar Dispositivos MIDI
>>>>>>> principal.py
def listar_dispositivos_midi():
    """
    Retorna uma lista dos nomes dos dispositivos MIDI de entrada.
    """
    try:
        dispositivos_in = mido.get_input_names()
        return dispositivos_in
    except Exception as e:
        return [f"Erro ao listar dispositivos: {e}"]

#def



# Funcao Criar Menu Principal
def criar_gui():
    # Cria Janela
    root = tk.Tk()
<<<<<<< /tmp/tsoUyM_principal.py
    root.geometry("800x600")
    root.title("Controlador KFX CR9")
    root.bind("<Escape>", quit)
    root.config(bg=gbg)
=======
    root.geometry("800x600") # Tamanho Janela
    root.title("Controlador KFX CR9") # Titulo Janela
    root.bind("<Escape>", quit) # Comportamento ao Teclar ESC
    root.config(bg=gbg) # Configurações fundo


    #Conecta Banco de Dados Configurações
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
            mm = f'{row[4]}.add_command(label="{row[0]}", command=row[1])'
            exec(mm)
            print(mm)
            #print(row)
            #print(f'{row[4]}.add_command(label="Texto")')
            #f'{row[4]}.add_command(label="Texto")'


    root.config(menu=menubar)



>>>>>>> principal.py
    
    # Listbox
    listbox = tk.Listbox(root, width=35, height=2, bg=gbgbt, highlightbackground=gbgbt)
    listbox.place(x=433,y=537)
    
    # Listar e inserir os dispositivos no Listbox
    dispositivos_midi = listar_dispositivos_midi()
    if dispositivos_midi:
        for dispositivo in dispositivos_midi:
            listbox.insert(tk.END, dispositivo)
    else:
        listbox.insert(tk.END, "Nenhum dispositivo MIDI encontrado.")


    # Barra de rolagem para o Listbox
    scrollbar = tk.Scrollbar(listbox, orient=tk.VERTICAL, command=listbox.yview)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(bg=gbgbt, activebackground=gbg, highlightbackground=gbgbt)
    scrollbar.place(x=267,y=0)
    
       


    xmetronomo = tk.Button(root,text="Met",bg=gbgmt,activebackground=gbgbt) #,command=
    xmetronomo.place(x=20,y=550)



    xplay = tk.Button(root,text=">",bg=gbgbtplay,activebackground=gbgbt) #,command=
    xplay.place(x=365,y=550)

    xpause = tk.Button(root,text="[ ]",bg=gbgbtpause,activebackground=gbgbt) #,command=
    xpause.place(x=395,y=550)

    

    xconectar = tk.Button(root,text="Conectar",bg=gbgbt) #,command=
    xconectar.place(x=720,y=550)

    
    
    
    

    root.mainloop()


if __name__ == "__main__":
<<<<<<< /tmp/tsoUyM_principal.py
    criar_gui()
=======
    criar_gui()
>>>>>>> principal.py
