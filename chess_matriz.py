from tkinter import *
from tkinter import messagebox

raiz=Tk()
raiz.title('FEN INPUT')
raiz.geometry('400x80')
raiz.iconbitmap("Chess_icono.ico")
raiz.config(bg='light blue')

miNombre=StringVar()

cuadroNombre=Entry(raiz, textvariable=miNombre)
cuadroNombre.place(x=10,y=40,width=300,height=25)

NombreLabel=Label(raiz,text='INGRESE LA EXPRESIÓN FEN :')
NombreLabel.place(x=90,y=10)

def codigoBoton(): #Función para guardar la información del boton
    a=miNombre.get()
    return a 

def destruir():
    raiz.destroy()

botonEnvio=Button(raiz, text='Enviar', command=destruir)
botonEnvio.pack()
botonEnvio.place(x=320,y=40,width=50,height=25)
raiz.mainloop()



cadena=codigoBoton()

print (cadena)
cadena=cadena.split('/') #separo la cadena por /
numeros=['0','1','2','3','4','5','6','7','8']
blancas=['P','N','B','R','Q','K']
negras=['p','n','b','r','q','k']
matriz=[[],[],[],[],[],[],[],[]]
lin=0
flag=True

for linea in cadena: 
    lin+=1
    contador=0
    for i in range(len(linea)):
        if linea[i] in numeros:
            contador+=int(linea[i])
        elif (linea[i] in blancas) or (linea[i] in negras):
            contador+=1
        else:
            messagebox.showwarning("CARACTER INVÁLIDO", f" EL CARACTER {linea[i]} EN LA LÍNEA {lin} ES INVÁLIDO")
            flag=False

    if contador<8: 
        messagebox.showwarning("EXPRESIÓN INCORRECTA", f"Contiene MENOS de 8 casillas en la línea {lin}")
        flag=False
    elif contador>8:
        messagebox.showwarning("EXPRESIÓN INCORRECTA", f"Contiene MÁS de 8 casillas en la línea {lin}")
        flag=False

l=0
for linea in cadena:
    for i in linea:
        if i in numeros:
            for c in range(int(i)):
                matriz[l].append('--')
        elif i in blancas:
            if i=='P':
                matriz[l].append('wP')
            if i=='N':
                matriz[l].append('wN')
            if i=='B':
                matriz[l].append('wB')
            if i=='R':
                matriz[l].append('wR')
            if i=='Q':
                matriz[l].append('wQ')
            if i=='K':
                matriz[l].append('wK')

        elif i in negras:
            if i=='p':
                matriz[l].append('bP')
            if i=='n':
                matriz[l].append('bN')
            if i=='b':
                matriz[l].append('bB')
            if i=='r':
                matriz[l].append('bR')
            if i=='q':
                matriz[l].append('bQ')
            if i=='k':
                matriz[l].append('bK')
    l+=1  
print(matriz)

if flag is True:
    class Game():
        def __init__(self):
            self.piezas=matriz
    
        