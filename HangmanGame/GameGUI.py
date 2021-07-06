# -*- coding: utf-8 -*-
"""
Game view
GUI based Hangman Game
"""
import random
from tkinter import *
import words


# ---------------------- Window handling
root = Tk()
root.geometry('900x900+70+70')
root.title("Hangman Game")

# ----------------------- Word Selection
word = random.choice(words.words_list)
similar_word = word[1]
chances = 6

# -------------------- initial look
result = ["_" for i in range(len(similar_word))]  # for storing the letters

canvas = Canvas(root, width=300, height=300)
canvas.place(x=0, y=50)
img = PhotoImage(file="images/0.png")
canvas.create_image(100, 100, image=img)  # displaying the image

# -------------------------- labels
welcome_label = Label(root, text='Hangman Game', font=('arial', 30, 'bold')).place(x=220, y=5)

similar_word_label = Label(root, text="WORD : {}".format(word[0]), font=('arial', 16), fg="chocolate").place(x=300,
                                                                                                                y=87)

disp_res = Label(root, text="{}".format(" ".join(result)), font=('arial', 17), padx=10).place(x=300, y=150)

chances_label = Label(root, text="Chances Left : {}".format(chances), font=('arial', 17)).place(x=600, y=200)

user_entry_label = Label(root, text="Enter Letter: ", font=('arial', 23)).place(x=157, y=400)

letter = StringVar()
user_entry = Entry(root, textvariable=letter, justify="center").place(x=370, y=413)
# user_entry.focus_set()


# ---------------------------------- Functions

def match():  # Function for checking whether the entered letter is Correct or not

    global result, disp_res, user_entry, similar_word, word, letter, chances, chances_label, img

    let = letter.get()
    #user_entry.delete(0, END)
    if let in similar_word:

        for j in range(len(similar_word)):
            if let == similar_word[j]:
                result[j] = let

        disp_res = Label(root, text="{}".format(" ".join(result)), font=('arial', 17), padx=10).place(x=300, y=150)
        # disp_res.config(text = result)

        if str("".join(result)) == similar_word:
            game_result_label = Label(root, text="You Won !! The letter was : {}".format(similar_word),
                                         font=('arial', 30, 'bold'), fg="darkgreen").place(x=278, y=510)



    else:
        chances -= 1
        chances_label = Label(root, text="Chances Left : {}".format(chances), font=('arial', 17)).place(x=600, y=200)
        img = PhotoImage(file="images/{}.png".format(6 - chances))
        canvas.create_image(100, 100, image=img)

    if chances == 0:
        game_result_label = Label(root, text="You Are Hanged!!", font=('arial', 30, 'bold'), fg="red")
        game_result_label.place(x=300, y=510)


def fun(event):  # fun for managing the enter key
    match()


# --------------------------- Buttons
submit_btn = Button(root, text='submit', command=match, font=("arial", 16), padx=10, bg="green", fg="white",
                       activebackground="darkgreen", activeforeground="white", relief="raised").place(x=270, y=460)

root.bind("<Return>", fun)  # taking input when enter key is pressed

root.mainloop()