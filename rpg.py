import random

playerStats = { # [health, maxHealth]
   "health": [100, 100],
   "damage": 1,
   "armor": 0,
   "level": 1,
   "xp": 0,

   "weaponsEquipped": ["none", "none", "none"],
   "armorEquipped": "none"
}

weapons = { # [damage, speed, fire, ice, poison]
   "none": [0, 0, 0, 0, 0],
   "sword": [10, 10, 0, 0, 0]
}

def playerAttack(playerStats, enemyStats):

   damage = playerStats["damage"] + weapons[playerStats["weaponsEquipped"][int(input("Which weapon would you like to use? 1, 2, or 3? ")) - 1]][0] + random.randint(0, 5)

   enemyStats["health"][0] -= damage
   print(f"You dealt {damage} damage to the enemy. The enemy has {enemyStats['health'][0]} health left.")

def enemyAttack(playerStats, enemyStats):

   damage = enemyStats["damage"] + weapons[enemyStats["weaponEquipped"]][0] + random.randint(0, 5)

   playerStats["health"][0] -= damage
   print(f"The enemy dealt {damage} damage to you. You have {playerStats['health'][0]} health left.")

def attack(playerStats, enemyStats):
   playerAttack(playerStats, enemyStats)
   enemyAttack(playerStats, enemyStats)

enemyStats = {
   "health": [15, 15],
   "damage": 1,
   "armor": 0,

   "weaponEquipped": "none",
   "armorEquipped": "none",
}

print("")
attack(playerStats, enemyStats)
print("")