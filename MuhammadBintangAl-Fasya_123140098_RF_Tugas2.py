import random #random untuk memberikan nilai acak dari serangan, akurasi, crtitical, stun, dan heal

# Kelas Robot 
class Robot:
    def __init__(self, name, hp, attack, defense, accuracy):
        #atribut robot
        self.name = name  # Nama 
        self.hp = hp  # Health Points / Nyawa
        self.attack = attack  # Serangan
        self.defense = defense  # Pertahanan
        self.accuracy = accuracy  # Akurasi
        self.ultimate_cooldown = 0  # Cooldown Ultimate
        
    def is_alive(self):
        return self.hp > 0
    
    def attack_enemy(self, enemy):
        if random.random() < self.accuracy:
            damage = self.attack - enemy.defense
            if damage < 0:
                damage = 0

            # Memberikan critical hit 
            if random.random() < 0.2: # Peluang berhasil 20%
                damage *= 2
                print("Serangan Kritis!")

            enemy.hp -= damage
            if enemy.hp < 0:
                enemy.hp = 0
            print(f"{self.name} menyerang {enemy.name} sebesar {damage}. HP {enemy.name}: {enemy.hp}")
        else:
            print(f"------------ {self.name} gagal menyerang ----------------")

    # Skill Heal
    def heal_self(self):
        heal_amount = random.randint(10, 20) # Dapat memulihkan HP sebesar 10-20
        self.hp += heal_amount
        print(f"{self.name} melakukan penyembuhan sebesar {heal_amount}. HP sekarang: {self.hp}") 
    
    # Skill ulti
    def ultimate_enemy(self, enemy):
        if self.ultimate_cooldown > 0:
            print(f"{self.name} tidak dapat menggunakan Ultimate! Cooldown: {self.ultimate_cooldown} ronde lagi.")
            return False
        if random.random() < 0.7:  # Peluang berhasil 70%
            damage = self.attack * 4  # Ultimate menghasilkan 4x damage
            enemy.hp -= damage
            self.ultimate_cooldown = 3  # Set cooldown setelah penggunaan
            print(f"{self.name} berhasil menggunakan Ultimate pada {enemy.name}! Damage: {damage}. HP {enemy.name}: {enemy.hp}")
            return True
        else:
            print(f"{self.name} gagal menggunakan Ultimate pada {enemy.name}!")
            self.ultimate_cooldown = 3  # Tetap cooldown meskipun gagal
            return False

    def reduce_cooldown(self):
        if self.ultimate_cooldown > 0:
            self.ultimate_cooldown -= 1   
        
# Kelas Game
class Game:
    def start_battle(self, prabowo, anies):
        round_number = 1
        while prabowo.is_alive() and anies.is_alive():
            print(f"\nRound-{round_number} ==========================================================")
            print(f"{prabowo.name} [{prabowo.hp}|{prabowo.attack}]")
            print(f"{anies.name} [{anies.hp}|{anies.attack}]")

            # Aksi Robot Prabowo
            prabowo.reduce_cooldown()
            action1 = 0
            while action1 not in [1, 2, 3, 4]:
                print("1. Attack     2. Heal    3. Ultimate      4. Giveup")
                try:
                    action1 = int(input(f"{prabowo.name}, pilih aksi: "))
                    if action1 == 1:
                        prabowo.attack_enemy(anies)
                    elif action1 == 2:
                        prabowo.heal_self()
                    elif action1 == 3:
                        prabowo.ultimate_enemy(anies)
                    elif action1 == 4:
                        print(f"\n{anies.name} menang!")
                        return
                    else:
                        print("Pilihan tidak valid! Masukkan angka 1-4.")
                except ValueError:
                    print("Input tidak valid! Masukkan angka 1-4.")

            # Cek apakah Anies masih hidup
            if not anies.is_alive():
                print(f"\n{prabowo.name} menang!")
                return

            # Aksi Robot Anies
            anies.reduce_cooldown()
            action2 = 0
            while action2 not in [1, 2, 3, 4]:
                print("\n1. Attack     2. Heal    3. Ultimate      4. Giveup")
                try:
                    action2 = int(input(f"{anies.name}, pilih aksi: "))
                    if action2 == 1:
                        anies.attack_enemy(prabowo)
                    elif action2 == 2:
                        anies.heal_self()
                    elif action2 == 3:
                        anies.ultimate_enemy(prabowo)
                    elif action2 == 4:
                        print(f"\n{prabowo.name} menang!")
                        return
                    else:
                        print("Pilihan tidak valid! Masukkan angka 1-4.")
                except ValueError:
                    print("Input tidak valid! Masukkan angka 1-4.")

            # Cek apakah Prabowo masih hidup
            if not prabowo.is_alive():
                print(f"\n{anies.name} menang!")
                return

            round_number += 1
        print("\nPertarungan Selesai!")
        if prabowo.is_alive():
            print(f"{prabowo.name} menang!")
        else:
            print(f"{anies.name} menang!")
            
# Membuat objek robot
prabowo = Robot("Prabowo", 164, 20, 10, 0.5859)
anies = Robot("Anies", 164, 20, 10, 0.2495)
# Memulai pertarungan
game = Game()
game.start_battle(prabowo, anies)

            
    