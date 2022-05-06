from calendar import c
from sqlite3 import Row
from tkinter import *
from tkinter.tix import COLUMN

root = Tk()

root.geometry('300x300')

q_list = []

a_list = []

def display_card():
    card_count = 0
    if card_count != 0 :
        card_count = card_count + 1
    

    q_card_num_var = "question_" + str(card_count)
    a_card_num_var = "answer_" + str(card_count)
    globals()[q_card_num_var] = Label(root, text = q_list[card_count])
    globals()[a_card_num_var] = Label(root, text = a_list[card_count])
    globals()[q_card_num_var].grid(row= card_count + 4, column= 0)
    globals()[a_card_num_var].grid(row= card_count + 5, column= 0)

def send_data():
    q_list.append(txt1.get())
    a_list.append(txt2.get())
    print("q list: "+ str(q_list))
    print("a list: "+ str(a_list))
    display_card()

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
root.mainloop()