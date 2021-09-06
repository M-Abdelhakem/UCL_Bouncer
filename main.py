from tkinter import *
import math
import time
import sys




#################game_ronaldo###################
def game_ronaldo():
    def outro():
        def exitt():
            window.destroy()
            sys.exit()
            # game_over_window.destroy()

        game_over_window = Toplevel()
        game_over_window.overrideredirect(1)
        game_over_window.config(bg='#032750')

        WIDTH = 400
        HEIGHT = 300

        screenwidth = game_over_window.winfo_screenwidth()
        screenheight = game_over_window.winfo_screenheight()
        game_over_window.geometry(
            f"{WIDTH}x{HEIGHT}+{math.floor((screenwidth / 2) - (WIDTH / 2))}+{math.floor((screenheight / 2) - (HEIGHT / 2) - 30)}")

        Label(game_over_window, text='GAME OVER', bg='#cf8af4', fg='white', font=('Constantia', 26), padx=30).pack(
            pady=30)
        Label(game_over_window, text='Your Score:', fg='#cf8af4', bg='#032750', font=('Segoe Print', 22)).pack()
        Label(game_over_window, text=SCORE, fg='#cf8af4', bg='#032750', font=('Impact', 70)).pack()
        game_over_window.after(2000, exitt)
        game_over_window.mainloop()

    start_window.destroy()
    def move_right(event):
        if player.winfo_x() + player_width < 500:
            player.place(x=player.winfo_x()+10, y=player.winfo_y())


    def move_left(event):
        if player.winfo_x() > 0:
            player.place(x=player.winfo_x()-10, y=player.winfo_y())

    ##############################

    # creating the game window
    window = Tk()
    # adjusting it
    window.resizable(0, 0)

    icon = PhotoImage(file='data\\photos\\ucl.png')
    window.iconphoto(True, icon)

    window.title("UCL BOUNCER !")
    xVELOCITY = 2
    yVELOCITY = 3

    WIDTH = 500
    HEIGHT = 500

    SCORE = 0

    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    window.geometry(f"{WIDTH}x{HEIGHT}+{math.floor((screenwidth / 2) - (WIDTH / 2))}+{math.floor((screenheight / 2) - (HEIGHT / 2) - 30)}")

    canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg='#032750')
    canvas.pack()
    # the buttons that control the player
    window.bind("<a>", move_left)
    window.bind("<d>", move_right)
    window.bind("<Left>", move_left)
    window.bind("<Right>", move_right)

    stadium = PhotoImage(file='data\\photos\\bg.png')
    mystadium = canvas.create_image(0, 0, image=stadium, anchor=NW)

    ball = PhotoImage(file='data\\photos\\ball.png')
    myball = canvas.create_image(0, 0, image=ball, anchor=NW)

    salah = PhotoImage(file='data\\photos\\salah.png')
    messi = PhotoImage(file='data\\photos\\messi.png')
    ronaldo = PhotoImage(file='data\\photos\\ronaldo.png')
    player_width = salah.width()
    player_height = salah.height()

    player = Label(canvas, image=ronaldo, bg='#032750')
    player.place(x=250 - (0.5 * player_width), y=500 - player_height)

    ball_width = ball.width()
    ball_height = ball.height()

    score = Label(canvas, text=f"Score:{SCORE}", bg='#032750', fg='#ffffff', font=('Consolas', 14))
    score.place(x=0, y=0)

    try:
        while True:
            coordinates = canvas.coords(myball)
            over = coordinates[1] + ball_height
            if coordinates[0] >= WIDTH - ball_width or coordinates[0] < 0:
                xVELOCITY = -xVELOCITY
            if coordinates[1] >= HEIGHT - ball_height or coordinates[1] < 0:
                yVELOCITY = -yVELOCITY
            if coordinates[0] + (0.5 * ball.width()) in range(player.winfo_x(), (player.winfo_x() + player_width)) and coordinates[1] + ball_height == player.winfo_y():
                yVELOCITY = -yVELOCITY
                SCORE += 1
                yVELOCITY -= 0.3
            if over >= HEIGHT:
                window.after(10, outro)
            canvas.move(myball, xVELOCITY, yVELOCITY)
            score.config(text=f"Score:{SCORE}")
            window.update()
            time.sleep(0.01)
    except:
        pass
    window.mainloop()


#################game_ronaldo###################


