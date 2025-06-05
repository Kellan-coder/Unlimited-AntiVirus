import random
import tkinter as tk
from tkinter import messagebox

class Virus:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.scanned = False

    def __str__(self):
        return f"{self.name} (difficulty {self.difficulty})"

class GameGUI:
    VIRUS_NAMES = [
        "Worminator",
        "Malbot",
        "SneakyTrojan",
        "AdwareZilla",
        "SpywarePro",
        "CryptoLock",
    ]

    def __init__(self, root):
        self.root = root
        self.stability = 5
        self.score = 0
        self.current_virus = None
        self.setup_ui()
        self.next_virus()

    def setup_ui(self):
        self.root.title("Infinite Antivirus")
        self.virus_label = tk.Label(self.root, text="")
        self.virus_label.pack(pady=10)

        info_frame = tk.Frame(self.root)
        info_frame.pack()
        self.stability_label = tk.Label(info_frame, text="Stability: 5")
        self.stability_label.pack(side=tk.LEFT, padx=10)
        self.score_label = tk.Label(info_frame, text="Score: 0")
        self.score_label.pack(side=tk.LEFT, padx=10)

        self.message_var = tk.StringVar(value="Welcome to Infinite Antivirus!")
        self.message_label = tk.Label(self.root, textvariable=self.message_var, wraplength=300)
        self.message_label.pack(pady=10)

        button_frame = tk.Frame(self.root)
        button_frame.pack()
        tk.Button(button_frame, text="Scan", width=8, command=self.scan).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(button_frame, text="Delete", width=8, command=self.delete).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(button_frame, text="Decode", width=8, command=self.decode).grid(row=0, column=2, padx=5, pady=5)
        tk.Button(button_frame, text="Pass", width=8, command=self.pass_virus).grid(row=0, column=3, padx=5, pady=5)
        tk.Button(button_frame, text="Help", width=8, command=self.show_help).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(button_frame, text="Quit", width=8, command=self.root.quit).grid(row=1, column=2, padx=5, pady=5)

    def help_text(self):
        return (
            "Commands:\n"
            "  scan   - analyze the current virus\n"
            "  delete - remove a scanned virus\n"
            "  decode - attempt to decode and neutralize the virus\n"
            "  pass   - skip this virus (costs 1 stability)\n"
            "  help   - show this help text\n"
            "  quit   - exit the game\n"
        )

    def next_virus(self):
        if self.stability <= 0:
            self.game_over()
            return
        name = random.choice(self.VIRUS_NAMES)
        difficulty = random.randint(1, 3)
        self.current_virus = Virus(name, difficulty)
        self.current_virus.scanned = False
        self.virus_label.config(text=f"Virus: {self.current_virus.name} (difficulty {self.current_virus.difficulty})")
        self.message_var.set("A wild virus appears!")

    def update_info(self):
        self.stability_label.config(text=f"Stability: {self.stability}")
        self.score_label.config(text=f"Score: {self.score}")

    def scan(self):
        self.current_virus.scanned = True
        self.message_var.set(f"Scanned {self.current_virus}")

    def delete(self):
        if not self.current_virus.scanned:
            self.message_var.set("You must scan before deleting!")
            return
        self.score += self.current_virus.difficulty
        self.update_info()
        self.message_var.set(f"Deleted {self.current_virus.name}!")
        self.next_virus()

    def decode(self):
        success = random.random() < (0.4 + 0.2 * self.current_virus.difficulty)
        if success:
            self.score += self.current_virus.difficulty * 2
            self.update_info()
            self.message_var.set(f"Successfully decoded {self.current_virus.name}!")
            self.next_virus()
        else:
            self.stability -= 1
            self.update_info()
            if self.stability <= 0:
                self.game_over()
            else:
                self.message_var.set(f"Failed to decode {self.current_virus.name}. It mutates!")
                self.current_virus.scanned = False

    def pass_virus(self):
        self.stability -= 1
        self.update_info()
        if self.stability <= 0:
            self.game_over()
        else:
            self.message_var.set(f"You ignored {self.current_virus.name}. It wreaks some havoc!")
            self.next_virus()

    def show_help(self):
        messagebox.showinfo("Help", self.help_text())

    def game_over(self):
        messagebox.showinfo("Game Over", f"Score: {self.score}")
        self.root.quit()


def main():
    root = tk.Tk()
    game = GameGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
