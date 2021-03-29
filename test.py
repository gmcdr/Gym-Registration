"""
from tkinter import *


def limitar_tamanho(p):
    if len(p) > 8:
        return False
    return True


root = Tk()

# Registrando a função que faz a validação.
vcmd = root.register(func=limitar_tamanho)

entrada = Entry(root, validate='key', validatecommand=(vcmd, '%P'))
entrada2 = Entry(root, validate='key', validatecommand=(vcmd, '%P'))
entrada2.pack()
entrada.pack()

root.mainloop()

import os


from tkinter import *

import sqlite3

bank = sqlite3.connect('data_base/Academy_data_base.db')

cursor = bank.cursor()



def serch():
    alucpf = str(pesq.get())
    print(alucpf)

    cursor.execute(f"SELECT * FROM alunos WHERE cpf= {alucpf}")
    cpfR["text"] = cursor.fetchone()


pes = Tk()
pes.title("Pesquisar Aluno")
pes.configure(bg='#00FF7F')

pesq = Entry(pes)
pesq.place(x=190,y=40)

cpfL = Label(pes,text="CPF DO ALUNO", font="Gotham")
cpfL.configure(bg='#00FF7F')
cpfL.place(x=183,y=10)

cpfR = Label(pes, text='ss',font='Gotham')
cpfR.place(x=1,y=100)


loupe = PhotoImage(file="img/loupe.png")
lp = Label(pes, image=loupe)
search = Button(pes, text="Pesquisar", image=loupe, borderwidth=0,command=serch)
search.configure(bg='#00FF7F')
search.place(x=320,y=40)

id  = PhotoImage(file="img/id.png")
pho_17 = Label(pes, image=id)
pho_17.configure(bg='#00FF7F')
pho_17.place(x=1,y=5)

pes.geometry("1200x200+50+200")
pes.resizable(width=0,height=0)
pes.mainloop()

bank.commit()

import sqlite3

bank = sqlite3.connect('data_base/Academy_data_base.db')

cursor = bank.cursor()



def excluir():
    try:
        exl = str(et.get())
        cursor.execute(f" DELETE from alunos WHERE cpf = {exl}")
    except:
        erro()

e = Tk()
e.title("Excluir")
e.configure(bg='#00FF7F')
error = Label(e, text="CPF DO ALUNO", font="Gotham-Black")
error.place(x=90, y=5)

et = Entry(e)
et.place(x=95, y=35)

ex = Button(e,text='Excluir Registro',command=excluir)
ex.place(x=112, y=60)

e.geometry("320x100+560+200")
e.resizable(width=0, height=0)
e.mainloop()
from datetime import datetime
from tkinter import *

import sqlite3

bank = sqlite3.connect('data_base/Academy_data_base.db')

cursor = bank.cursor()

bank.commit()



print(datetime.now())

def pagar():
    try:
        cpfp = epc.get();  valor = epv.get();
        data_hora = str(datetime.now())
        cursor.execute("INSERT INTO pagamentos VALUES ('"+str(cpfp)+"', '"+str(valor)+"', '"+data_hora+"')")
        bank.commit()
        s = Tk()
        s.title("ERROR")
        s.configure(bg='#00FF7F')
        su = Label(s, text="ERRO DE DADOS !")
        su.place(x=50, y=20)

        s.geometry("200x50+560+200")
        s.resizable(width=0, height=0)
        s.mainloop()
    except:
        pass


rp = Tk()
rp.title("Pagar")
rp.configure(bg='#00FF7F')


rpl = Label(rp, text="REGISTRAR PAGAMENTO",font="Gotham-Black")
rpl.configure(bg='#00FF7F')
rpl.place(x=50, y=5)


cpfpe = Label(rp, text="CPF", font="Gotham-Black")
cpfpe.configure(bg='#00FF7F')
cpfpe.place(x=60,y=40)

vlp = Label(rp, text="VALOR", font="Gotham-Black")
vlp.configure(bg='#00FF7F')
vlp.place(x=180,y=40)

epc = Entry(rp)
epc.place(x=60,y=80, width=75)

epv = Entry(rp)
epv.place(x=180,y=80, width=75)

pg = Button(rp,text="Pagar",command=pagar)
pg.place(x=105, y=110,width=100)

rp.geometry("320x150+560+200")
rp.resizable(width=0, height=0)
rp.mainloop()

"""
