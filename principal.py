import tkinter as tk
import mido

# Variaveis Globais
global gbg, gbgbt, gbgmt

# Definicao Temas
gbg="gray30"
gbgbt="khaki4"
gbgmt="aquamarine2"
gbgbtplay="aquamarine2"
gbgbtpause="aquamarine2"



def listar_dispositivos_midi():
    """
    Retorna uma lista dos nomes dos dispositivos MIDI de entrada.
    """
    try:
        dispositivos_in = mido.get_input_names()
        return dispositivos_in
    except Exception as e:
        return [f"Erro ao listar dispositivos: {e}"]

def criar_gui():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Controlador KFX CR9")
    root.bind("<Escape>", quit)
    root.config(bg=gbg)
    
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
    criar_gui()