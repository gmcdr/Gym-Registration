import sqlite3
from tkinter import *
from datetime import datetime
import os


bank = sqlite3.connect('data_base/Academy_data_base.db')
cursor = bank.cursor()
bank.commit()


window = Tk()
var = StringVar()
window.title("CadastroZ 1.0")
window.iconbitmap("img/icone.ico")
window.configure(bg='#00FF7F')

# =====================================VARIAVEIS=========================================
name = '' ; idade = ''; email ='' ; tel1 = ''; tel2 =''; mas = '';fem =''; sexo = ''
cpf = ''; nas = ''; alt = ''; peso = ''; ende = '' ; men ='';num  = '';alucpf = ''
exl = ''; data_hora = ''; cpfp = ''; valor = ''
# =======================================================================================




#========================================FUNCTIONS===================================
def li_name(n):
    if len(n) > 22:
        return False
    return True


def email(k):
    if len(k) > 35:
        return False
    return True


def li_idade(i):
    if len(i) > 3:
        return False
    return True



def li_tele(t):
    if len(t) > 9:
        return False
    return True


def li_dia(d):
    if len(d) > 2:
        return False
    return True


def li_ano(a):
    if len(a) > 4:
        return False
    return True


def exit():
    window.quit()


def erro():
    e = Tk()
    e.title("ERROR")
    e.configure(bg='#00FF7F')
    error = Label(e, text="ERRO DE DADOS !")
    error.place(x=50, y=20)

    e.geometry("200x50+560+200")
    e.resizable(width=0, height=0)
    e.mainloop()


def li_cpf(c):
    if len(c) > 11:
        return False
    return True

def cadastrar_aluno():

    try:
        name = str(name_field.get()) ; idade = int(idade_field.get()) ; email = str(email_field.get())
        tel1 = int(telefone_field.get()) ; tel2 = int(telefone_2_field.get()) ; sexo = str(var.get())
        cpf = int(cpf_field.get()); nas = int(n_dia_field.get()), int(n_mes_field.get()), int(n_ano_field.get())
        alt = int(altura_field.get()); peso = int(peso_field.get()); ende = str(ende_field.get())
        men = int(mensa_field.get()) ; num = int(num_field.get())

        cursor.execute("INSERT INTO alunos VALUES('"+name+"', '"+str(idade)+"','"+email+"','"+str(tel1)+"', '"+sexo+"', '"+str(cpf)+"', '"+str(nas)+"', '"+str(alt)+"', '"+str(peso)+"', '"+str(ende)+"', '"+str(num)+"', '"+str(tel2)+"', '"+str(men)+"')")
        bank.commit()

        cadasC = Tk()
        cadasC.title("Cadastro Completo")
        cdc = Label(cadasC, text='CADASTRO REALIZADO !',font='Gotham-Black')
        cdc.configure(bg='#00FF7F')
        cdc.place(x=30, y=20)
        cadasC.configure(bg='#00FF7F')
        cadasC.geometry("275x50+560+200")
        cadasC.resizable(width=0, height=0)
        cadasC.mainloop()
    except:
        erro()


def pesquisar_Aluno():
        def serch():
            try:
                alucpf = str(pesq.get())
                cursor.execute(f"SELECT * FROM alunos WHERE cpf= {alucpf}")
                cpfR["text"] = cursor.fetchone()

            except:
                erro()

        pes = Tk()
        pes.iconbitmap("img/Gakuseisean-Ivista-2-Start-Menu-Search.ico")
        pes.title("Pesquisar Aluno")
        pes.configure(bg='#00FF7F')

        vldcp = pes.register(func=li_cpf)
        pesq = Entry(pes,highlightthickness=2 ,validate='key', validatecommand=(vldcp, '%P'))
        pesq.place(x=400, y=37)

        cpfL = Label(pes, text="CPF DO ALUNO", font="Gotham-Black")
        cpfL.configure(bg='#00FF7F')
        cpfL.place(x=400, y=10)

        info= Label(pes, text='NOME   | IDADE   | EMAIL   | TEL   | SEX   | CPF   | NAS   | ALT   | PESO   | ENDE   | Nº   | TEL2   | MEN   |',font="Gotham-Black")
        info.place(x=1, y=100)
        info.configure(bg='#00FF7F')

        cpfR = Label(pes, text='')
        cpfR.place(x=1, y=130)

        search = Button(pes, text="Pesquisar", command=serch)
        search.place(x=540, y=35)

        pho_17 = Label(pes)
        pho_17.configure(bg='#00FF7F')
        pho_17.place(x=1, y=5)

        pes.geometry("950x200")
        pes.resizable(width=0, height=0)
        pes.mainloop()

