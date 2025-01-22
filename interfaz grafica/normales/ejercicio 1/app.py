import tkinter as tk
from PIL import ImageTk, Image
root= tk.Tk()
load = Image.open(r"C:\Users\USER\Desktop\Python\interfaz grafica\normales\ejercicio 1\creeper.jpg")
render = ImageTk.PhotoImage(load)
root.iconphoto(True, render)
def cambiar_color_hover(event):
    boton.config(bg="green2")  

def restaurar_color(event):
    boton.config(bg="green")  
def saludo():
    nombre =pa.get()
    if nombre.strip():
        holamundo.config(text=f"Hola, {nombre}")
    else:
        holamundo.config(text="Por favor, ingresa tu nombre.")
root.title('Hola mundo')
label=tk.Label(root,text='Este es mi primer interfaz grafica en Python',bg="lightblue",font=("minecraftia",10))
label.pack(pady=12)
pa= tk.Entry(root,width=50, )
pa.pack(pady=12)
boton=tk.Button(root,text="Este es un boton",bg='green',command=saludo, width=15, height=2, font=("minecraftia",8), relief="groove", fg="white", bd=5 )
boton.pack()
holamundo=tk.Label(root,text='',bg="lightblue",font=("minecraftia",10))
holamundo.pack(pady=12)
boton.bind("<Enter>", cambiar_color_hover)
boton.bind("<Leave>", restaurar_color) 
img = Image.open(r"C:\Users\USER\Desktop\Python\interfaz grafica\normales\ejercicio 1\creeper.jpg")
image = img.resize((300,300))
imagen= ImageTk.PhotoImage(image)
imagen_label = tk.Label(root, image=imagen)
imagen_label.pack()
root.config(bg='lightblue') 
root.geometry('500x500')
root.mainloop()