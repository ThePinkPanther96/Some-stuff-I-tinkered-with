from tkinter import Tk, Button, Label

# create window
window = Tk()
# change the title
window.title("tic tac toe")
# size of window
window.geometry("450x565")
# color bg
window.configure(bg='white')

FONT = ('Tahoma', 24, 'bold')

global turn
turn = True

list_of_X = []
list_of_O = []

def button1_pressed():
    global turn
    while True:
        if turn is True:
            button_1.configure(text='X')
            turn = False
            list_of_X.append(1)
            player_turn.configure(text="player: 2")
            if check_X():
                player_turn.configure(text="player X is the winner")
                window.geometry("450x80")
            break
        if turn is False:
            button_1.configure(text='O')
            turn = True
            list_of_O.append(1)
            player_turn.configure(text="player: 1")
            if check_O():
                player_turn.configure(text="player X is the winner")
                window.geometry("450x80")
            break


def button2_pressed():
    global turn
    while True:
        if turn is True:
            button_2.configure(text='X')
            turn = False
            list_of_X.append(2)
            player_turn.configure(text="player: 2")
            if check_X():

                player_turn.configure(text="player X is the winner")
                window.geometry("450x80")
            break
        if turn is False:
            button_2.configure(text='O')
            turn = True
            list_of_O.append(2)
            player_turn.configure(text="player: 1")
            if check_O():
                player_turn.configure(text="player X is the winner")
                window.geometry("450x80")
            break


def button3_pressed():
    global turn
    while True:
        if turn is True:
            button_3.configure(text='X')
            turn = False
            list_of_X.append(3)
            player_turn.configure(text="player: 2")
            if check_X():
                player_turn.configure(text="player X is the winner")
                window.geometry("450x80")
            break
        if turn is False:
            button_3.configure(text='O')
            turn = True
            list_of_O.append(3)
            player_turn.configure(text="player: 1")
            if check_O():
                player_turn.configure(text="player X is the winner")
                window.geometry("450x80")
            break



def button4_pressed():
    global turn
    while True:
        if turn is True:
            button_4.configure(text='X')
            turn = False
            list_of_X.append(4)
            player_turn.configure(text="player: 2")
            if check_X():
                player_turn.configure(text="player X is the winner")
                window.geometry("450x80")
            break
        if turn is False:
            button_4.configure(text='O')
            turn = True
            list_of_O.append(4)
            player_turn.configure(text="player: 1")
            if check_O():
                player_turn.configure(text="player X is the winner")
                window.geometry("450x80")
            break


def button5_pressed():
    global turn
    while True:
        if turn is True:
            button_5.configure(text='X')
            turn = False
            list_of_X.append(5)
            player_turn.configure(text="player: 2")
            if check_X():
                player_turn.configure(text="player X is the winner")
                window.geometry("450x80")
            break
        if turn is False:
            button_5.configure(text='O')
            turn = True
            list_of_O.append(5)
            player_turn.configure(text="player: 1")
            if check_O():
                player_turn.configure(text="player X is the winner")
                window.geometry("450x80")
            break


def button6_pressed():
    global turn
    while True:
        if turn is True:
            button_6.configure(text='X')
            turn = False
            list_of_X.append(6)
            player_turn.configure(text="player: 2")
            if check_X():
                player_turn.configure(text="player X is the winner")
                window.geometry("450x80")
            break
        if turn is False:
            button_6.configure(text='O')
            turn = True
            list_of_O.append(6)
            player_turn.configure(text="player: 1")
            if check_O():
                player_turn.configure(text="player X is the winner")
                window.geometry("450x80")
            break


def button7_pressed():
    global turn
    while True:
        if turn is True:
            button_7.configure(text='X')
            turn = False
            list_of_X.append(7)
            player_turn.configure(text="player: 2")
            if check_X():
                player_turn.configure(text="player X is the winner")
                window.geometry("450x80")
            break
        if turn is False:
            button_7.configure(text='O')
            turn = True
            list_of_O.append(7)
            player_turn.configure(text="player: 1")
            if check_O():
                player_turn.configure(text="player X is the winner")
                window.geometry("450x80")
            break


