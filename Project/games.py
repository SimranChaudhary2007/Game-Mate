from tkinter import*
from tkinter import messagebox, ttk
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

GENRES = [
    {"name": "Popular", "slug": "action"},
    {"name": "Action", "slug": "action"},
    {"name": "Adventure", "slug": "adventure"},
    {"name": "Masively Multiplayer", "slug": "shooter"},
    {"name": "Shooter", "slug": "shooter"},
    {"name": "RPG", "slug": "role-playing-games-rpg"},
    {"name": "Strategy", "slug": "strategy"},
    {"name": "Puzzle", "slug": "puzzle"},
    {"name": "Racing", "slug": "racing"},
    {"name": "Sports", "slug": "sports"},
    {"name": "Fighting", "slug": "fighting"},
    {"name": "Family", "slug": "family"},
    {"name": "Board Games", "slug": "board-games"},
    {"name": "Educational", "slug": "educational"},
    {"name": "Card", "slug": "card"},
]

GENRE_SLUG_MAP = {genre["name"]: genre["slug"] for genre in GENRES}

POPULAR_GAMES = [
    "Valorant", "Fortnite", "Minecraft", "PUBG", "League of Legends", "Counter-Strike",
    "Call of Duty", "Apex Legends", "Overwatch", "Rainbow Six Siege","Dota","Mobile legend","Fall Guys"
]

def fetch_games_by_genre(genre_name=None):
    """Fetch games by genre, only when needed"""
    
    if genre_name in ["Popular Games", "Popular"]:
        popular_games_results = []
        for game_name in POPULAR_GAMES:
            try:
                search_params = {
                    "key": API_KEY,
                    "search": game_name,
                    "search_precise": "true",
                    "page_size": 3
                }
                response = requests.get(BASE_URL, params=search_params)
                
                if response.status_code == 200:
                    results = response.json().get("results", [])
                    if results:
                        popular_games_results.append(results[0])  
            except Exception as e:
                print(f"Error searching for {game_name}: {e}")
    
        return popular_games_results

    params = {
        "key": API_KEY,
        "ordering": "-added",
        "page_size": 30,
    }

    if genre_name and genre_name in GENRE_SLUG_MAP:
        params["genres"] = GENRE_SLUG_MAP[genre_name] 

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        games = data.get("results", [])
        return games
    except requests.exceptions.RequestException as e:
        print(f"Error fetching game data: {e}")
        return []

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

compatible_frame = Frame(win, width=1000, height=150, bg="#B1B1B1")
compatible_frame.place(x=500, y=240)
Label(compatible_frame, text="Games", font=("Bahnschrift", 40), bg="#B1B1B1").place(x=430, y=0)
Label(compatible_frame, text="Select a genre to load games.", font=("Bahnschrift", 13), bg="#B1B1B1").place(x=400, y=60)

genre_frame = Frame(compatible_frame, bg="#B1B1B1")
genre_frame.place(x=300, y=90)

Label(genre_frame, text="Genre:", font=("Bahnschrift", 12), bg="#B1B1B1").pack(side=LEFT, padx=5)

genre_var = StringVar()
genre_dropdown = ttk.Combobox(genre_frame, textvariable=genre_var, state="readonly", width=30, font=("Bahnschrift", 10))
genre_dropdown['values'] = [genre["name"] for genre in GENRES]
genre_dropdown.current(0)  
genre_dropdown.pack(side=LEFT, padx=5)

loading_label = Label(win, text="Please select a genre to load games", font=("Arial", 16), bg="#0C0A0B", fg="white")
loading_label.place(x=800, y=400)

games_frame = Frame(win)
games_frame.place(x=499, y=390)

canvas = Canvas(games_frame, width=980, height=650, bg="white")
scrollbar = Scrollbar(games_frame, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas, bg="white")
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

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
            img = Image.open(image_response.raw).resize((160, 180))
            photo = ImageTk.PhotoImage(img)
            Label(game_frame, image=photo, bg="white").place(x=20, y=10)
            image_references.append(photo)
    except Exception as e:
        print(f"Error loading image for {game_name}: {e}")
        no_image_label = Label(game_frame, text="No Image", width=15, height=8, bg="lightgray")
        no_image_label.place(x=20, y=10)

    def game_details_page(game_data):
        with open("selected_game.json", "w") as file:
            json.dump({"selected_game": game_data["name"], "game_data": game_data}, file)

        win.destroy()
        runpy.run_path("Project/game_details.py")

    btn = Button(game_frame, text=f"{game_name}", font=("Arial", 20, "bold"), fg="#0078D7", bg="white", border=0,
                activebackground="white", command=lambda g=game_data: game_details_page(g))
    btn.place(x=190, y=60)
    
    Frame(game_frame, height=1, bg="#CCCCCC").place(x=0, y=179, width=980)

def clear_game_frames():
    global image_references
    for widget in scrollable_frame.winfo_children():
        widget.destroy()
    image_references = []

def load_games_by_genre():
    global current_games
    
    selected_genre = genre_var.get()

    loading_label.config(text=f"Loading {selected_genre} games...")
    loading_label.place(x=800, y=400)
    
    canvas.pack_forget()
    scrollbar.pack_forget()
    
    clear_game_frames()
    
    def fetch_and_display():
        global current_games
        current_games = fetch_games_by_genre(selected_genre)
        
        win.after(0, display_fetched_games)
    
    def display_fetched_games():
        if not current_games:
            loading_label.config(text=f"No games found for {selected_genre}. Please check your API connection.")
            return
        for game in current_games:
            create_game_frame(game["name"], game)
        
        loading_label.place_forget()
    
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    loading_thread = threading.Thread(target=fetch_and_display)
    loading_thread.daemon = True
    loading_thread.start()

load_button = Button(genre_frame, text="Load Games", font=("Bahnschrift", 10), bg="#0078D7", fg="white",
                     command=load_games_by_genre)
load_button.pack(side=LEFT, padx=10)

def logout():
    msg_box=messagebox.askquestion("Confirm Logout","Are you sure you want to logout?")
    if msg_box == 'yes':
        win.destroy()
        runpy.run_path("Project/log_in.py")

logout_button = Button(text="Logout", font=buttonFont, bg="#0C0A0B", fg="white", border=0, command=logout)
logout_button.place(x=1800, y=80)

win.mainloop()