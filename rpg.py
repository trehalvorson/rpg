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

weapons = { # [damage, speed, fire, ice, poison]
   "Fists": [0, 0, 0, 0, 0],
   "sword": [10, 10, 0, 0, 0]
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
   damage = (playerStats["damage"] + weapons[chosenWeapon][0]) * random.uniform(1, 2)

   enemyStats["health"][0] -= damage

   print("")

   if chosenWeapon == "Fists":
      print("You punched the enemy!")
   else:
      print(f"You used a {chosenWeapon}!")

   healthBar(enemyStats["health"][0], enemyStats["health"][1])
   print(f"Enemy Health: {math.ceil(enemyStats['health'][0])}/{enemyStats['health'][1]}")
   print("")

def enemyAttack(playerStats, enemyStats):

   damage = enemyStats["damage"] + weapons[enemyStats["weaponEquipped"]][0] + random.randint(0, 5)

   playerStats["health"][0] -= damage

   print("")

   if enemyStats["weaponEquipped"] == "Fists":
      print("The enemy punched you!")
   else:
      print(f"The enemy used a {enemyStats['weaponEquipped']}!")
   
   healthBar(playerStats["health"][0], playerStats["health"][1])
   print(f"Player Health: {math.ceil(playerStats['health'][0])}/{playerStats['health'][1]}")

def attack(playerStats, enemyStats):

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