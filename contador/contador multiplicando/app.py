import tkinter as tk
from PIL import ImageTk, Image
root = tk.Tk()
root.title("Contador")
logopaint=Image.open(r"C:\Users\USER\Desktop\Python\contador\contador de valor a valor\user (2).jpeg")
logo= ImageTk.PhotoImage(logopaint)
root.iconphoto(False,logo)
color="cyan3"
fuente="minecraftia"
labels_numeros = []
def contador():
    par=0
    impar=0
    contar=1
    for label in labels_numeros:
        label.destroy()
    labels_numeros.clear() 
    labelRespuesta.config(text="")
    if input1.get().strip() and input2.get().strip():
        try:
            inicio=int(input1.get())
            fin=int(input2.get())
        except ValueError:
            labelRespuesta.config(text="Pon valores numericos validos")
        for inicio in range(inicio,fin+1):
            contar=1
            for contar in range(contar,6):
                resultado=contar*inicio
                if resultado%2==0:
                    label3=tk.Label(root,text=f"{contar} x {inicio} = {resultado} es par",bg=color,font=(fuente,10),fg="red")
                    label3.pack()
                    labels_numeros.append(label3)
                    par=par+1
                else:
                    label3=tk.Label(root,text=f"{contar} x {inicio} = {resultado} es impar",bg=color,font=(fuente,10),fg="red")
                    label3.pack()
                    labels_numeros.append(label3)
                    impar=impar+1
            label3=tk.Label(root,text='-----------------------',bg=color,font=(fuente,10),fg="red")
            label3.pack()
            labels_numeros.append(label3)
        labelRespuesta.config(text="Finalizo")
        labelRespuesta.config(text=f'Veces de pares: {par} \nVeces impares: {impar}')
    else:
        labelRespuesta.config(text="Por favor llena ambos campos")

titulo=tk.Label(root, text="Contador de valor a valor",font=(fuente,20),bg=color,fg="white")
titulo.pack(pady=10)
ubicacion1=tk.Frame(root,bg=color)
ubicacion1.pack(pady=5,anchor="w")
ubicacion2=tk.Frame(root,bg=color)
ubicacion2.pack(pady=5,anchor="w")
label1=tk.Label(ubicacion1,font=(fuente,15),text="Primer valor:",fg="red", bg=color)
label1.pack(side="left",padx=5)
input1=tk.Entry(ubicacion1,font=(fuente,15),fg="red",relief="solid",borderwidth=1,width=21)
input1.pack(side="right")
label2=tk.Label(ubicacion2,font=(fuente,15),text="Segundo valor:",fg="red", bg=color)
label2.pack(side="left",padx=5)
input2=tk.Entry(ubicacion2,font=(fuente,15),fg="red",relief="solid",borderwidth=1,width=19)
input2.pack(side="right")
imagen_boton= logopaint.resize((40,40))
imagen_boton=ImageTk.PhotoImage(imagen_boton)
boton=tk.Button(root,text="Iniciar",image=imagen_boton,compound="left",font=(fuente,15),padx=5,bg="red",fg="white",command=contador)
boton.pack()
labelRespuesta=tk.Label(root,font=(fuente,15),text="",fg="red", bg=color)
labelRespuesta.pack()
numero=tk.Frame(root,bg=color,width=12)
numero.pack(pady=5)
root.geometry("500x500")
root.config(bg=color)
root.mainloop()