def excluir_registro():
    def excluir():
        try:
            exl = str(et.get())
            cursor.execute(f" DELETE from alunos WHERE cpf = {exl}")
            bank.commit()
            bank.close()
            e = Tk()
            e.configure(bg='#00FF7F')
            error = Label(e, text="ALUNO EXCLUIDO!")
            error.place(x=50, y=20)
            e.geometry("200x50+560+200")
            e.resizable(width=0, height=0)
            e.mainloop()
        except:
            erro()
    e = Tk()
    e.iconbitmap("img/Whyred-Dsquared-Bin-Trash-grey-empty.ico")
    e.title("Excluir")
    e.configure(bg='#00FF7F')
    error = Label(e, text="CPF DO ALUNO", font="Gotham-Black")
    error.configure(bg='#00FF7F')
    error.place(x=90, y=5)

    vldcp = e.register(func=li_cpf)
    et = Entry(e,highlightthickness=2 ,validate='key', validatecommand=(vldcp, '%P'))
    et.place(x=95, y=35)

    ex = Button(e, text='Excluir Registro', command=excluir)
    ex.place(x=112, y=65)

    e.geometry("320x100+560+200")
    e.resizable(width=0, height=0)
    e.mainloop()

def registrar_pagamento():
    def pagar():
        try:
            cpfp = epc.get();
            valor = epv.get();
            data_hora = str(datetime.now())
            cursor.execute(
                "INSERT INTO pagamentos VALUES ('" + str(cpfp) + "', '" + str(valor) + "', '" + data_hora + "')")
            bank.commit()
            s = Tk()
            s.title("Pago !")
            s.configure(bg='#00FF7F')
            su = Label(s, text="PAGAMENTO EFETUADO !")
            su.place(x=30, y=20)

            s.geometry("200x50+560+200")
            s.resizable(width=0, height=0)
            s.mainloop()
        except:
            pass

    rp = Tk()
    rp.iconbitmap("img/Designcontest-Ecommerce-Business-Money.ico")
    rp.title("Pagar")
    rp.configure(bg='#00FF7F')

    rpl = Label(rp, text="REGISTRAR PAGAMENTO", font="Gotham-Black")
    rpl.configure(bg='#00FF7F')
    rpl.place(x=50, y=5)

    cpfpe = Label(rp, text="CPF", font="Gotham-Black")
    cpfpe.configure(bg='#00FF7F')
    cpfpe.place(x=60, y=40)

    vlp = Label(rp, text="VALOR", font="Gotham-Black")
    vlp.configure(bg='#00FF7F')
    vlp.place(x=180, y=40)

    vldcp = rp.register(func=li_cpf)
    epc = Entry(rp,highlightthickness=2 ,validate='key', validatecommand=(vldcp, '%P'))
    epc.place(x=60, y=80, width=75)

    epv = Entry(rp,highlightthickness=2 ,validate='key', validatecommand=(vldcp, '%P'))
    epv.place(x=180, y=80, width=75)

    pg = Button(rp, text="Pagar", command=pagar)
    pg.place(x=105, y=110, width=100)

    rp.geometry("320x150+560+200")
    rp.resizable(width=0, height=0)
    rp.mainloop()

# ===================================================================================================



# ====================================MENU===========================================================
my_menu = Menu(window)
window.config(menu=my_menu)

