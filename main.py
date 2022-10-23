from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashcard Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=flash_card_img)
canvas.grid(column=0, row=0, columnspan=2)
language = canvas.create_text(400, 150, text="Tile", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word",font=("Ariel", 60, "bold"))

button_wrong_img = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=button_wrong_img, highlightthickness=0)
button_wrong.grid(column=0, row=1)

button_right_img = PhotoImage(file="./images/right.png")
button_right = Button(image=button_right_img, highlightthickness=0)
button_right.grid(column=1, row=1)

window.mainloop()