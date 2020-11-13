import tkinter
from PIL import Image
from PIL import ImageTk
import random

root = tkinter.Tk()
root.title("Rock Paper Scissors")
root.iconbitmap("images/rps.ico")
root.geometry("500x700")
root.config(bg="white")

rps = Image.open("images/rps.png")
rps_resize = rps.resize((335,335), Image.ANTIALIAS)
rps_enemy = ImageTk.PhotoImage(rps_resize)

rock = Image.open("images/rock.png")
rock_enemy = ImageTk.PhotoImage(rock)
rock_resize = rock.resize((100,100), Image.ANTIALIAS)
rock_img = ImageTk.PhotoImage(rock_resize)

paper = Image.open("images/paper.png")
paper_enemy = ImageTk.PhotoImage(paper)
paper_resize = paper.resize((100,100), Image.ANTIALIAS)
paper_img = ImageTk.PhotoImage(paper_resize)

scissors = Image.open("images/scissors.png")
scissors_enemy = ImageTk.PhotoImage(scissors)
scissors_resize = scissors.resize((100,100), Image.ANTIALIAS)
scissors_img = ImageTk.PhotoImage(scissors_resize)

img = [rock_enemy, paper_enemy, scissors_enemy]

def play(rps):
    global count
    global choice
    global point
    num = random.randint(0, 300)
    if num < 100:
        enemy.config(image=img[0])
        txt.config(text="Rock")
        choice = 0
    elif num < 200:
        enemy.config(image=img[1])
        txt.config(text="Paper")
        choice = 1
    elif num < 300:
        enemy.config(image=img[2])
        txt.config(text="Scissors")
        choice = 2

    if choice == 0 and rps == 1:
        point += 1
        indicator.config(text="You won")
    elif choice == 1 and rps == 2:
        point += 1
        indicator.config(text="You won")
    elif choice == 2 and rps ==  0:
        point += 1
        indicator.config(text="You won")
    elif choice == rps:
        indicator.config(text="You tied")
    else:
        indicator.config(text="You lost")

    count += 1
    counter.config(text=f"Round {count}   |   Points: {point}")

count = 0
point = 0

counter = tkinter.Label(root, text=f"Round {count}   |   Points: {point}", font=("comic sans ms", 20), bg="white")
counter.pack(anchor=tkinter.NW)

bot = tkinter.Frame(root, bg="white")
bot.pack(pady=10)

enemy = tkinter.Label(bot, image=rps_enemy, borderwidth=0, bg="white")
enemy.pack()
txt = tkinter.Label(bot, text="Rock Paper Scissors", font=("comic sans ms", 20), bg="white")
txt.pack()

player = tkinter.Frame(root, bg="white")
player.pack(pady=20)

rock_lbl = tkinter.Button(player, image=rock_img, borderwidth=0, bg="white", command=lambda: play(0))
paper_lbl = tkinter.Button(player, image=paper_img, borderwidth=0, bg="white", command=lambda: play(1))
scissors_lbl = tkinter.Button(player, image=scissors_img, borderwidth=0, bg="white", command=lambda: play(2))

rock_lbl.grid(row=0, column=0, padx=10)
paper_lbl.grid(row=0, column=1, padx=10)
scissors_lbl.grid(row=0, column=2, padx=10)

indicator = tkinter.Label(root, text="Click to start", font=("comic sans ms", 20), bg="white")
indicator.pack(pady=10)

root.mainloop()