import tkinter as tk
from tkinter import messagebox
import random
import time

class StudentGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Life Game")
        self.root.geometry("400x400")
        self.student = None

        # Welcome Screen
        self.start_screen()

    def start_screen(self):
        self.clear_frame()
        tk.Label(self.root, text="Welcome to the Student Life Game!", font=("Arial", 16), pady=10).pack()

        tk.Label(self.root, text="Enter Student's Name:", font=("Arial", 12)).pack(pady=5)
        self.name_entry = tk.Entry(self.root, font=("Arial", 12))
        self.name_entry.pack(pady=5)

        tk.Button(self.root, text="Start Game", command=self.start_game, font=("Arial", 12), bg="green", fg="white").pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit, font=("Arial", 12), bg="red", fg="white").pack()

    def start_game(self):
        name = self.name_entry.get()
        if not name.strip():
            messagebox.showwarning("Invalid Input", "Please enter a valid name!")
            return

        self.student = {"name": name, "life": 5}
        self.game_screen()

    def game_screen(self):
        self.clear_frame()

        # Header
        tk.Label(self.root, text=f"Student: {self.student['name']}", font=("Arial", 16), pady=10).pack()

        # Life Display
        self.life_label = tk.Label(self.root, text=f"Life: {self.student['life']}", font=("Arial", 14))
        self.life_label.pack(pady=5)

        # Animated Canvas for Random Event
        self.canvas = tk.Canvas(self.root, width=200, height=200, bg="white", highlightthickness=0)
        self.canvas.pack(pady=10)
        self.circle = self.canvas.create_oval(90, 90, 110, 110, fill="blue")

        # Buttons for Actions
        tk.Button(self.root, text="Random Event", command=self.random_event, font=("Arial", 12), bg="blue", fg="white").pack(pady=5)
        tk.Button(self.root, text="Heal Student", command=self.heal_student, font=("Arial", 12), bg="green", fg="white").pack(pady=5)
        tk.Button(self.root, text="End Game", command=self.end_game, font=("Arial", 12), bg="red", fg="white").pack(pady=5)

    def animate_circle(self, direction="right"):
        """Simulates an animation of a moving circle."""
        for _ in range(20):
            if direction == "right":
                self.canvas.move(self.circle, 2, 0)
            elif direction == "left":
                self.canvas.move(self.circle, -2, 0)
            self.root.update()
            time.sleep(0.01)

        # Return circle to the center
        self.canvas.coords(self.circle, 90, 90, 110, 110)

    def random_event(self):
        self.animate_circle(direction="right")

        events = [
            f"{self.student['name']} slipped on a banana peel and lost a life.",
            f"A surprise quiz stressed {self.student['name']} out! lost a life.",
            f"{self.student['name']} found a first-aid kit and gained a life.",
            f"{self.student['name']} had a relaxing day, no life lost.",
        ]
        event = random.choice(events)
        messagebox.showinfo("Random Event", event)

        if "lost a life" in event:
            self.student['life'] -= 1
        elif "gained a life" in event:
            self.student['life'] += 1

        self.update_life()

    def heal_student(self):
        self.animate_circle(direction="left")
        self.student['life'] += 1
        messagebox.showinfo("Heal", f"{self.student['name']} gained 1 life!")
        self.update_life()

    def update_life(self):
        self.life_label.config(text=f"Life: {self.student['life']}")
        if self.student['life'] <= 0:
            self.end_game()

    def end_game(self):
        if self.student['life'] <= 0:
            messagebox.showinfo("Game Over", f"Game over! {self.student['name']}'s life has reached 0.")
        else:
            messagebox.showinfo("Game Ended", f"{self.student['name']} has {self.student['life']} life remaining.")
        self.start_screen()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# Main
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentGame(root)
    root.mainloop()
