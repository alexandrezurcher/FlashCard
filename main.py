from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

data = pandas.read_csv("./data/german_words.csv")
to_learn = data.to_dict(orient="records")
def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="German",fill="black")
    canvas.itemconfig(card_word, text=current_card["German"],fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English",fill="white")
    canvas.itemconfig(card_word, text=current_card["English"],fill="white")
    canvas.itemconfig(card_background, image=card_back_img)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashcard Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,flip_card)

canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word",font=("Ariel", 60, "bold"))

button_wrong_img = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=button_wrong_img, highlightthickness=0,command=new_card)
button_wrong.grid(column=0, row=1)

button_right_img = PhotoImage(file="./images/right.png")
button_right = Button(image=button_right_img, highlightthickness=0,command=new_card)
button_right.grid(column=1, row=1)

new_card()




window.mainloop()