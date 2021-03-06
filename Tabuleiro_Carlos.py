# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 09:49:28 2016

@author: Carlosjunior
"""
import tkinter as tk
import JOGO_DA_VELHA

class Tabuleiro():
    "Classe tabuleiro"
    
    def __init__(self,nome):
        self.game = JOGO_DA_VELHA.jogo()
        self.root = tk.Tk()
        self.nome = self.root.title(nome)
        self.label1 = tk.Label()
        self.label2 =tk.Label()
        self.label3 = tk.Label()
        self.label1.grid(row = 0, column = 0)
        self.label2.grid(row = 1, column = 0)
        self.label3.grid(row = 2, column = 0)
        self.Canvas = tk.Canvas(self.label1,width = 200, height = 20, bg = "black")
        self.Canvas.create_text(80,10,text = "{0}".format(nome), fill = "white")
        self.Canvas.pack()
        self.Canvas2 = tk.Canvas(self.label3,width = 200, height = 20, bg = "black")
        def callback1():
            print(1)
        def callback2():
            print(2)
        def callback3():
            print(3)
        def callback4():
            print(4)
        def callback5():
            print(5)
        def callback6():
            print(6)        
        def callback7():
            print(7)
        def callback8():
            print(8)
        def callback9():
            print(9)
        
        self.b1 = tk.Button(self.label2, text="", width = 10, height = 5)
        self.b2 = tk.Button(self.label2, text="",width = 10, height = 5)
        self.b3 = tk.Button(self.label2, text="", width = 10, height = 5)        
        self.b4 = tk.Button(self.label2, text="",  width = 10, height = 5)
        self.b5 = tk.Button(self.label2, text="", width = 10, height = 5)
        self.b6 = tk.Button(self.label2, text="", width = 10, height = 5)
        self.b7 = tk.Button(self.label2, text="", width = 10, height = 5)
        self.b8 = tk.Button(self.label2, text="", width = 10, height = 5)
        self.b9 = tk.Button(self.label2, text="", width = 10, height = 5)
        
        
        self.b1.configure(command = callback1)
        self.b2.configure(command = callback2)
        self.b3.configure(command = callback3)
        self.b4.configure(command = callback4)
        self.b5.configure(command = callback5)
        self.b6.configure(command = callback6)
        self.b7.configure(command = callback7)
        self.b8.configure(command = callback8)
        self.b9.configure(command = callback9)
        
        a = self.game.recebe_jogada()     
        
        self.b1.pack()
        self.b2.pack()
        self.b3.pack()
        self.b4.pack()
        self.b5.pack()
        self.b6.pack()
        self.b7.pack()
        self.b8.pack()
        self.b9.pack()
        
        self.b1.grid(row = 0, column = 0)
        self.b2.grid(row = 0, column = 1)
        self.b3.grid(row = 0, column = 2)
        self.b4.grid(row = 1, column = 0)
        self.b5.grid(row = 1, column = 1)
        self.b6.grid(row = 1, column = 2)
        self.b7.grid(row = 2, column = 0)
        self.b8.grid(row = 2, column = 1)
        self.b9.grid(row = 2, column = 2)
        
        if a ==0 :
            self.Canvas2.create_text(80,10,text = "Proxima jogada:X", fill = "white")
        else:
            self.Canvas2.create_text(80,10,text = "Proxima jogada:O", fill = "white")
        self.Canvas2.pack()
    
    
    def iniciar(self):
        tk.mainloop()
    
a = Tabuleiro("Jogo da velha")
tk.mainloop()