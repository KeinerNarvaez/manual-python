import tkinter as tk
from PIL import ImageTk, Image
import pyautogui as Pg
import time
root= tk.Tk()
def chat(): 

    try:
        cantida = int(cantidad.get()) 
    except ValueError:
        texto.config(text="Por favor ingresa un número válido")
        return
    time.sleep(5)
    if(mensaje.get().strip()):
        texto.config(text="Trabajando en ello...")
        imagen_proceso= Image.open(r"C:\Users\USER\Desktop\Python\bot de chat automatico\chat-bot.png")
        imagen_proceso= imagen_proceso.resize((250,250))
        imagen_proceso=ImageTk.PhotoImage(imagen_proceso)
        label_imagen_proceso.config(image=imagen_proceso)
        for i in range(cantida):
            Pg.write(f' {mensaje.get()}') 
            Pg.press('enter')
        texto.config(text="¡Listo!")
    else:
        texto.config(text="Por favor llena el segundo campo")
        imagen_proceso= Image.open(r"C:\Users\USER\Desktop\Python\bot de chat automatico\chatbot.png")
        imagen_proceso= imagen_proceso.resize((250,250))
        imagen_proceso=ImageTk.PhotoImage(imagen_proceso)
        label_imagen_proceso.config(image=imagen_proceso)
mine="minecraftia"
color="cyan3"
root.title("bot para chat")
icon= ImageTk.PhotoImage(Image.open(r"C:\Users\USER\Desktop\Python\bot de chat automatico\chatbot.png"))
root.iconphoto(False,icon)
Titulo=tk.Label(root,text="Bot para escribir mensajes repetidamente",bg=color, font=(mine,13))
Titulo.pack(pady=8)
ubicacion1=tk.Frame(root,bg=color)
ubicacion1.pack(anchor="w",padx=5,pady=5)
ubicacion2=tk.Frame(root,bg=color,pady=5)
ubicacion2.pack(anchor="w",padx=5)
indicador_numero=tk.Label(ubicacion1,text="¿Cuantos mensajes quieres?",bg=color,font=(mine,10))
indicador_numero.pack(side="left")
cantidad=tk.Entry(ubicacion1,font=(mine,10),relief="solid",borderwidth=2,width=100)
cantidad.pack(side="left",padx=5)
indicador_mensaje=tk.Label(ubicacion2,text="¿Cual es tu mensaje?",bg=color,font=(mine,10))
mensaje=tk.Entry(ubicacion2,font=(mine,10),relief="solid",borderwidth=2, width=120)
indicador_mensaje.pack(side="left")
mensaje.pack(side="right",padx=5)
imagen_boton=Image.open(r"C:\Users\USER\Desktop\Python\bot de chat automatico\robot-conversacional.png")
imagen_boton = imagen_boton.resize((40,40))
imagen_boton= ImageTk.PhotoImage(imagen_boton)
boton=tk.Button(root,text="Iniciar bot", image=imagen_boton,compound="left",padx=5, font=(mine,13),relief="solid",fg="white",bg="red3", command=chat)
boton.pack()
texto=tk.Label(root,text="",bg=color,font=(mine,13))
texto.pack()
imagen_proceso= Image.open(r"C:\Users\USER\Desktop\Python\bot de chat automatico\proceso.gif")
imagen_proceso= imagen_proceso.resize((1,1))
imagen_proceso=ImageTk.PhotoImage(imagen_proceso)
label_imagen_proceso=tk.Label(root,image=imagen_proceso,bg=color)
label_imagen_proceso.pack(pady=5)


root.config(bg=color)
root.geometry("500x500") 
root.mainloop() 