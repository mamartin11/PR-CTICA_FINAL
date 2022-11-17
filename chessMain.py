from tkinter import *
import chess_matriz

class App():
    def __init__(self, lado):
        self.game = chess_matriz.Game()
        self.lado = lado
        self.imagenes = {}

        self.ventana = Tk()
        self.ventana.title("FEN CHESS")
        self.ventana.iconbitmap("Chess_icono.ico")
        self.ventana.geometry(f"{str(lado*8)}x{str(lado*8)}")
        self.ventana.resizable(0,0)
    

        self.miframe=Frame(self.ventana, width= 840, height=480)
        self.miframe.pack(expand='True', fill='both')
        self.miframe.config(cursor='hand2')


        self.interfaz = Canvas(self.miframe)
        self.interfaz.pack(fill="both", expand=True)

        


    def __call__(self):
        self.ventana.mainloop()

    def tablero(self):
        for i in range(8):
            for j in range(8):
                if (i+j)%2==0:
                    self.interfaz.create_rectangle(i*self.lado, j*self.lado, (i+1)*self.lado, (j+1)*self.lado, fill="#dfc07f")
                else:
                    self.interfaz.create_rectangle(i*self.lado, j*self.lado, (i+1)*self.lado, (j+1)*self.lado, fill="#7a4f37")

    def cargar(self):
        piezas=["bB","bK","bN","bP","bQ","bR","wB","wK","wN","wP","wQ","wR"]
        for pieza in piezas:
            self.imagenes[pieza] = PhotoImage(file="./imagenes/" + pieza + ".png")

    def mostrar(self):
        for indice_i, i in enumerate(self.game.piezas):
            for indice_j,j in enumerate(i):
                if j !="--":
                    self.interfaz.create_image(indice_j*self.lado, indice_i*self.lado, image=self.imagenes[j], anchor="nw" )

Ajedrez=App(60)
Ajedrez.tablero()
Ajedrez.cargar()
Ajedrez.mostrar()
Ajedrez()