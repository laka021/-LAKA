# lobby.py

def show_lobby():
    print("Welcome to the Lobby, LAKA!")

if __name__ == "__main__":
    show_lobby()

import tkinter as tk

def create_lobby_window():
    window = tk.Tk()
    window.title("Lobby")
    
    label = tk.Label(window, text="Welcome to the Lobby, LAKA!", font=("Arial", 16))
    label.pack(padx=20, pady=20)
    
    window.mainloop()

if __name__ == "__main__":
    create_lobby_window()
