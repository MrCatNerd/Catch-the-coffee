from tkinter import *
from WITH_HEIGHT import WITH,HEIGHT
from sys import exit

window = Tk()
window.title("Catch the coffee")

center_X_screen = window.winfo_screenwidth()
center_Y_screen = window.winfo_screenheight()

spawn_x = (center_X_screen/2)-(WITH/2)
spawn_y = (center_Y_screen/2)-(HEIGHT/2)

window.geometry(f"{WITH}x{HEIGHT}+{int(spawn_x)}+{int(spawn_y)}")
bg_color = "blue"
window.configure(bg = bg_color)

def close_game():
    window.destroy()
    exit()

def start_game():
    global duificulty
    if duificulty == "":
        duificulty = "normal"
    window.destroy()
    import game_script
    game_script.init()

duificulty = ""

def easy_duificulty():
    global duificulty
    duificulty = "easy"
    start_game()

def normal_duificulty():
    global duificulty
    duificulty = "normal"
    start_game()

def hard_duificulty():
    global duificulty
    duificulty = "hard"
    start_game()

def hardcore_duificulty():
    global duificulty
    duificulty = "hardcore"
    start_game()

def start_duificulty():
    duificulty_window = Toplevel(bg = bg_color)
    
    easy = Button(duificulty_window,text="EASY",command= easy_duificulty).pack()
    normal = Button(duificulty_window,text="NORMAL",command= normal_duificulty).pack()
    hard = Button(duificulty_window,text="HARD",command= hard_duificulty).pack()
    hardcore = Button(duificulty_window,text="HARDCORE",command= hardcore_duificulty).pack()

def init():

    start_game = Button(window,text="START",fg = "gold",bg = "black",command= start_duificulty).pack()
    exit_game = Button(window,text="CLOSE",fg = "silver",bg = "black",command=close_game).pack()
    
    window.mainloop()

if __name__ == '__main__':
    init()