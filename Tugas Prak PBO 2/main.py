import random

class Robot:
    def __init__(self, name, hp, attack_power, accuracy):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.max_hp = hp
        self.accuracy = accuracy 

    def attack_enemy(self, enemy):
        
        random_accuracy = random.uniform(0, 1)
         
        if random_accuracy <= self.accuracy:  
            enemy.hp -= self.attack_power
            print(f"{self.name} menyerang {enemy.name} dan menyebabkan {self.attack_power} damage!")
        else:
            print(f"{self.name} menyerang {enemy.name} tetapi serangannya meleset!")

    def regen_health(self, amount):
        if self.hp < self.max_hp:
            self.hp += amount
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            print(f"Helath {self.name} + {amount}. health total: {self.hp}/{self.max_hp}")
        else:
            print(f"{self.name} sudah dalam kondisi penuh. Health tidak bisa bertambah.")

    def is_alive(self):
        return self.hp > 0

    def display_status(self):
        print(f"{self.name} health: {self.hp}/{self.max_hp} | Attack power: {self.attack_power}")


class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.round = 1

    def play(self):
        while self.robot1.is_alive() and self.robot2.is_alive():
            print(f"\nRound-{self.round} ==========================================================")
            self.robot1.display_status()
            self.robot2.display_status()

            # Robot 1 turn
            action1 = self.get_action(self.robot1)
            if action1 == 1: 
                self.robot1.attack_enemy(self.robot2)
            elif action1 == 2:
                self.robot1.regen_health(5)

            if not self.robot2.is_alive():
                print(f"{self.robot1.name} menang!")
                break

            # Robot 2 turn
            action2 = self.get_action(self.robot2)
            if action2 == 1: 
                self.robot2.attack_enemy(self.robot1)
            elif action2 == 2:
                self.robot2.regen_health(5)

            if not self.robot1.is_alive():
                print(f"{self.robot2.name} menang!")
                break

            self.round += 1

    def get_action(self, robot):
        while True:
            try:
                print(f"{robot.name}, pilih aksi: ")
                print("1. Attack")
                print("2. Defense (Regenerate Health)")
                print("3. Giveup")
                action = int(input("Masukkan pilihan (1/2/3): "))
                if action in [1, 2, 3]:
                    if action == 3:
                        print(f"{robot.name} menyerah!")
                        exit()
                    return action
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka 1, 2, atau 3.")


robot1 = Robot("Atreus", 500, 10, 0.8)
robot2 = Robot("Daedalus", 750, 8, 0.7)

game = Game(robot1, robot2)
game.play()