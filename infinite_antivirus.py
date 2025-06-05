import random

class Virus:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.scanned = False

    def __str__(self):
        return f"{self.name} (difficulty {self.difficulty})"

class Game:
    VIRUS_NAMES = [
        "Worminator", "Malbot", "SneakyTrojan",
        "AdwareZilla", "SpywarePro", "CryptoLock",
    ]

    ACTIONS = ["scan", "delete", "decode", "pass", "help", "quit"]

    def __init__(self):
        self.stability = 5
        self.score = 0

    def generate_virus(self):
        name = random.choice(self.VIRUS_NAMES)
        difficulty = random.randint(1, 3)
        return Virus(name, difficulty)

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

    def play(self):
        print("Welcome to Infinite Antivirus!")
        print("Decode as many viruses as you can. Type 'help' for options.")
        while self.stability > 0:
            virus = self.generate_virus()
            print(f"\nA wild virus appears: {virus.name}!")
            while True:
                action = input("Action > ").strip().lower()
                if action not in self.ACTIONS:
                    print("Unknown command. Type 'help' for options.")
                    continue
                if action == "help":
                    print(self.help_text())
                    continue
                if action == "scan":
                    virus.scanned = True
                    print(f"Scanned {virus}.")
                    continue
                if action == "delete":
                    if virus.scanned:
                        print(f"Deleted {virus.name}!")
                        self.score += virus.difficulty
                        break
                    else:
                        print("You must scan the virus before deleting it!")
                        continue
                if action == "decode":
                    success = random.random() < (0.4 + 0.2 * virus.difficulty)
                    if success:
                        print(f"Successfully decoded {virus.name}!")
                        self.score += virus.difficulty * 2
                        break
                    else:
                        print(f"Failed to decode {virus.name}. It mutates!")
                        self.stability -= 1
                        if self.stability <= 0:
                            break
                        else:
                            print(f"System stability: {self.stability}")
                            virus.scanned = False
                            continue
                if action == "pass":
                    print(f"You ignored {virus.name}. It wreaks some havoc!")
                    self.stability -= 1
                    break
                if action == "quit":
                    self.stability = 0
                    break
            if self.stability <= 0:
                break
        print("\nGame over!")
        print(f"Score: {self.score}")

if __name__ == "__main__":
    Game().play()
