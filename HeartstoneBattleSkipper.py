import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import configparser  
import time
import subprocess as sp


def createConfig():
    """
    Create a config file
    """
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "PATH", "test")

    with open("settings.ini", "w") as config_file:
        config.write(config_file)

    pass

def crudConfig(hs_path):
  
    if not os.path.exists("settings.ini"):
        createConfig()
    
    config = configparser.ConfigParser()
    config.read("settings.ini")
    
    # Меняем значения из конфиг. файла.
    config.set("Settings", "PATH", f'"{hs_path}"')
    
    # Вносим изменения в конфиг. файл.
    with open("settings.ini", "w") as config_file:
        config.write(config_file)

def restart_game():
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read("settings.ini")
    sp.Popen('taskkill /im Hearthstone.exe /f') 
    #time.sleep(4)
    #sp.Popen(str(config["Settings"]["PATH"]))

def skip_bat():
    #os.system("Hs\skip_scrip.bat")

    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read("settings.ini")
    os.system(f'netsh advfirewall firewall add rule name="HS_stop" dir=out action=block program={str(config["Settings"]["PATH"])}')
    print(f'netsh advfirewall firewall add rule name="HS_stop" dir=out action=block program={str(config["Settings"]["PATH"])}')
    time.sleep(5)
    os.system(f'netsh advfirewall firewall delete rule name="HS_stop"')
    pass




def path_save():

    def save_bb():
        x = entry_tf.get()
        print(x)
        crudConfig(str(x))
        #my_file = open("Hs\conf.ini", "w")
        #my_file.write("[PATH]\n")
        #my_file.write(f'path={x}')
        #my_file.close()
        newWindow.destroy()

    newWindow = tk.Toplevel()
    newWindow.title("Path")
    newWindow.configure(bg = '#1c1c1c')
    newWindow.geometry('200x85')
    newWindow.attributes("-toolwindow", True)
    newWindow.attributes("-topmost",True)
    newWindow.resizable(width=False, height=False)
    newWindow.wm_attributes('-alpha', 0.90)
    newWindow['bg'] = '#1c1c1c'
    frame_win = Frame(newWindow,padx=15,pady=10,bg='#1c1c1c')
    #newWindow.iconbitmap(' hsd.ico')
    frame_win.pack(expand=True) 
    
    change_lb = Label(frame_win, text = "Write your path to Heartstone",bg='#1c1c1c',fg='#fbfbfb')
    change_lb.grid(row=1, column=1)
    entry_tf = Entry(frame_win,bg='#303030',fg='#fbfbfb')
    entry_tf.grid(row=2, column=1, pady=2)
    entry_btn = Button(frame_win, text="Save", command=save_bb,bg='#303030',fg='#fbfbfb')
    entry_btn.grid(row=5, column=1,pady=2)

    

window = Tk()
window.title("Battle Skipper")
window.geometry('295x170')
window.attributes("-topmost",True)
window.resizable(width=False, height=False)
#window.iconbitmap('hsd.ico')
window['bg'] = '#1c1c1c'
window.wm_attributes('-alpha', 0.90)

frame = Frame(
    window,
    padx=17,
    pady=13
)
frame.pack(expand=True)
frame['bg'] = '#1c1c1c'

info_lb = Label(
    frame,
    text="Heartstone Skip Battle.",
    fg='#fbfbfb'
)
info_lb.grid(row=1, column=1)
info_lb['bg'] = '#1c1c1c'

info_2_lb = Label(
    frame,
    text="By @Akumanion & @fenomenom1",
    fg='#fbfbfb'
)
info_2_lb.grid(row=2, column=1)
info_2_lb['bg'] = '#1c1c1c'

path_game_lb = Label(
    frame,
    text="Set your HS path: ",
    fg='#fbfbfb'
)
path_game_lb.grid(row=3, column=1,pady=2)
path_game_lb['bg'] = '#1c1c1c'

skip_battle_lb = Label(
    frame,
    text="If you wish abuse: ",
    bg='#1c1c1c',
    fg='#fbfbfb'
)
skip_battle_lb.grid(row=4, column=1,pady=2)


path_game_btn = Button(
    frame, 
    text='Change Path', 
    command=path_save,
    bg='#303030',
    fg='#fbfbfb'
)
path_game_btn.grid(row=3, column=2,pady=2)

skip_btn = Button(
    frame, 
    text='Skip Battle',
    command=skip_bat,
    bg='#303030',
    fg='#fbfbfb'
)
skip_btn.grid(row=4, column=2,pady=2)

restart_bnt = Button(
    frame, 
    text='Exit Game',
    command=restart_game,
    bg='#303030',
    fg='#fbfbfb'
)
restart_bnt.grid(row=5, column=2,pady=2)

restart_game_lb = Label(
    frame,
    text="If you want exit game: ",
    bg='#1c1c1c',
    fg='#fbfbfb'
)
restart_game_lb.grid(row=5, column=1,pady=2)

window.mainloop()