pesquisar_menu = Menu(my_menu)
my_menu.add_cascade(label="Opções", menu=pesquisar_menu)
pesquisar_menu.add_command(label="Pesquisar aluno",command=pesquisar_Aluno)
pesquisar_menu.add_command(label="Registrar Pagamento",command=registrar_pagamento)
pesquisar_menu.add_command(label="Excluir Registro",command=excluir_registro)
pesquisar_menu.add_command(label="Sair", command=exit)
# ===========================================================



# =========================ENTRYS====================================================================
vldn = window.register(func=li_name)
name_field = Entry(window,highlightthickness=2 ,validate='key', validatecommand=(vldn, '%P'))
name_field.config(highlightbackground = "#00FF7F", highlightcolor= "#00FF7F")
name_field.place(x=60, y=120, width=130)


vldi = window.register(func=li_idade)
idade_field = Entry(window, highlightthickness=2 ,validate='key', validatecommand=(vldi, '%P'))
idade_field.config(highlightbackground = "#00FF7F", highlightcolor= "#00FF7F")
idade_field.place(x=60, y=160, width=25)

vldem =window.register(func=email)
email_field = Entry(window,highlightthickness=2 , validate='key', validatecommand=(vldem, '%P'))
email_field.config(highlightbackground = "#00FF7F", highlightcolor= "#00FF7F")
email_field.place(x=60, y=200, width=220)


ddd_field = Entry(window,highlightthickness=2 , validate='key', validatecommand=(vldi, '%P'))
ddd_field.config(highlightbackground = "#00FF7F", highlightcolor= "#00FF7F")
ddd_field.place(x=60, y=240, width=28)


vldt = window.register(func=li_tele)
telefone_field = Entry(window, highlightthickness=2 ,validate='key', validatecommand=(vldt, '%P'))
telefone_field.config(highlightbackground = "#00FF7F", highlightcolor= "#00FF7F")
telefone_field.place(x=100, y=240, width=60)

ddd_2_field = Entry(window, highlightthickness=2 ,validate='key', validatecommand=(vldi, '%P'))
ddd_2_field.config(highlightbackground = "#00FF7F", highlightcolor= "#00FF7F")
ddd_2_field.place(x=180, y=240, width=28)


telefone_2_field = Entry(window,highlightthickness=2 , validate='key', validatecommand=(vldt, '%P'))
telefone_2_field.config(highlightbackground = "#00FF7F", highlightcolor= "#00FF7F")
telefone_2_field.place(x=220, y=240, width=60)


m = Radiobutton(window,text="Masculino",variable=var,value="M",font="Gotham")
m.configure(bg='#00FF7F')
f = Radiobutton(window, text="Feminino",variable=var,value="F",font="Gotham")
f.configure(bg='#00FF7F')
m.place(x=60,y=280)
f.place(x=170,y=280)


vldc = window.register(func=li_cpf)
cpf_field = Entry(window, highlightthickness=2 ,validate='key', validatecommand=(vldc, '%P'))
cpf_field.config(highlightbackground = "#00FF7F", highlightcolor= "#00FF7F")
cpf_field.place(x=60, y=320, width=80)



vldd = window.register(func=li_dia)
n_dia_field = Entry(window, highlightthickness=2 ,validate='key', validatecommand=(vldd, '%P'))
n_dia_field.config(highlightbackground = "#00FF7F", highlightcolor= "#00FF7F")
n_dia_field.place(x=60, y=360, width=25)


n_mes_field = Entry(window, highlightthickness=2 ,validate='key', validatecommand=(vldd, '%P'))
n_mes_field.config(highlightbackground = "#00FF7F", highlightcolor= "#00FF7F")
n_mes_field.place(x=90, y=360, width=25)


vldan = window.register(func=li_ano)
n_ano_field = Entry(window, highlightthickness=2 ,validate='key', validatecommand=(vldan, '%P'))
n_ano_field.config(highlightbackground = "#00FF7F", highlightcolor= "#00FF7F")
n_ano_field.place(x=120, y=360, width=30)


