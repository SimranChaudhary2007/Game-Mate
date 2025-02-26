from tkinter import*
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk,Image
import tkinter.font as font
import runpy
import requests
import threading
import json
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")  
BASE_URL = os.getenv("BASE_URL")

def fetch_games():
    params = {
        "key": API_KEY,
        "ordering": "-added",
        "page_size": 100,
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        games = response.json().get("results", [])
        
        must_include = ["Valorant", "Fortnite", "Minecraft","PUBG","League of Legend"]
        included_games = []
        extra_games = []
        
        for game in games:
            if any(name.lower() in game["name"].lower() for name in must_include):
                included_games.append(game)
            else:
                extra_games.append(game)
        
        needed_games = [game for game in fetch_specific_games(must_include) if game not in included_games]
        
        return included_games + needed_games + extra_games[:(100 - len(included_games) - len(needed_games))]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching game data: {e}")
        return []

def fetch_specific_games(game_names):
    specific_games = []
    for name in game_names:
        params = {"key": API_KEY, "search": name, "page_size": 1}
        try:
            response = requests.get(BASE_URL, params=params)
            response.raise_for_status()
            results = response.json().get("results", [])
            if results:
                specific_games.append(results[0])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {name}: {e}")
    return specific_games


win = Tk()
win.configure(bg="#0C0A0B")
win.attributes("-fullscreen", True)

a = Frame(win, width=2000, height=35, bg="white").place(x=0, y=0)
title = Label(a, text="Game Mate", font=("Semi Bold Italic", 15, "bold"), bg="white").place(x=36, y=3)
img = Image.open("Project_images/icon.jpg")
img = img.resize((20, 20))
new_logo = ImageTk.PhotoImage(img)
image = Label(image=new_logo, border=2, bg="#989898").place(x=5, y=5)
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

def min():
    win.iconify()

def on_enter(i):
    btn2['background'] = "red"

def on_leave(i):
    btn2['background'] = "white"

def max():
    msg_box = messagebox.askquestion('Exit Application', 'Are you sure you want to close the application?', icon='warning')
    if msg_box == 'yes':
        win.destroy()

label1 = LabelFrame(win, height=30, bg="white").place(x=0, y=0)
buttonFont = font.Font(size=14)

btn2 = Button(a, text="✕", command=max, width=4, bg="white", border=0, font=buttonFont)
btn2.pack(anchor="ne")
btn2.bind('<Enter>', on_enter)
btn2.bind('<Leave>', on_leave)

def enter(i):
    btn['background'] = "#989898"

def leave(i):
    btn['background'] = "white"

btn = Button(a, text="-", command=min, width=4, bg="white", border=0, font=buttonFont)
btn.place(x=screen_width - 100, y=0)  
btn.bind('<Enter>', enter)
btn.bind('<Leave>', leave)  

def back():
    win.destroy()
    runpy.run_path("Project/specs_checker.py")
    
def enter1(i):
    btn3['background']="#989898"
def leave1(i):
    btn3['background']="white"

btn3=Button(win,text="<<",width=4,bg="white",border=0,font=buttonFont,command=back)
btn3.place(x=screen_width-150,y=0)
btn3.bind('<Enter>', enter1)
btn3.bind('<Leave>', leave1)

logo_img=Image.open("Project_images/logo.jpeg")
logo_img=logo_img.resize((150,150))
logo=ImageTk.PhotoImage(logo_img)
image=Label(image=logo,border=0).place(x=5,y=80)

heading=Label(text="GAME MATE",font=("Gabriola",100),bg="#0C0A0B",fg="white").place(x=170,y=35)


compatible_frame = Frame(win, width=1000, height=100, bg="#B1B1B1")
compatible_frame.place(x=500, y=240)
Label(compatible_frame, text="Games", font=("Bahnschrift", 40), bg="#B1B1B1").place(x=430, y=0)
Label(compatible_frame, text="Here are the list most popular games and their details.", font=("Bahnschrift", 13), bg="#B1B1B1").place(x=300, y=60)

loading_label = Label(win, text="Loading games...", font=("Arial", 16), bg="#0C0A0B", fg="white")
loading_label.place(x=900, y=400)

games_frame = Frame(win)
games_frame.place(x=499, y=340)

image_references = []

canvas = Canvas(games_frame, width=980, height=700, bg="white")
scrollbar = Scrollbar(games_frame, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas, bg="white")
scrollable_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

canvas.pack_forget()
scrollbar.pack_forget()

def create_game_frame(game_name, game_data):
    game_frame = Frame(scrollable_frame, width=980, height=180, bg="white")
    game_frame.pack(fill=X, padx=0, pady=0)
    game_frame.pack_propagate(False)
    
    
    try:
        if game_data.get("background_image"):
            image_url = game_data["background_image"]
            image_response = requests.get(image_url, stream=True)
            image_response.raise_for_status()
            img = Image.open(image_response.raw).resize((150, 170))
            photo = ImageTk.PhotoImage(img)
            Label(game_frame, image=photo, bg="white").place(x=20, y=10)
            image_references.append(photo)
    except Exception as e:
        print(f"Error loading image for {game_name}: {e}")

    def game_details_page(game_name):
        with open("selected_game.json", "w") as file:
            json.dump({"selected_game": game_name}, file)

        win.destroy()
        runpy.run_path("Project/game_details.py")

            
    btn = Button(game_frame, text=f"{game_name}", font=("Arial", 20, "bold"), fg="#0078D7", bg="white", border=0,
                activebackground="white",command=lambda g=game_name: game_details_page(g))
    btn.place(x=180, y=60)

def load_games():
    global games_to_load  
    games_to_load = fetch_games()  
    win.after(0, create_game_frames) 

def create_game_frames():
    global games_to_load 
    for game in games_to_load:  
        create_game_frame(game["name"], game)  
    
    loading_label.place_forget()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

loading_thread = threading.Thread(target=load_games)
loading_thread.daemon = True
loading_thread.start()

def logout():
    msg_box=messagebox.askquestion("Confirm Logout","Are you sure you want to logout?")
    if msg_box == 'yes':
        win.destroy()
        runpy.run_path("Project/log_in.py")

logout_button = Button(text="Logout", font=buttonFont, bg="#0C0A0B", fg="white", border=0,command=logout)
logout_button.place(x=1800, y=80)

win.mainloop()