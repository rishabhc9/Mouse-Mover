import tkinter as tk
from tkinter import messagebox
import threading
import time
import pyautogui

class MouseMoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mouse Mover")

        # Interval
        tk.Label(root, text="Hover Interval (in minutes)").grid(row=0, column=0, padx=10, pady=10)
        self.interval_entry = tk.Entry(root, width=10)
        self.interval_entry.grid(row=0, column=1, padx=10, pady=10)
        
        # Start Button
        self.start_button = tk.Button(root, text="Start", command=self.start_moving)
        self.start_button.grid(row=1, column=0, padx=10, pady=10)

        # Stop Button
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_moving, state=tk.DISABLED)
        self.stop_button.grid(row=1, column=1, padx=10, pady=10)

        self.moving = False
        self.thread = None

    def move_mouse(self):
        while self.moving:
            pyautogui.moveRel(0, 50)  # Move the mouse down by 10 pixels
            time.sleep(0.5)
            pyautogui.moveRel(0, -50)  # Move the mouse up by 10 pixels
            
            interval_minutes = float(self.interval_entry.get())
            time.sleep(interval_minutes * 60)

    def start_moving(self):
        if not self.interval_entry.get().strip():
            messagebox.showwarning("Input Error", "Please specify the interval in minutes.")
            return

        try:
            interval_minutes = float(self.interval_entry.get())
            if interval_minutes <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Input Error", "Please enter a positive number for the interval.")
            return

        self.moving = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.thread = threading.Thread(target=self.move_mouse, daemon=True)
        self.thread.start()

    def stop_moving(self):
        self.moving = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = MouseMoverApp(root)
    root.mainloop()
