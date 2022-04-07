import random
from tkinter import *
from tkinter import messagebox

run=True
# veidojam  logu - mainloop
while run:
    root=Tk()
    root.geometry('905x700')
    root.config(bg='#E7FFFF')
# kā izvēleties vārdus?
    index=random.randint(0,250)
    file=open("words.txt",'r')
    l=file.readlines()
    selected_word=l[index].strip('\n')
# izliekam svītras mināmajam vārdam _ _ _
    x=250
    for i in range(0, len(selected_word)):
        x+=60
        exec('d{}=Label(root,text="_",bg="#E7FFFF",font=("arial",40))'.format(i))
        exec('d{}.place(x={},y={})'.format(i,x,450))
#  izliekam burtus uz ekrāna kā tastatūru
    al=['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for let in al:
        exec('{}=PhotoImage(file="{}.png")'.format(let,let))
# jānorāda vieta, kur tos burtus likt
    button = [['b1','a',0,595],['b2','b',70,595],['b3','c',140,595],['b4','d',210,595],['b5','e',280,595],['b6','f',350,595],['b7','g',420,595],['b8','h',490,595],['b9','i',560,595],['b10','j',630,595],['b11','k',700,595],['b12','l',770,595],['b13','m',840,595],['b14','n',0,645],['b15','o',70,645],['b16','p',140,645],['b17','q',210,645],['b18','r',280,645],['b19','s',350,645],['b20','t',420,645],['b21','u',490,645],['b22','v',560,645],['b23','w',630,645],['b24','x',700,645],['b25','y',770,645],['b26','z',840,645]]
    for q1 in button:
        exec('{}=Button(root,bd=0,command=lambda:check("{}","{}"),bg="#E7FFFF",activebackground="#E7FFFF",font=10,image={})'.format(q1[0],q1[1],q1[0],q1[1]))
        exec('{}.place(x={},y={})'.format(q1[0],q1[2],q1[3]))









    root.mainloop()