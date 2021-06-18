import random
import tkinter as tk
import turtle, time
from sys import exit
import winsound
from tkinter import *

def EXIT():
    window.destroy()
    exit()

res = tk.Tk()
Sheight = res.winfo_screenheight()
Swidth = res.winfo_screenwidth()
res.destroy()
res.mainloop()

def test(guess):
    print(guess)


def check(guess):
    winsound.PlaySound('buttons.wav',winsound.SND_FILENAME)
    global wordList, correct, attempt
    if (guess =='A'):
        A.config(bg="red",state="disabled")
    elif (guess =='B'):
        B.config(bg="red",state="disabled")
    elif (guess =='C'):
        C.config(bg="red",state="disabled")
    elif (guess =='D'):
        D.config(bg="red",state="disabled")
    elif (guess =='E'):
        E.config(bg="red",state="disabled")
    elif (guess =='F'):
        F.config(bg="red",state="disabled")
    elif (guess =='G'):
        G.config(bg="red",state="disabled")
    elif (guess =='H'):
        H.config(bg="red",state="disabled")
    elif (guess =='I'):
        I.config(bg="red",state="disabled")
    elif (guess =='J'):
        J.config(bg="red",state="disabled")
    elif (guess =='K'):
        K.config(bg="red",state="disabled")
    elif (guess =='L'):
        L.config(bg="red",state="disabled")
    elif (guess =='M'):
        M.config(bg="red",state="disabled")
    elif (guess =='N'):
        N.config(bg="red",state="disabled")
    elif (guess =='O'):
        O.config(bg="red",state="disabled")
    elif (guess =='P'):
        P.config(bg="red",state="disabled")
    elif (guess =='Q'):
        Q.config(bg="red",state="disabled")
    elif (guess =='R'):
        R.config(bg="red",state="disabled")
    elif (guess =='S'):
        S.config(bg="red",state="disabled")
    elif (guess =='T'):
        T.config(bg="red",state="disabled")
    elif (guess =='U'):
        U.config(bg="red",state="disabled")
    elif (guess =='V'):
        V.config(bg="red",state="disabled")
    elif (guess =='W'):
        W.config(bg="red",state="disabled")
    elif (guess =='X'):
        X.config(bg="red",state="disabled")
    elif (guess =='Y'):
        Y.config(bg="red",state="disabled")
    elif (guess =='Z'):
        Z.config(bg="red",state="disabled")


    
    occurences = word.count(guess)
    if occurences > 0:
        while occurences > 0:
            location = word.index(guess)
            word[location] = "!"
            wordList[location] = guess
            occurences -= 1
            correct += 1
        wordDisplay.config(text=wordList)
        if correct == total:
            wordList = ("You won! The word was " + final)
            wordDisplay.config(text=wordList)
            winsound.PlaySound('applause8.wav',winsound.SND_FILENAME)
            again()

    else:
        attempt += 1
        draw(attempt)
        
def er():
    winsound.PlaySound('chimes.wav',winsound.SND_FILENAME)

def cc():
    a = tk.Button(window, text="9", bg=colour,font=("arial black", 12),fg='black',height=2,width=4)
    a.place(relx=0.3, rely=0.90)
    

def aa():
    a = tk.Button(window, text="8", bg=colour,font=("arial black", 12),fg='black',height=2,width=4)
    a.place(relx=0.3, rely=0.90)

def c():
    a = tk.Button(window, text="7", bg=colour,font=("arial black", 12),fg='black',height=2,width=4)
    a.place(relx=0.3, rely=0.90)

def d():
    a = tk.Button(window, text="6", bg=colour,font=("arial black", 12),fg='black',height=2,width=4)
    a.place(relx=0.3, rely=0.90)

def e():
    a = tk.Button(window, text="5", bg=colour,font=("arial black", 12),fg='black',height=2,width=4)
    a.place(relx=0.3, rely=0.90)

def f():
    a = tk.Button(window, text="4", bg=colour,font=("arial black", 12),fg='black',height=2,width=4)
    a.place(relx=0.3, rely=0.90)

def g():
    a = tk.Button(window, text="3", bg=colour,font=("arial black", 12),fg='black',height=2,width=4)
    a.place(relx=0.3, rely=0.90)

def h():
    a = tk.Button(window, text="2", bg=colour,font=("arial black", 12),fg='black',height=2,width=4)
    a.place(relx=0.3, rely=0.90)

def i():
    a = tk.Button(window, text="1", bg=colour,font=("arial black", 12),fg='black',height=2,width=4)
    a.place(relx=0.3, rely=0.90)

def j():
    a = tk.Button(window, text="0", bg=colour,font=("arial black", 12),fg='black',height=2,width=4)
    a.place(relx=0.3, rely=0.90)