def button8_pressed():
    global turn
    while True:
        if turn is True:
            button_8.configure(text='X')
            turn = False
            list_of_X.append(8)
            player_turn.configure(text="player: 2")
            if check_X():
                player_turn.configure(text="player X is the winner")
                window.geometry("450x80")
            break
        if turn is False:
            button_8.configure(text='O')
            turn = True
            list_of_O.append(8)
            player_turn.configure(text="player: 1")
            if check_O():
                player_turn.configure(text="player O is the winner")
                window.geometry("450x80")
            break

def button9_pressed():
    global turn
    while True:
        if turn is True:
            button_9.configure(text='X')
            turn = False
            list_of_X.append(9)
            player_turn.configure(text="player: 2")
            if check_X():
                player_turn.configure(text="player X is the winner")
                window.geometry("450x80")
            break
        if turn is False:
            button_9.configure(text='O')
            turn = True
            list_of_O.append(9)
            player_turn.configure(text="player: 1")
            if check_O():
                player_turn.configure(text="player O is the winner")
                window.geometry("450x80")
            break


def check_X():
    if 1 in list_of_X and 2 in list_of_X and 3 in list_of_X \
            or 4 in list_of_X and 5 in list_of_X and 6 in list_of_X \
            or 7 in list_of_X and 8 in list_of_X and 9 in list_of_X \
            or 1 in list_of_X and 4 in list_of_X and 7 in list_of_X \
            or 2 in list_of_X and 5 in list_of_X and 8 in list_of_X \
            or 3 in list_of_X and 6 in list_of_X and 9 in list_of_X \
            or 1 in list_of_X and 5 in list_of_X and 9 in list_of_X \
            or 3 in list_of_X and 5 in list_of_X and 7 in list_of_X:
        return True


def check_O():
    if 1 in list_of_O and 2 in list_of_O and 3 in list_of_O \
            or 4 in list_of_O and 5 in list_of_O and 6 in list_of_O \
            or 7 in list_of_O and 8 in list_of_O and 9 in list_of_O \
            or 1 in list_of_O and 4 in list_of_O and 7 in list_of_O \
            or 2 in list_of_O and 5 in list_of_O and 8 in list_of_O \
            or 3 in list_of_O and 6 in list_of_O and 9 in list_of_O \
            or 1 in list_of_O and 5 in list_of_O and 9 in list_of_O \
            or 3 in list_of_O and 5 in list_of_O and 7 in list_of_O:
        return True




player_turn = Label(text="player: 1", font=('Tahoma', 24, 'bold'))
player_turn.grid(columnspan=3, pady=20)

button_1 = Button(window, bg='white', fg='black', width=20, height=10, command=button1_pressed)
button_1.grid(row=1, column=0, )

button_2 = Button(window, bg='white', fg='black', width=20, height=10, command=button2_pressed)
button_2.grid(row=1, column=1)

button_3 = Button(window, bg='white', fg='black', width=20, height=10, command=button3_pressed)
button_3.grid(row=1, column=2)

button_4 = Button(window, bg='white', fg='black', width=20, height=10, command=button4_pressed)
button_4.grid(row=2, column=0)

button_5 = Button(window, bg='white', fg='black', width=20, height=10, command=button5_pressed)
button_5.grid(row=2, column=1)

button_6 = Button(window, bg='white', fg='black', width=20, height=10, command=button6_pressed)
button_6.grid(row=2, column=2)

button_7 = Button(window, bg='white', fg='black', width=20, height=10, command=button7_pressed)
button_7.grid(row=3, column=0)

button_8 = Button(window, bg='white', fg='black', width=20, height=10, command=button8_pressed)
button_8.grid(row=3, column=1)

button_9 = Button(window, bg='white', fg='black', width=20, height=10, command=button9_pressed)
button_9.grid(row=3, column=2)

# hold the window open
window.mainloop()
