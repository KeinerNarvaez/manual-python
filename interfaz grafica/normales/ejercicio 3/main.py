import tkinter as tk
from PIL import ImageTk, Image
root=tk.Tk()
mine="minecraftia"
color_fondo="salmon"
icono=Image.open(r"C:\Users\USER\Pictures\user (2).jpeg")
logo=ImageTk.PhotoImage(icono)
root.iconphoto(True,logo)
root.title("Calculadora")
frame_cuerpo= tk.Frame(root, bg="gold")
frame_cuerpo.pack()
titulo=tk.Label(root,text="Calculadora", fg="white", font=(mine,27), bg=color_fondo)
titulo.pack(pady=5)
label1=tk.Label(root,text="Primer valor:",font=(mine,14),bg=color_fondo)
label1.pack(anchor="w", padx=5)
input1=tk.Entry(relief="solid",borderwidth=1, width=48,font=(mine,12))
input1.pack(anchor="sw",padx=5)
label2=tk.Label(root,text="Segundo valor:",font=(mine,14),bg=color_fondo)
label2.pack(anchor="w", padx=5)
input2=tk.Entry(relief="solid",borderwidth=1, width=48,font=(mine,12))
input2.pack(anchor="sw",padx=5)
frame_botones = tk.Frame(root, bg=color_fondo)
frame_botones.pack(pady=20)
def suma():
    resultado=int(input1.get())+int(input2.get())
    result.config(text="El resultado es:")
    valor.config(text=resultado)
def restar():
    resultado=int(input1.get())-int(input2.get())
    result.config(text="El resultado es:")
    valor.config(text=resultado)
def division():
    resultado=int(input1.get())/int(input2.get())
    result.config(text="El resultado es:")
    valor.config(text=resultado)
def multiplicacion():
    resultado=int(input1.get())*int(input2.get())
    result.config(text="El resultado es:")
    valor.config(text=resultado)
sumar=tk.Button(frame_botones,text="+", font=(mine,16),relief="solid",borderwidth=3,width=4,command=suma)
sumar.pack(padx=9,side="left")
resta=tk.Button(frame_botones,text="-", font=(mine,16),relief="solid",borderwidth=3,width=4,command=restar)
resta.pack(padx=9,side="left")
multi=tk.Button(frame_botones,text="x", font=(mine,16),relief="solid",borderwidth=3,width=4,command=multiplicacion)
multi.pack(padx=9,side="left")
division=tk.Button(frame_botones,text="÷", font=(mine,16),relief="solid",borderwidth=3,width=4,command=division)
division.pack(padx=9,side="left")
result= tk.Label(root,text="",bg=color_fondo,font=(mine,14))
result.pack()
valor=tk.Label(root,font=(mine,50),bg=color_fondo,text="")
valor.pack(pady=5)
root.config(bg=color_fondo)
root.geometry('500x500')
root.mainloop()