from tkinter import *
import random
from tkinter import messagebox


words = ['example', 'typing', 'test', 'quick', 'brown', 'fox', 'jumps', 'over', 'lazy', 'dog', 'python', 'programming', 'developer', 'keyboard', 'interface', 'function', 'variable', 'loop', 'condition', 'algorithm']

Mainscreen = Tk()
Mainscreen.geometry('800x600')
Mainscreen.title('Typing Test By Teja Singuru')
Mainscreen.config(bg="skyblue")

score = 0
missed = 0
time = 60
count1 = 0
movingwords = ''

def movingtest():
    global count1, movingwords
    floatingtext = 'Typing Test By Teja Singuru'
    if count1 >= len(floatingtext):
        count1 = 0
        movingwords = ''
    movingwords += floatingtext[count1]
    count1 += 1
    findlabels.configure(text=movingwords)
    findlabels.after(150, movingtest)

def giventime():
    global time, score, missed
    if time > 0:
        time -= 1
        timercount.configure(text=time)
        timercount.after(1000, giventime)
    else:
        gameinstruction.configure(text=f'Hit={score} | Miss={missed} | Total Score={score - missed}')
        rr = messagebox.askretrycancel('Notification', 'Do you want to play again?')
        if rr:
            reset_game()

def reset_game():
    global score, missed, time
    score = 0
    missed = 0
    time = 60
    timercount.configure(text=time)
    update_word()
    scorelabelcount.configure(text=score)
    wordentry.delete(0, END)
    gameinstruction.configure(text='Hit enter button after typing the word')
    startlabel.configure(text='Start Typing')
    wordentry.focus_set()

def game(event):
    global score, missed
    if time == 60:
        giventime()
    gameinstruction.configure(text='')
    startlabel.configure(text='')
    entered_word = wordentry.get().strip()
    current_word = labelforward['text']
    if entered_word.lower() == current_word.lower():
        score += 1
        scorelabelcount.configure(text=score)
    else:
        missed += 1
        scorelabelcount.configure(text=score)
    update_word()
    wordentry.delete(0, END)

def update_word():
    global words, labelforward
    labelforward.configure(text=random.choice(words))


findlabels = Label(Mainscreen, text='', font=('arial', 20, 'italic bold'), bg="skyblue", fg="black")
findlabels.place(x=250, y=150)

startlabel = Label(Mainscreen, text='Start Typing', font=('arial', 30, 'italic bold'), bg='black', fg='white')
startlabel.place(x=275, y=50)

labelforward = Label(Mainscreen, text=random.choice(words), font=('arial', 45, 'italic bold'), fg='green')
labelforward.place(x=250, y=240)

scorelabel = Label(Mainscreen, text='Your Score:', font=('arial', 25, 'italic bold'), fg='red')
scorelabel.place(x=10, y=100)

scorelabelcount = Label(Mainscreen, text=score, font=('arial', 25, 'italic bold'), fg='blue')
scorelabelcount.place(x=150, y=180)

labelfortimer = Label(Mainscreen, text='Time Left:', font=('arial', 25, 'italic bold'), fg='red')
labelfortimer.place(x=600, y=100)

timercount = Label(Mainscreen, text=time, font=('arial', 25, 'italic bold'), fg='blue')
timercount.place(x=600, y=180)

gameinstruction = Label(Mainscreen, text='Hit enter button after typing the word', font=('arial', 25, 'italic bold'), fg='grey')
gameinstruction.place(x=150, y=500)

wordentry = Entry(Mainscreen, font=('arial', 25, 'italic bold'), bd=10, justify='center')
wordentry.place(x=250, y=330)
wordentry.focus_set()

Mainscreen.bind('<Return>', game)

movingtest()

mainloop()
