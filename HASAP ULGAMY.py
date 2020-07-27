from tkinter import *
from tkinter import ttk

r = Tk()
r.title('HASAPLAMA ULGAMY') #ady
r.geometry('650x600') #penjiranin olcegi
r.resizable(FALSE, FALSE) #penjiranin olceginin uytgemezligi ucin
r.configure(bg = 'light blue') #arka plan renki acyk gok

#jemi bahany hasaplamak ucin baha funksiyasyny yazalyn:
def baha():
    s1 = str(entpalow.get()) #palowyn girizilen mukdaryny (sanyny) alyp stringe owuryar
    if s1.isdigit(): #eger girizilen yazgy san (digit) bolsa, integer edip alyar
        s1 = int(entpalow.get()) #integere owuryar
    else: #eger bos goyulan ya-da integerden basga zat girizilen bolsa 0-a denleyar
        s1 = 0
#beyleki naharlar ucin hem menzes funskiyany yazmaly, copy/paste edelin onda :)
    s2 = str(entcorba.get()) #corbanyn girizilen mukdaryny (sanyny) alyp stringe owuryar
    if s2.isdigit(): #eger girizilen yazgy san (digit) bolsa, integer edip alyar
        s2 = int(entcorba.get()) #integere owuryar
    else: #eger bos goyulan ya-da integerden basga zat girizilen bolsa 0-a denleyar
        s2 = 0

    s3 = str(entpizza.get()) #pizzanyn girizilen mukdaryny (sanyny) alyp stringe owuryar
    if s3.isdigit(): #eger girizilen yazgy san (digit) bolsa, integer edip alyar
        s3 = int(entpizza.get()) #integere owuryar
    else: #eger bos goyulan ya-da integerden basga zat girizilen bolsa 0-a denleyar
        s3 = 0

    s4 = str(entayran.get()) #ayranyn girizilen mukdaryny (sanyny) alyp stringe owuryar
    if s4.isdigit(): #eger girizilen yazgy san (digit) bolsa, integer edip alyar
        s4 = int(entayran.get()) #integere owuryar
    else: #eger bos goyulan ya-da integerden basga zat girizilen bolsa 0-a denleyar
        s4 = 0

    s5 = str(entkola.get()) #kolanyn girizilen mukdaryny (sanyny) alyp stringe owuryar
    if s5.isdigit(): #eger girizilen yazgy san (digit) bolsa, integer edip alyar
        s5 = int(entkola.get()) #integere owuryar
    else: #eger bos goyulan ya-da integerden basga zat girizilen bolsa 0-a denleyar
        s5 = 0

    s6 = str(entsuw.get()) #suwyn girizilen mukdaryny (sanyny) alyp stringe owuryar
    if s6.isdigit(): #eger girizilen yazgy san (digit) bolsa, integer edip alyar
        s6 = int(entsuw.get()) #integere owuryar
    else: #eger bos goyulan ya-da integerden basga zat girizilen bolsa 0-a denleyar
        s6 = 0

    s7 = str(entmedewik.get()) #medewigin girizilen mukdaryny (sanyny) alyp stringe owuryar
    if s7.isdigit(): #eger girizilen yazgy san (digit) bolsa, integer edip alyar
        s7 = int(entmedewik.get()) #integere owuryar
    else: #eger bos goyulan ya-da integerden basga zat girizilen bolsa 0-a denleyar
        s7 = 0

    s8 = str(enttort.get()) #tortyn girizilen mukdaryny (sanyny) alyp stringe owuryar
    if s8.isdigit(): #eger girizilen yazgy san (digit) bolsa, integer edip alyar
        s8 = int(enttort.get()) #integere owuryar
    else: #eger bos goyulan ya-da integerden basga zat girizilen bolsa 0-a denleyar
        s8 = 0

    s9 = str(entbaklava.get()) #baklavanyn girizilen mukdaryny (sanyny) alyp stringe owuryar
    if s9.isdigit(): #eger girizilen yazgy san (digit) bolsa, integer edip alyar
        s9 = int(entbaklava.get()) #integere owuryar
    else: #eger bos goyulan ya-da integerden basga zat girizilen bolsa 0-a denleyar
        s9 = 0
#jemi bahany hasaplamak ucin mukdarlaryny (s'leri) bahalaryna kopeldip gosyarys we labeljemi'de yazdyryarys
    lbjemi['text'] = str(s1*10 + s2*8 + s3*15 + s4*2 + s5*3 + s6*1 + s7*3 + s8*4 + s9*2) + ' $'

#yazylanlary ocurmek ucin ocur funksiyany yazalyn:
def ocur():
    entpalow.delete(0, END)
    entpizza.delete(0, END)
    entcorba.delete(0, END)
    entkola.delete(0, END)
    entayran.delete(0, END)
    entsuw.delete(0, END)
    entmedewik.delete(0, END)
    enttort.delete(0, END)
    entbaklava.delete(0, END)
    #jemi'de yazylan jemi bahany (text'i) hem ocurmeli:
    lbjemi['text'] = ' '