def draw(step):
    if step ==1:
        t.pensize(5)
        t.penup()
        t.goto(-300, -200)
        t.pendown()
        t.forward(600)
        t.penup()
        t.goto(-100,-200)
        cc()
        er()
    elif step ==2:
        t.pensize(5)
        t.left(90)
        t.pendown()
        t.forward(400)
        aa()
        er()
    elif step ==3:
        t.pensize(5)
        t.right(90)
        t.forward(250)
        c()
        er()
    elif step ==4:
        t.pensize(5)
        t.penup()
        t.goto(-100, 160)
        t.left(45)
        t.pendown()
        t.forward(56.56854249)
        d()
        er()
    elif step ==5:
        t.pensize(5)
        t.penup()
        t.goto(150,200)
        t.setheading(270)
        t.pendown()
        t.forward(40)
        e()
        er()
    elif step ==6:
        t.pensize(5)
        t.speed(0)
        t.seth(180)
        t.circle(32)
        f()
        er()
    elif step == 7:
        t.pensize(5)
        t.speed(5)
        t.penup()
        t.goto(150,92)
        t.pendown()
        t.seth(270)
        t.forward(90)
        g()
        er()
    elif step ==8:
        t.pensize(5)
        t.penup()
        t.goto(115,60)
        t.seth(0)
        t.pendown()
        t.forward(70)
        h()
        er()
    elif step ==9:
        t.pensize(5)
        t.penup()
        t.goto(150,0.2)
        t.right(45)
        t.pendown()
        t.forward(75)
        i()
        er()
    elif step ==10:
        t.pensize(5)
        t.penup()
        t.goto(150,0.0)
        t.right(90)
        t.pendown()
        t.forward(75)
        j()
        wordDisplay.config(text = "OUT OF LIVES! The word was " + final)
        winsound.PlaySound('boo2.wav',winsound.SND_FILENAME)
        
        again()
        
colour = "skyblue"


def again():
    RESTART = tk.Button(bg='blue', text="REPLAY",fg='white',font=("arial black", 10), command=restart,height=3,width=6)
    RESTART.place(relx=0.9, rely=0.60)

def restart():
     A.config(bg="lime",state="normal")
     B.config(bg="lime",state="normal")
     C.config(bg="lime",state="normal")
     D.config(bg="lime",state="normal")
     E.config(bg="lime",state="normal")
     F.config(bg="lime",state="normal")
     G.config(bg="lime",state="normal")
     H.config(bg="lime",state="normal")
     I.config(bg="lime",state="normal")
     J.config(bg="lime",state="normal")
     K.config(bg="lime",state="normal")
     L.config(bg="lime",state="normal")
     M.config(bg="lime",state="normal")
     N.config(bg="lime",state="normal")
     O.config(bg="lime",state="normal")
     P.config(bg="lime",state="normal")
     Q.config(bg="lime",state="normal")
     R.config(bg="lime",state="normal")
     S.config(bg="lime",state="normal")
     T.config(bg="lime",state="normal")
     U.config(bg="lime",state="normal")
     V.config(bg="lime",state="normal")
     W.config(bg="lime",state="normal")
     X.config(bg="lime",state="normal")
     Y.config(bg="lime",state="normal")
     Z.config(bg="lime",state="normal")
     
     t.reset()
     window.wm_state('iconic')
     START()  

def START():
    global word, ready, wordDisplay, wordList, total, correct, attempt, final
    word = ["Bhoothnath","Zanjeer","Saudagar","Parvarish","Naseeb","Shamitabh","Laavaris","Yaarana","Sholay","Wazir","Deewaar",
                 "Mohabbatein","Sooryavansham","Agneepath","Shahenshah","Satyagrah","Arakshan","Coolie","Geraftaar"]
    final = random.choice(word)
    
    word = final.upper()
    word = list(word)
    wordList = []
    ready = True
    for n in range(len(word)):
        wordList.append("_")
    ', '.join(wordList)
    wordDisplay.config(text=wordList)
    total = len(word)
    correct = 0
    t.penup()
    t.goto(-300,-200)
    attempt = 0
    window.deiconify()
        

ready = False

window = tk.Tk()
window.title("Hangman")
window.attributes('-fullscreen', 'True')

 
window.configure(background=colour)

title = tk.Label(window, text="HANGMAN", bg=colour, font=("Cooper Black", 70))
title.place(relx=0.38, rely=0.05)


title = tk.Label(window, text="        Guess  the   movie  of ", bg=colour, font=("Arial", 20))
title.place(relx=0.0, rely=0.05)

title = tk.Label(window, text="  Amitabh Bachchan  ", bg=colour, font=("Maiandra GD", 30),fg='red')
title.place(relx=0.0, rely=0.10)

title = tk.Label(window, text="You have only        attempts", bg=colour, font=("Arial", 30),fg='blue')
title.place(relx=0.1, rely=0.90)

