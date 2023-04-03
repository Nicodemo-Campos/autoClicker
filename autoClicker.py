import pyautogui
import time
import tkinter as tk

class AutoClickerGUI:
    def __init__(self):
        self.is_clicking = False
        self.root = tk.Tk()
        self.start_button = tk.Button(self.root, text="Iniciar", command=self.start_clicking)
        self.stop_button = tk.Button(self.root, text="Detener", command=self.stop_clicking)
        self.start_button.pack()
        self.stop_button.pack()
        self.root.mainloop()

    def start_clicking(self):
        if not self.is_clicking:
            self.is_clicking = True
            while self.is_clicking:
                x, y = pyautogui.position()
                pyautogui.click(x, y)
                time.sleep(15)

    def stop_clicking(self):
        self.is_clicking = False

AutoClickerGUI()