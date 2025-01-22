import tkinter as tk
import yt_dlp
from PIL import ImageTk, Image


def saludo():
    url = pa.get()
    if url.strip():
        try:
            holamundo.config(text="El video se está descargando...")
            ydl_opts = {'format': 'best'}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            holamundo.config(text="¡Video descargado con éxito!")
            
            img = Image.open(r"C:\Users\USER\Desktop\Python\descargar videos\889221.png")
            img = img.resize((300, 300)) 
            imagen = ImageTk.PhotoImage(img)
            imagen_label.config(image=imagen)
            imagen_label.image = imagen 

        except Exception as e:
            holamundo.config(text=f"La url esta incompleta o esta mal")
            img = Image.open(r"C:\Users\USER\Desktop\Python\descargar videos\disgusto.png")
            img = img.resize((300, 300)) 
            imagen = ImageTk.PhotoImage(img)
            imagen_label.config(image=imagen)
            imagen_label.image = imagen 
    else:
        holamundo.config(text="Por favor, ingresa la URL.")

root = tk.Tk()
load = Image.open(r"C:\Users\USER\Desktop\Python\descargar videos\youtube.png")
render = ImageTk.PhotoImage(load)
root.iconphoto(False, render)
root.title('Descargador de Videos de YouTube')
label = tk.Label(root, text='Ingresa la url del video de youtube que deseas descargar.',bd=5, bg="lightblue", font=("Minecraftia", 10))
label.pack(pady=12)
pa = tk.Entry(root, width=50)
pa.pack(pady=12)
boton = tk.Button(root, text="Descargar Video", bg='green', command=saludo, width=15, height=2, font=("Minecraftia", 8), relief="groove", fg="white", bd=5)
boton.pack()
holamundo = tk.Label(root, text='', bg="lightblue", font=("Minecraftia", 10))
holamundo.pack(pady=12)
img = Image.open(r"C:\Users\USER\Desktop\Python\interfaz grafica\normales\ejercicio 1\creeper.jpg")
image = img.resize((300,300))
imagen= ImageTk.PhotoImage(image)
imagen_label = tk.Label(root, image=imagen)
imagen_label.pack()
root.config(bg='lightblue')
root.geometry('500x500')
root.mainloop()