######################game_salah####################
def game_salah():
    def outro():
        def exitt():
            window.destroy()
            sys.exit()
            # game_over_window.destroy()

        game_over_window = Toplevel()
        game_over_window.overrideredirect(1)
        game_over_window.config(bg='#032750')

        WIDTH = 400
        HEIGHT = 300

        screenwidth = game_over_window.winfo_screenwidth()
        screenheight = game_over_window.winfo_screenheight()
        game_over_window.geometry(
            f"{WIDTH}x{HEIGHT}+{math.floor((screenwidth / 2) - (WIDTH / 2))}+{math.floor((screenheight / 2) - (HEIGHT / 2) - 30)}")

        Label(game_over_window, text='GAME OVER', bg='#cf8af4', fg='white', font=('Constantia', 26), padx=30).pack(
            pady=30)
        Label(game_over_window, text='Your Score:', fg='#cf8af4', bg='#032750', font=('Segoe Print', 22)).pack()
        Label(game_over_window, text=SCORE, fg='#cf8af4', bg='#032750', font=('Impact', 70)).pack()
        game_over_window.after(2000, exitt)
        game_over_window.mainloop()

    start_window.destroy()
    def move_right(event):
        if player.winfo_x() + player_width < 500:
            player.place(x=player.winfo_x()+10, y=player.winfo_y())


    def move_left(event):
        if player.winfo_x() > 0:
            player.place(x=player.winfo_x()-10, y=player.winfo_y())

    ##############################

    # creating the game window
    window = Tk()
    # adjusting it
    window.resizable(0, 0)

    icon = PhotoImage(file='data\\photos\\ucl.png')
    window.iconphoto(True, icon)

    window.title("UCL BOUNCER !")
    xVELOCITY = 2
    yVELOCITY = 3

    WIDTH = 500
    HEIGHT = 500

    SCORE = 0

    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    window.geometry(f"{WIDTH}x{HEIGHT}+{math.floor((screenwidth / 2) - (WIDTH / 2))}+{math.floor((screenheight / 2) - (HEIGHT / 2) - 30)}")

    canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg='#032750')
    canvas.pack()
    # the buttons that control the player
    window.bind("<a>", move_left)
    window.bind("<d>", move_right)
    window.bind("<Left>", move_left)
    window.bind("<Right>", move_right)

    stadium = PhotoImage(file='data\\photos\\bg.png')
    mystadium = canvas.create_image(0, 0, image=stadium, anchor=NW)

    ball = PhotoImage(file='data\\photos\\ball.png')
    myball = canvas.create_image(0, 0, image=ball, anchor=NW)

    salah = PhotoImage(file='data\\photos\\salah.png')
    messi = PhotoImage(file='data\\photos\\messi.png')
    ronaldo = PhotoImage(file='data\\photos\\ronaldo.png')
    player_width = salah.width()
    player_height = salah.height()

    player = Label(canvas, image=salah, bg='#032750')
    player.place(x=250 - (0.5 * player_width), y=500 - player_height)

    ball_width = ball.width()
    ball_height = ball.height()

    score = Label(canvas, text=f"Score:{SCORE}", bg='#032750', fg='#ffffff', font=('Consolas', 14))
    score.place(x=0, y=0)

    try:
        while True:
            coordinates = canvas.coords(myball)
            over = coordinates[1] + ball_height
            if coordinates[0] >= WIDTH - ball_width or coordinates[0] < 0:
                xVELOCITY = -xVELOCITY
            if coordinates[1] >= HEIGHT - ball_height or coordinates[1] < 0:
                yVELOCITY = -yVELOCITY
            if coordinates[0] + (0.5 * ball.width()) in range(player.winfo_x(), (player.winfo_x() + player_width)) and coordinates[1] + ball_height == player.winfo_y():
                yVELOCITY = -yVELOCITY
                SCORE += 1
                yVELOCITY -= 0.3
            if over >= HEIGHT:
                window.after(10, outro)
            canvas.move(myball, xVELOCITY, yVELOCITY)
            score.config(text=f"Score:{SCORE}")
            window.update()
            time.sleep(0.01)
    except:
        pass
    window.mainloop()



#################game_salah######################



