from calendar import c
from faulthandler import disable
from sqlite3 import Row
from tkinter import *
from tkinter.tix import COLUMN
from random import randint

root = Tk()

root.geometry('300x300')

root.title("Flash Cards!")

q_list = []

a_list = []


q_card_num_var = Label(root, text = "")
a_card_num_var = Label(root, text = "")


q_card_num_var.grid(row= 5, column= 0, columnspan=2)
a_card_num_var.grid(row= 6, column= 0, columnspan=2)


card_count = 0
def open_win(name, info):
    new = name
    globals()[new] = Toplevel(root)
    globals()[new].geometry('1000x200')
    globals()[new].title("pop up")
    Label(globals()[new], text = info, font = ("arial", 25)).pack(pady=30)

def set_card():
    global q_card_num_var
    global a_card_num_var
    q_card_num_var = Label(root, text = "")
    a_card_num_var = Label(root, text = "")


    q_card_num_var.grid(row= 5, column= 0, columnspan=2)
    a_card_num_var.grid(row= 6, column= 0, columnspan=2)
    '''
    show = True
    global canvas
    canvas = Canvas(root, width=50, height=50)
    canvas.grid(row=6,column=0,)
    rectangle = canvas.create_rectangle(0, 0, 50, 25, fill='grey')
    '''


def display_all_cards():
    button.configure(state=DISABLED)
    global rnum
    lq_list =[]
    if q_list == []:
        button.configure(state=NORMAL)
        open_win("finished_cards", "You finished your flashcards! Add more to continue!")
        q_card_num_var.configure(text = "")
        a_card_num_var.configure(text = "")
    else:
        rnum= randint(0,(len(q_list)-1))

        q_card_num_var.configure(text = q_list[rnum])
        show= False
        show_a(show, a_list[rnum])
        
        
        re_q = q_list[rnum]
        re_a = q_list[rnum]

        q_list.remove(q_list[rnum])
        
        print(q_list)
        print(a_list)
        next_btn.configure(state=DISABLED)

def show_a(show, text1):
    global canvas
    if show == True:
        a_card_num_var.config(text = a_list[rnum])
        a_list.remove(a_list[rnum])
        next_btn.configure(state=NORMAL)
    elif show == False:
        a_card_num_var.config(text="")
        print("stuff")


def show_false():
    show = True
    show_a(show, "")

def send_data():
    append_check = False

    if txt1.get() == "" or txt1.get() == " ":
        open_win("error", "You can NOT have a empty space or just a space")
        window_check = True
        append_check = True
    if txt2.get() == "" or txt2.get() == " ":
        if window_check != True:
            open_win("error", "You can NOT have a empty space or just a space")
            append_check = True

    if append_check != True:
        q_list.append(txt1.get())
        a_list.append(txt2.get())
        set_card()
    print("q list: "+ str(q_list))
    print("a list: "+ str(a_list))
    



txt1 = Entry(root, width = 20)
txt2 = Entry(root, width = 20)

txt1.grid(row=0, column=1)
txt2.grid(row=1, column=1)


lbl1 = Label(root,text = "Question:", width = 10)
lbl2 = Label(root,text = "Answer:", width = 10)

lbl1.grid(row=0, column=0)
lbl2.grid(row=1, column=0)

button = Button(root, width = 15, text = "Create Flash Card", command= send_data)
button.grid(row=3, column=0, columnspan=2)
next_btn = Button(root, width = 15, text = "Next Card", command= display_all_cards)
next_btn.grid(row=4, column=0, columnspan=2)
button1 = Button(root, width = 15, text = "Show Answer", command= show_false)
button1.grid(row=7, column=0, columnspan=2)

root.mainloop()