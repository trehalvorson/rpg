import random
import math

playerStats = { # [health, maxHealth]
   "health": [15, 15],
   "damage": 1,
   "armor": 0,
   "level": 1,
   "xp": 0,

   "weaponsEquipped": ["Fists", "Fists", "Fists"],
   "armorEquipped": "Fists"
}

weapons = { # [type, damage, speed, fire, ice, poison]
   "Fists": [0, 0, 0, 0, 0, 0],
   "Sword": [1, 10, 10, 0, 0, 0]
}

def healthBar(health, maxHealth):

   for i in range(0, math.ceil(health / maxHealth * 20)):
      print("=", end="")

   for i in range(0, 20 - math.ceil(health / maxHealth * 20)):
      print("-", end="")
   
   print("")

def playerAttack(playerStats, enemyStats):

   print("Your weapons:")
   for i in range(3):
      print(f"{i + 1}. {playerStats['weaponsEquipped'][i]}")
   chosenWeapon = playerStats["weaponsEquipped"][int(input("Which weapon would you like to use? 1, 2, or 3? ")) - 1]
   damage = (playerStats["damage"] + weapons[chosenWeapon][1]) * random.uniform(1, 2)

   enemyStats["health"][0] -= damage

   print("")

   if weapons[chosenWeapon][0] == 0:
      print(f"You punched the {enemyStats['species/name'].lower()}!")
   elif weapons[chosenWeapon][0] == 1:
      print(f"You used a {chosenWeapon.lower()}!")
   elif weapons[chosenWeapon][0] == 2:
      print(f"You used an {chosenWeapon.lower()}!")
   elif weapons[chosenWeapon][0] == 3:
      print(f"You used {chosenWeapon}!")

   healthBar(enemyStats["health"][0], enemyStats["health"][1])
   print(f"Enemy Health: {math.ceil(enemyStats['health'][0])}/{enemyStats['health'][1]}")
   print("")

def enemyAttack(playerStats, enemyStats):

   damage = enemyStats["damage"] + weapons[enemyStats["weaponEquipped"]][0] + random.randint(0, 5)

   playerStats["health"][0] -= damage

   print("")

   if weapons[enemyStats["weaponEquipped"]][0] == 0:
      print(f"The {enemyStats['species/name'].lower()} punched you!")
   elif weapons[enemyStats["weaponEquipped"]][0] == 1:
      print(f"The {enemyStats['species/name'].lower()} used a {enemyStats['weaponEquipped'].lower()}!")
   elif weapons[enemyStats["weaponEquipped"]][0] == 2:
      print(f"The {enemyStats['species/name'].lower()} used an {enemyStats['weaponEquipped'].lower()}!")
   
   healthBar(playerStats["health"][0], playerStats["health"][1])
   print(f"Player Health: {math.ceil(playerStats['health'][0])}/{playerStats['health'][1]}")

def attack(playerStats, enemyStats):

   print("")
   print(f"You encountered a {enemyStats['species/name'].lower()}!")
   print("")

   playerAttack(playerStats, enemyStats)
   enemyAttack(playerStats, enemyStats)

enemyStats = {
   "species/name": "Slime",
   "health": [15, 15],
   "damage": 1,
   "armor": 0,

   "weaponEquipped": "Fists",
   "armorEquipped": "Fists",
}

attack(playerStats, enemyStats)