###############game_messi#################
def game_messi():
    start_window.destroy()
    def outro():
        def exitt():
            window.destroy()
            sys.exit()
            #game_over_window.destroy()
        game_over_window = Toplevel()
        game_over_window.overrideredirect(1)
        game_over_window.config(bg='#032750')

        WIDTH = 400
        HEIGHT = 300

        screenwidth = game_over_window.winfo_screenwidth()
        screenheight = game_over_window.winfo_screenheight()
        game_over_window.geometry(f"{WIDTH}x{HEIGHT}+{math.floor((screenwidth / 2) - (WIDTH / 2))}+{math.floor((screenheight / 2) - (HEIGHT / 2) - 30)}")

        Label(game_over_window, text='GAME OVER', bg='#cf8af4', fg='white', font=('Constantia', 26), padx=30).pack(
            pady=30)
        Label(game_over_window, text='Your Score:', fg='#cf8af4', bg='#032750', font=('Segoe Print', 22)).pack()
        Label(game_over_window, text=SCORE, fg='#cf8af4', bg='#032750', font=('Impact', 70)).pack()
        game_over_window.after(2000, exitt)
        game_over_window.mainloop()


    # moving the player functions
    def move_right(event):
        if player.winfo_x() + player_width < 500:
            player.place(x=player.winfo_x()+10, y=player.winfo_y())


    def move_left(event):
        if player.winfo_x() > 0:
            player.place(x=player.winfo_x()-10, y=player.winfo_y())

    ##############################

    # creating the game window
    window = Tk()
    # adjusting it
    window.resizable(0, 0)

    icon = PhotoImage(file='data\\photos\\ucl.png')
    window.iconphoto(True, icon)

    window.title("UCL BOUNCER !")
    xVELOCITY = 2
    yVELOCITY = 3

    WIDTH = 500
    HEIGHT = 500

    SCORE = 0

    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    window.geometry(f"{WIDTH}x{HEIGHT}+{math.floor((screenwidth / 2) - (WIDTH / 2))}+{math.floor((screenheight / 2) - (HEIGHT / 2) - 30)}")

    canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg='#032750')
    canvas.pack()
    # the buttons that control the player
    window.bind("<a>", move_left)
    window.bind("<d>", move_right)
    window.bind("<Left>", move_left)
    window.bind("<Right>", move_right)

    stadium = PhotoImage(file='data\\photos\\bg.png')
    mystadium = canvas.create_image(0, 0, image=stadium, anchor=NW)

    ball = PhotoImage(file='data\\photos\\ball.png')
    myball = canvas.create_image(0, 0, image=ball, anchor=NW)

    salah = PhotoImage(file='data\\photos\\salah.png')
    messi = PhotoImage(file='data\\photos\\messi.png')
    ronaldo = PhotoImage(file='data\\photos\\ronaldo.png')
    player_width = salah.width()
    player_height = salah.height()

    player = Label(canvas, image=messi, bg='#032750')
    player.place(x=250 - (0.5 * player_width), y=500 - player_height)

    ball_width = ball.width()
    ball_height = ball.height()

    score = Label(canvas, text=f"Score:{SCORE}", bg='#032750', fg='#ffffff', font=('Consolas', 14))
    score.place(x=0, y=0)

    try:
        while True:
            coordinates = canvas.coords(myball)
            over = coordinates[1] + ball_height
            if coordinates[0] >= WIDTH - ball_width or coordinates[0] < 0:
                xVELOCITY = -xVELOCITY
            if coordinates[1] >= HEIGHT - ball_height or coordinates[1] < 0:
                yVELOCITY = -yVELOCITY
            if coordinates[0] + (0.5 * ball.width()) in range(player.winfo_x(), (player.winfo_x() + player_width)) and coordinates[1] + ball_height == player.winfo_y():
                yVELOCITY = -yVELOCITY
                SCORE += 1
                yVELOCITY -= 0.3
            if over >= HEIGHT:
                #exit()
                window.after(10, outro)
            canvas.move(myball, xVELOCITY, yVELOCITY)
            score.config(text=f"Score:{SCORE}")
            window.update()
            time.sleep(0.01)
    except:
        pass
    window.mainloop()

################game_messi####################


def bounce():
    player_image = chosenPlayer.get()
    if player_image == 0:
        start_window.after(250, game_messi)
        #player = Label(canvas1, image=player_image, bg='#032750')
        #player.place(x=250 - (0.5 * player_width), y=500 - player_height)
    elif player_image == 1:
        start_window.after(250, game_salah)
        #player = Label(canvas1, image=player_image, bg='#032750')
        #player.place(x=250 - (0.5 * player_width), y=500 - player_height)
    elif player_image == 2:
        start_window.after(250, game_ronaldo)
        #player = Label(canvas1, image=player_image, bg='#032750')
        #player.place(x=250 - (0.5 * player_width), y=500 - player_height)

start_window = Tk()
start_window.resizable(0, 0)

start_window.config(bg='#032750')
start_window.title("UCL BOUNCER !")
WIDTH = 500
HEIGHT = 500

screenwidth = start_window.winfo_screenwidth()
screenheight = start_window.winfo_screenheight()
start_window.geometry(f"{WIDTH}x{HEIGHT}+{math.floor((screenwidth / 2) - (WIDTH / 2))}+{math.floor((screenheight / 2) - (HEIGHT / 2) - 30)}")

icon = PhotoImage(file='data\\photos\\ucl.png')
start_window.iconphoto(True, icon)

frame = Frame(start_window, width=250).pack()

canvas = Canvas(frame, width=500, height=400, bg='#032750')
canvas.pack()

start = PhotoImage(file='data\\photos\\bg3.png')
mystart = canvas.create_image(0, 0, image=start, anchor=NW)

############################################

messiImage = PhotoImage(file='data\\photos\\messi1.png')
salahImage = PhotoImage(file='data\\photos\\salah1.png')
ronaldoImage = PhotoImage(file='data\\photos\\ronaldo1.png')
playersImage = [messiImage, salahImage, ronaldoImage]
players = ["Messi", "Salah", "Ronaldo"]
chosenPlayer = IntVar()

for player in players:
    radio = Radiobutton(frame,
                        text=player,
                        variable=chosenPlayer,
                        value=players.index(player),
                        padx=5,
                        pady=5,
                        font=('Segoe Print', 14),
                        image=playersImage[players.index(player)],
                        compound=LEFT,
                        indicatoron=FALSE,
                        width=400/3 + 13,
                        height=80,
                        command=bounce,
                        fg='#cf8af4',
                        activeforeground='white',
                        bg='#032750',
                        bd=4,
                        relief=GROOVE,
                        activebackground='#cf8af4')

    radio.pack(anchor=E, side=RIGHT)
##############################################

start_window.mainloop()