altura_field = Entry(window, highlightthickness=2 ,validate='key', validatecommand=(vldi, '%P'))
altura_field.config(highlightbackground = "#00FF7F", highlightcolor= "#00FF7F")
altura_field.place(x=60, y=400, width=40)

peso_field = Entry(window, highlightthickness=2 ,validate='key', validatecommand=(vldi, '%P'))
peso_field.config(highlightbackground = "#00FF7F", highlightcolor= "#00FF7F")
peso_field.place(x=60, y=440, width=40)

ende_field = Entry(window, highlightthickness=2 ,validate='key', validatecommand=(vldem, '%P'))
ende_field.config(highlightbackground = "#00FF7F", highlightcolor= "#00FF7F")
ende_field.place(x=60, y=480, width=230)


mensa_field = Entry(window, highlightthickness=2 ,validate='key', validatecommand=(vldi, '%P'))
mensa_field.config(highlightbackground = "#00FF7F", highlightcolor= "#00FF7F")
mensa_field.place(x=220, y=320, width=80)


num_field = Entry(window, highlightthickness=2 ,validate='key', validatecommand=(vldan, '%P'))
num_field.config(highlightbackground = "#00FF7F", highlightcolor= "#00FF7F")
num_field.place(x=300, y=480, width=50)
# ===================================================================================================



# =========================BUTTONS===================================================================
login = PhotoImage(file='img/login.png')
pho_17 = Label(window,image=login)
cadastrar = Button(window, image=login,command=cadastrar_aluno,borderwidth=0)
cadastrar.configure(bg='#00FF7F')
cadastrar.place(x=150, y=510)
# ===================================================================================================


# =========================LAYERS====================================================================
person = PhotoImage(file="img/person.png")
pho_02 = Label(window, image=person)
pho_02.configure(bg='#00FF7F')
pho_02.place(x=110, y=-14)


pho_03 = Label(window, text="Nome:", font="Gotham-Black")
pho_03.configure(bg='#00FF7F')
pho_03.place(x=2, y=117)


pho_04 = Label(window, text="Email:", font="Gotham-Black")
pho_04.configure(bg='#00FF7F')
pho_04.place(x=2, y=200)


pho_05 = Label(window, text="Tel:", font="Gotham-Black")
pho_05.configure(bg='#00FF7F')
pho_05.place(x=2, y=240)

pho_06 = Label(window, text="Idade:", font="Gotham-Black")
pho_06.configure(bg='#00FF7F')
pho_06.place(x=2, y=160)

pho_07 = Label(window, text="Sexo:", font="Gotham-Black")
pho_07.configure(bg='#00FF7F')
pho_07.place(x=2,y=280)

pho_08 = Label(window, text="CPF:", font="Gotham-Black")
pho_08.configure(bg='#00FF7F')
pho_08.place(x=2, y=320)

pho_15 = Label(window, text="Mensa:", font="Gotham-Black")
pho_15.configure(bg='#00FF7F')
pho_15.place(x=150, y=320)

pho_09 = Label(window, text="Nasc:", font="Gotham-Black")
pho_09.configure(bg='#00FF7F')
pho_09.place(x=2, y=360)

pho_10 = Label(window, text="Altu:", font="Gotham-Black")
pho_10.configure(bg='#00FF7F')
pho_10.place(x=2, y=400)

pho_11 = Label(window, text="Peso:", font="Gotham-Black")
pho_11.configure(bg='#00FF7F')
pho_11.place(x=2, y=440)

pho_12 = Label(window, text="Ende:", font="Gotham-Black")
pho_12.configure(bg='#00FF7F')
pho_12.place(x=2, y=480)

logo =  PhotoImage(file="img/logo.png")
pho_20 = Label(window, image=logo)
pho_20.configure(bg="#00FF7F")
pho_20.place(x=240, y=370)

# ===================================================================================================
window.resizable(width=0, height=0)
window.geometry("400x600+450+40")
window.mainloop()





