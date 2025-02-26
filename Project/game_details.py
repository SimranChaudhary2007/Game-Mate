from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter.font as font
import runpy
import json
from tkinter import ttk
import requests
import webbrowser
import threading
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")  
BASE_URL = os.getenv("BASE_URL")

def fetch_game_details(game_name):
    params = {
        "key": API_KEY,
        "search": game_name,
        "page_size": 1
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        results = response.json().get("results", [])
        if results:
            game_id = results[0]["id"]
            
            details_response = requests.get(f"{BASE_URL}/{game_id}", params={"key": API_KEY})
            details_response.raise_for_status()
            details = details_response.json()
            
            screenshots_response = requests.get(f"{BASE_URL}/{game_id}/screenshots", params={"key": API_KEY})
            screenshots_response.raise_for_status()
            screenshots = screenshots_response.json().get("results", [])
            
            return details, screenshots
        return None, []
    except requests.exceptions.RequestException as e:
        print(f"Error fetching game details: {e}")
        return None, []

win = Tk()
win.configure(bg="#0C0A0B")
win.attributes("-fullscreen", True)

try:
    with open("selected_game.json", "r") as file:
        data = json.load(file)
        selected_game = data.get("selected_game", "Unknown Game")
except FileNotFoundError:
    selected_game = "Unknown Game"

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
    runpy.run_path("Project/games.py")
    
def enter1(i):
    btn3['background']="#989898"
def leave1(i):
    btn3['background']="white"

btn3=Button(win,text="<<",width=4,bg="white",border=0,font=buttonFont,command=back)
btn3.place(x=screen_width-150,y=0)
btn3.bind('<Enter>', enter1)
btn3.bind('<Leave>', leave1)

logo_img = Image.open("Project_images/logo.jpeg")
logo_img = logo_img.resize((150, 150))
logo = ImageTk.PhotoImage(logo_img)
image = Label(image=logo, border=0).place(x=5, y=80)

heading = Label(text="GAME MATE", font=("Gabriola", 100), bg="#0C0A0B", fg="white").place(x=170, y=35)

compatible_frame = Frame(win, width=1000, height=100, bg="#B1B1B1")
compatible_frame.place(x=500, y=240)
Label(compatible_frame, text="Game Details", font=("Bahnschrift", 45), bg="#B1B1B1").place(x=330, y=5)

loading_label = Label(win, text="Loading game details...", font=("Arial", 16), bg="#0C0A0B", fg="white")
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

image_references = []
    
def load_game_details():
    game_details, screenshots = fetch_game_details(selected_game)
        
    if game_details:
        win.after(0, lambda: display_game_details(game_details, screenshots))
    else:
        loading_label.config(text=f"Could not load details for {selected_game}")
            
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
            
        error_label = Label(scrollable_frame, text="Game details not available.", 
                               font=("Arial", 16), bg="white", fg="red")
        error_label.pack(pady=50)

def display_game_details(details, screenshots):
    loading_label.place_forget()
        
    #Game title
    title_label = Label(scrollable_frame, text=details.get("name", selected_game), 
                        font=("Arial", 24, "bold"), bg="white")
    title_label.pack(pady=(20, 10), anchor="w", padx=20)
        
    #Game banner
    try:
        if details.get("background_image"):
            image_url = details["background_image"]
            image_response = requests.get(image_url, stream=True)
            image_response.raise_for_status()
            img = Image.open(image_response.raw)
            img = img.resize((900, 400))
            photo = ImageTk.PhotoImage(img)
            image_label = Label(scrollable_frame, image=photo, bg="white")
            image_label.pack(pady=10)
            image_references.append(photo)
    except Exception as e:
        print(f"Error loading main image: {e}")
    
    info_frame = Frame(scrollable_frame, bg="white")
    info_frame.pack(fill="x", padx=20, pady=10)
        
    #Release date
    date_label = Label(info_frame, text="Release Date:", font=("Arial", 12, "bold"), bg="white")
    date_label.grid(row=0, column=0, sticky="w", pady=5)
    date_value = Label(info_frame, text=details.get("released", "Unknown"), font=("Arial", 12), bg="white")
    date_value.grid(row=0, column=1, sticky="w", padx=10, pady=5)
        
    #Developers
    dev_label = Label(info_frame, text="Developers:", font=("Arial", 12, "bold"), bg="white")
    dev_label.grid(row=1, column=0, sticky="w", pady=5)
        
    developers = ", ".join([dev["name"] for dev in details.get("developers", [])])
    dev_value = Label(info_frame, text=developers or "Unknown", font=("Arial", 12), bg="white")
    dev_value.grid(row=1, column=1, sticky="w", padx=10, pady=5)
        
    #Publishers
    pub_label = Label(info_frame, text="Publishers:", font=("Arial", 12, "bold"), bg="white")
    pub_label.grid(row=2, column=0, sticky="w", pady=5)
        
    publishers = ", ".join([pub["name"] for pub in details.get("publishers", [])])
    pub_value = Label(info_frame, text=publishers or "Unknown", font=("Arial", 12), bg="white")
    pub_value.grid(row=2, column=1, sticky="w", padx=10, pady=5)

    #rating
    rating_label = Label(info_frame, text="Rating:", font=("Arial", 12, "bold"), bg="white")
    rating_label.grid(row=3, column=0, sticky="w", pady=5)

    rating = f"{details.get('rating', 'N/A')}/5 ({details.get('ratings_count', 0)} votes)"
    rating_value = Label(info_frame, text=rating, font=("Arial", 12), bg="white")
    rating_value.grid(row=3, column=1, sticky="w", padx=10, pady=5)

    plat_label = Label(info_frame, text="Platforms:", font=("Arial", 12, "bold"), bg="white")
    plat_label.grid(row=4, column=0, sticky="w", pady=5)
    
    platforms = []
    for platform_dict in details.get("platforms", []):
        platform = platform_dict.get("platform", {}).get("name")
        if platform:
            platforms.append(platform)
        
    platform_text = ", ".join(platforms) or "Unknown"
    plat_value = Label(info_frame, text=platform_text, font=("Arial", 12), bg="white")
    plat_value.grid(row=4, column=1, sticky="w", padx=10, pady=5)

    desc_label = Label(scrollable_frame, text="Game Description", font=("Arial", 16, "bold"), bg="white")
    desc_label.pack(anchor="w", padx=20, pady=(20, 5))

    desc_text = details.get("description_raw", "No description available.")
    if len(desc_text) > 1500:
        desc_text = desc_text[:1500] + "..."
        
    desc_frame = Frame(scrollable_frame, bg="white")
    desc_frame.pack(fill="x", padx=30, pady=5)
        
    desc_value = Label(desc_frame, text=desc_text, font=("Arial", 11), bg="white", justify=LEFT, wraplength=900)
    desc_value.pack(anchor="w")
        
    #Trailer
    trailer_label = Label(scrollable_frame, text="Trailer", font=("Arial", 16, "bold"), bg="white")
    trailer_label.pack(anchor="w", padx=20, pady=(20, 5))

    def open_trailer():
        if details.get("website"):
            webbrowser.open(details["website"])
        else:
            search_query = f"https://www.youtube.com/results?search_query={details.get('name', selected_game)}+trailer"
            webbrowser.open(search_query)

    trailer_btn = Button(scrollable_frame, text="Watch Trailer on YouTube", 
                           font=("Arial", 12), bg="#FF0000", fg="white", command=open_trailer)
    trailer_btn.pack(anchor="w", padx=30, pady=5)

    if screenshots:
        screenshots_label = Label(scrollable_frame, text="Images", font=("Arial", 16, "bold"), bg="white")
        screenshots_label.pack(anchor="w", padx=20, pady=(20, 10))
            
        screenshots_frame = Frame(scrollable_frame, bg="white")
        screenshots_frame.pack(fill="x", padx=20, pady=10)

        row, col = 0, 0
        for i, screenshot in enumerate(screenshots[:4]):
            try:
                image_url = screenshot["image"]
                image_response = requests.get(image_url, stream=True)
                image_response.raise_for_status()
                img = Image.open(image_response.raw)
                img = img.resize((430, 240))
                photo = ImageTk.PhotoImage(img)
                img_label = Label(screenshots_frame, image=photo, bg="white")
                img_label.grid(row=row, column=col, padx=5, pady=5)
                image_references.append(photo)
                    
                col += 1
                if col > 1:
                    col = 0
                    row += 1
            except Exception as e:
                print(f"Error loading screenshot {i+1}: {e}")
                continue
    loading_label.place_forget()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

loading_thread = threading.Thread(target=load_game_details)
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