import sys
import tkinter as tk
import random

class DesktopPet:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bunny Companion")
        self.root.overrideredirect(True)
        self.root.wm_attributes("-topmost", True)
        self.root.wm_attributes("-transparentcolor", "#123456")

        # Automatically falls back to standard graphic if needed
        try:
            self.img = tk.PhotoImage(file="pet.png")
        except:
            self.img = tk.PhotoImage() # Blank placeholder if file is missing
        
        self.label = tk.Label(self.root, image=self.img, bg="#123456", bd=0)
        self.label.pack()

        self.x = self.root.winfo_screenwidth() // 2
        self.y = self.root.winfo_screenheight() - 150
        self.root.geometry(f"+{self.x}+{self.y}")

        self.speed = 3
        self.direction = random.choice([-1, 1])
        self.state = "walking"

        self.label.bind("<Button-1>", self.start_move)
        self.label.bind("<B1-Motion>", self.on_move)

        self.root.after(100, self.update_movement)
        self.root.after(3000, self.change_mind)
        self.root.mainloop()

    def update_movement(self):
        if self.state == "walking":
            self.x += (self.speed * self.direction)
            if self.x < 0 or self.x > self.root.winfo_screenwidth() - 100:
                self.direction *= -1
            self.root.geometry(f"+{self.x}+{self.y}")
        self.root.after(50, self.update_movement)

    def change_mind(self):
        self.state = random.choice(["walking", "idling"])
        if self.state == "walking":
            self.direction = random.choice([-1, 1])
        self.root.after(random.randint(2000, 5000), self.change_mind)

    def start_move(self, event):
        self.drag_x = event.x
        self.drag_y = event.y

    def on_move(self, event):
        self.x = self.root.winfo_pointerx() - self.drag_x
        self.y = self.root.winfo_pointery() - self.drag_y
        self.root.geometry(f"+{self.x}+{self.y}")

if __name__ == "__main__":
    DesktopPet()