a = tk.Button(window, text="10", bg=colour,font=("arial black", 12),fg='black',height=2,width=4)
a.place(relx=0.3, rely=0.90)




b=tk.Button(window,bg="lime")
photo=PhotoImage(file="a.gif")
b.config(image=photo,width="200",height="200")
b.place(relx=0.82, rely=0.01)


FONT = ("Arial", 20)
row1 = 0.3
row2 = 0.4
row3 = 0.5
row4 = 0.6
row5 = 0.7
row6 = 0.8
column1 = 0.05
column2 = 0.1
column3 = 0.15
column4 = 0.2
column5 = 0.25

  
A = tk.Button(window, text="A", bg="lime", font=FONT, command=lambda : check('A')) 
A.place(relx=column1, rely=row1)

B = tk.Button(window, text="B", bg="lime", font=FONT, command=lambda : check('B'))
B.place(relx=column2, rely=row1)

C = tk.Button(window, text="C", bg="lime", font=FONT, command=lambda : check('C'))
C.place(relx=column3, rely=row1)

D = tk.Button(window, text="D", bg="lime", font=FONT, command=lambda : check('D'))
D.place(relx=column4, rely=row1)

E = tk.Button(window, text="E", bg="lime", font=FONT, command=lambda : check('E'))
E.place(relx=column5, rely=row1)

F = tk.Button(window, text="F", bg="lime", font=FONT, command=lambda : check('F'))
F.place(relx=column1, rely=row2)

G = tk.Button(window, text="G", bg="lime", font=FONT, command=lambda : check('G'))
G.place(relx=column2, rely=row2)

H = tk.Button(window, text="H", bg="lime", font=FONT, command=lambda : check('H'))
H.place(relx=column3, rely=row2)

I = tk.Button(window, text="I", bg="lime", font=FONT, command=lambda : check('I'))
I.place(relx=column4, rely=row2)

J = tk.Button(window, text="J", bg="lime", font=FONT, command=lambda : check('J'))
J.place(relx=column5, rely=row2)

K = tk.Button(window, text="K", bg="lime", font=FONT, command=lambda : check('K'))
K.place(relx=column1, rely=row3)

L = tk.Button(window, text="L", bg="lime", font=FONT, command=lambda : check('L'))
L.place(relx=column2, rely=row3)

M = tk.Button(window, text="M", bg="lime", font=FONT, command=lambda : check('M'))
M.place(relx=column3, rely=row3)

N = tk.Button(window, text="N", bg="lime", font=FONT, command=lambda : check('N'))
N.place(relx=column4, rely=row3)

O = tk.Button(window, text="O", bg="lime", font=FONT, command=lambda : check('O'))
O.place(relx=column5, rely=row3)

P = tk.Button(window, text="P", bg="lime", font=FONT, command=lambda : check('P'))
P.place(relx=column1, rely=row4)

Q = tk.Button(window, text="Q", bg="lime", font=FONT, command=lambda : check('Q'))
Q.place(relx=column2, rely=row4)

R = tk.Button(window, text="R", bg="lime", font=FONT, command=lambda : check('R'))
R.place(relx=column3, rely=row4)

S = tk.Button(window, text="S", bg="lime", font=FONT, command=lambda : check('S'))
S.place(relx=column4, rely=row4)

T = tk.Button(window, text="T", bg="lime", font=FONT, command=lambda : check('T'))
T.place(relx=column5, rely=row4)

U = tk.Button(window, text="U", bg="lime", font=FONT, command=lambda : check('U'))
U.place(relx=column1, rely=row5)

V = tk.Button(window, text="V", bg="lime", font=FONT, command=lambda : check('V'))
V.place(relx=column2, rely=row5)

W = tk.Button(window, text="W", bg="lime", font=FONT, command=lambda : check('W'))
W.place(relx=column3, rely=row5)

X = tk.Button(window, text="X", bg="lime", font=FONT, command=lambda : check('X'))
X.place(relx=column4, rely=row5)

Y = tk.Button(window, text="Y", bg="lime", font=FONT, command=lambda : check('Y'))
Y.place(relx=column5, rely=row5)

Z = tk.Button(window, text="Z", bg="lime", font=FONT, command=lambda : check('Z'))
Z.place(relx=column3, rely=row6)

canvas = tk.Canvas(window, height=Sheight*0.6, width=Swidth*0.6)
canvas.place(relx=0.35, rely=row1)

t = turtle.RawTurtle(canvas)
screen = t.getscreen()
screen.bgcolor=("white")


wordDisplay = tk.Label(window, text="WORD", font=("Arial",30), bg=colour)
wordDisplay.place(relx=0.1, rely=0.2)

EXIT = tk.Button(window, text="EXIT", bg='orange',font=("arial black", 10),fg='red', command=EXIT,height=3,width=6)
EXIT.place(relx=0.9, rely=0.80)

START()

window.mainloop()