#label'leri yazyp cykalyn :)
lbady = Label(r, text='HASAP ULGAMY', font='verdana 20 bold', fg='green', bg='light blue')
lbady.place(x=190, y=10) #adynyn cykjak yeri, renki yasyl, arka plan renki acyk gok
#menu'ny yazalyn:
lbnahar = Label(r, text='NAHAR', font='verdana 20 bold', bg='white')
lbnahar.place(x=50, y=70) #Nahar label'i
lbicgi = Label(r, text='ICGI', font='verdana 20 bold', bg='white')
lbicgi.place(x=260, y=70) #icgi label'i
lbsuyji = Label(r, text='SUYJI', font='verdana 20 bold', bg='white')
lbsuyji.place(x=460, y=70) #suyji label'i
#Naharyn icindaki menu'ny yazalyn, yagny naharlary
lbpalow = Label(r, text='PALOW (10 $)', font = 'verdana 12 bold', bg='light blue')
lbpalow.place(x=30, y=130) #palow label'i, 10 $ bahasy
lbcorba = Label(r, text='CORBA (8 $)', font = 'verdana 12 bold', bg='light blue')
lbcorba.place(x=30, y=220) #corba label'i, bahasy 8$
lbpizza = Label(r, text='PIZZA (15 $)', font = 'verdana 12 bold', bg='light blue')
lbpizza.place(x=30, y=310) #pizza label'i, bahasy 15$
#Icginin icindaki menu:
lbayran = Label(r, text='AYRAN (2 $)', font = 'verdana 12 bold', bg='light blue')
lbayran.place(x=240, y=130) #ayran label'i, 2$ bahasy
lbkola = Label(r, text='KOLA (3 $)', font = 'verdana 12 bold', bg='light blue')
lbkola.place(x=240, y=220) #kola label'i, 3$ bahasy
lbsuw = Label(r, text='SUW (1 $)', font = 'verdana 12 bold', bg='light blue')
lbsuw.place(x=240, y=310) #suw label'i, 1$ bahasy
#Suyjinin icindaki menu:
lbmedewik = Label(r, text='MEDEWIK (3 $)', font = 'verdana 12 bold', bg='light blue')
lbmedewik.place(x=440, y=130) #medewik label'i, 3$ bahasy
lbtort = Label(r, text='TORT (4 $)', font = 'verdana 12 bold', bg='light blue')
lbtort.place(x=440, y=220) #tort label'i, 4$ bahasy
lbbaklava = Label(r, text='BAKLAVA (2 $)', font = 'verdana 12 bold', bg='light blue')
lbbaklava.place(x=440, y=310) #baklava label'i, 2$ bahasy
#mukdarlaryny girizmek ucin entry'lerini yazalyn:
#nahar menusynynky:
entpalow = Entry(r, font='verdana 12 bold')
entpalow.place(x=40, y=170, width=90) #uzynlygy 90 bolan palow entry
entcorba = Entry(r, font='verdana 12 bold')
entcorba.place(x=40, y=260, width=90) #uzynlygy 90 bolan corba entry
entpizza = Entry(r, font='verdana 12 bold')
entpizza.place(x=40, y=350, width=90) #uzynlygy 90 bolan pizza entry
#icgi menusynynky:
entayran = Entry(r, font='verdana 12 bold')
entayran.place(x=240, y=170, width=90) #uzynlygy 90 bolan ayran entry
entkola = Entry(r, font='verdana 12 bold')
entkola.place(x=240, y=260, width=90) #uzynlygy 90 bolan kola entry
entsuw = Entry(r, font='verdana 12 bold')
entsuw.place(x=240, y=350, width=90) #uzynlygy 90 bolan suw entry
#suyji menusynynky:
#nahar menusynynky:
entmedewik = Entry(r, font='verdana 12 bold')
entmedewik.place(x=450, y=170, width=90) #uzynlygy 90 bolan medewik entry
enttort = Entry(r, font='verdana 12 bold')
enttort.place(x=450, y=260, width=90) #uzynlygy 90 bolan tort entry
entbaklava = Entry(r, font='verdana 12 bold')
entbaklava.place(x=450, y=350, width=90) #uzynlygy 90 baklava pizza entry
#jemi tolegi gorkezjek label'i yazalyn:
lbjemi = Label(r, font='verdana 20 bold')
lbjemi.place(x=300, y=430)
#jemi tolegin we yazylanlary ocurmek ucin ocur button'laryny yazalyn:
btjemi = Button(r, text='JEMI TOLEG:', font='verdana 20 bold', bg='green', command=baha)
btjemi.place(x=30, y=420)
btocur = Button(r, text='OCUR', font='verdana 20 bold', bg='red', command=ocur)
btocur.place(x=280, y=520)


r.mainloop()