from tkinter import *
from tkinter import font

import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("app-1-tkinter-3748e-587c25ce8bc6.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

root=Tk()
root.title("Interfaz")
root.resizable(300,200)

L1 = Label(root, text="Name", bd=2, relief="solid", width=10, height=2)
L1.grid(row=3, column=4, pady=10,padx=40)
font_size = font.nametofont("TkDefaultFont").actual()["size"]  
Nombre = Entry(root, textvariable=StringVar(), width=30, font=("Helvetica", font_size + 10),bd=2,
               relief="solid")
Nombre.grid(row=3, column=5, padx=10)

L2 = Label(root, text="Email", bd=2, relief="solid", width=10, height=2)
L2.grid(row=4, column=4, pady=10,padx=40)
font_size = font.nametofont("TkDefaultFont").actual()["size"]  
EM = Entry(root, 
           textvariable=StringVar(), 
           width=30, font=("Helvetica", font_size + 10),bd=2,
           relief="solid")
EM.grid(row=4, column=5, padx=10)

L3 = Label(root, text="Password", bd=2, relief="solid", width=10, height=2)
L3.grid(row=5, column=4, pady=10,padx=40)
font_size = font.nametofont("TkDefaultFont").actual()["size"]  
PASSW = Entry(root, 
           textvariable=StringVar(), 
           width=30, font=("Helvetica", font_size + 10),bd=2,
           relief="solid")
PASSW.grid(row=5, column=5, padx=10)

def addDataCol1():
    # Obtener el texto ingresado en el widget de entrada
    D1 = Nombre.get()
    D2 = EM.get()
    D3 = PASSW.get()

    if (not D1 and not D2 and not D3) or (not D1 or not D2 or not D3):
        R=Label(root,text="Falta llenar un dato",bd=2, relief="solid", width=30, height=2)
        R.grid(row=7,column=5)
        return
    else:
        datos_dict={ "Usuario":D1,"Correo":D2,"Contraseña":D3 }
        db.collection("Datos Basicos").add(datos_dict)
        R=Label(root,text="", width=30, height=2)
        R.grid(row=7,column=5)

L4 = Button(root, text="Guardar", bd=2, 
            relief="solid", width=40, 
            height=2,command=addDataCol1)
L4.grid(row=6, column=5, columnspan=2, pady=10)

root.mainloop()