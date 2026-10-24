import sys
import os
import random
import time
import subprocess
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

PASSWORD = "thelegion67"

# Helper function for PyInstaller bundled images
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def run_gui():
    def emergency_exit(event=None):
        window.destroy()

    window = tk.Tk()
    window.title("our brains are skirk")
    window.geometry("800x800")
    window.configure(bg="#FFFFFF")
    window.resizable(False, False)

    window.bind("<Control-Shift-K>", emergency_exit)

    title = tk.Label(
        window,
        text="Skirk detector \n Los datos de tu pc han sido skirkeados \n si apagas la pc el programa \nse autodestruye \ncon los datos que recolecta uwu",
        font=("Arial", 18, "bold"),
        fg="#3700ff",
        bg="#FFFFFF"
    )
    title.pack(pady=5)

    try:
        img_path = resource_path("our brains are skirk.jpg")
        image = Image.open(img_path)
        image = image.resize((300, 300))
        photo = ImageTk.PhotoImage(image)

        image_label = tk.Label(window, image=photo, bg="#FFFFFF")
        image_label.image = photo
        image_label.pack(pady=5)
    except Exception as e:
        print("Could not load image:", e)

    instruction = tk.Label(
        window,
        text="Inserta la contraseña",
        fg="white",
        bg="#171923"
    )
    instruction.pack(pady=10)

    password_entry = tk.Entry(
        window,
        font=("Arial", 14),
        justify="center"
    )
    password_entry.pack(padx=30, fill="x", ipady=5)

    def show_no_popup():
        popup = tk.Toplevel(window)
        popup.title("no no no")
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        
        x = random.randint(0, max(0, screen_width - 250))
        y = random.randint(0, max(0, screen_height - 250))
        
        popup.geometry(f"250x250+{x}+{y}")
        popup.configure(bg="black")
        popup.resizable(False, False)
        
        popup.configure(bg="#F9FAFD")
        popup.resizable(False, False)

        label = tk.Label(
            popup,
            text="no no no",
            font=("Arial", 20, "bold"),
            fg="#5900fd",
            bg="#FCFCFF"
        )
        label.pack(pady=10)

        try:
            popup_img_path = resource_path("big s.jpg")
            popup_image = Image.open(popup_img_path)
            popup_image = popup_image.resize((150, 150))
            popup_photo = ImageTk.PhotoImage(popup_image)

            image_label = tk.Label(
                popup,
                image=popup_photo,
                bg="#0056F5"
            )
            image_label.image = popup_photo
            image_label.pack(pady=5)
        except Exception as e:
            print("Could not load popup image:", e)

        ok_button = tk.Button(
            popup,
            text="OK",
            command=popup.destroy
        )
        ok_button.pack(pady=10)

    def recurring_skirk_popup():
        if not window.winfo_exists():
            return

        popup = tk.Toplevel(window)
        popup.title("skirk")
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x = random.randint(0, max(0, screen_width - 250))
        y = random.randint(0, max(0, screen_height - 250))

        popup.geometry(f"250x250+{x}+{y}")
        popup.configure(bg="black")
        popup.resizable(False, False)

        try:
            popup_img_path = resource_path("big s.jpg")
            image = Image.open(popup_img_path)
            image = image.resize((200, 200))
            photo = ImageTk.PhotoImage(image)

            label = tk.Label(popup, image=photo, bg="black")
            label.image = photo
            label.pack(expand=True)
        except Exception:
            pass

        popup.protocol("WM_DELETE_WINDOW", show_no_popup)
        window.after(800, recurring_skirk_popup)

    window.protocol("WM_DELETE_WINDOW", show_no_popup)
    window.after(800, recurring_skirk_popup)

    def check_password():
        password = password_entry.get()
        if password == PASSWORD:
            messagebox.showinfo("q wena", "xdddd")
            window.destroy()
        else:
            messagebox.showerror("nuh uh", "otra vez")
            show_no_popup()
            password_entry.delete(0, tk.END)

    button = tk.Button(
        window,
        text="enviar",
        command=check_password,
        bg="#00b7ff",
        fg="white",
        font=("Arial", 12, "bold")
    )
    button.pack(pady=20)

    window.bind("<Return>", lambda event: check_password())
    window.mainloop()

if __name__ == "__main__":
    run_gui()