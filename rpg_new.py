import random
import math

class Character:
   def __init__(self, name, health, maxHealth, damage, defense, weapons, armor, level, xp, energy):

      self.name = name
      self.health = health
      self.maxHealth = maxHealth
      self.damage = damage
      self.defense = defense
      self.weapons = weapons
      self.armor = armor
      self.level = level
      self.xp = xp
      self.energy = energy

   def healthBar(self):
      
      # write = for each 20th of max health remaining
      for i in range(0, math.ceil(self.health / self.maxHealth * 20)):
         print("=", end="")

      # write - for each 20th of max health taken
      for i in range(0, 20 - math.ceil(self.health / self.maxHealth * 20)):
         print("-", end="")
   
      print("")
      print(f"{self.name} (LVL {self.level}) Health: {math.ceil(self.health)}/{self.maxHealth}")
      print("")

   def attack(self, enemy): # One attack from one side in a battle

      chosenWeapon = self.weapons

      # Select weapon to use
      if self.name == "You":

         #print(f"Your Energy: {self.energy}, Enemy's Energy: {enemy.energy}")
         print("Your weapons:")
         for i in range(3):
            print(f"{i + 1}. {self.weapons[i]}")
         chosenWeapon = self.weapons[int(input("Which weapon would you like to use? 1, 2, or 3? ")) - 1]

      damage = (self.damage + weapons[chosenWeapon][0]) / enemy.defense * random.uniform(0.8, 1.2)
      enemy.health -= damage
      self.energy -= weapons[chosenWeapon][1]

      print("")
      print(f"{self.name} used {chosenWeapon.lower()}!")

      enemy.healthBar()

      if enemy.health <= 0: # If someone in battle dies, end loop

         if enemy.name == "You": # If you died, do something idk

            print("You were defeated... You wake up in a nearby hospital...")
            print("")

         else: # If the enemy died, get xp

            print(f"{enemy.name} was defeated! You won the battle!")
            xpGained = math.ceil(enemy.maxHealth)
            print(f"You gained {int(xpGained)} EXP!")
            self.xp += xpGained
            levelUp()
            print(f"LVL {self.level} EXP {int(self.xp)}")
            print("")

      else: # Continue loop as opponent

         if enemy.energy >= self.energy:
            enemy.attack(self)
         else:
            self.attack(enemy)
         
def encounter(): # Set stats to random values and start attack against Slime

   health = random.randint(8, 12)
   damage = random.uniform(0.8, 1.2)
   defense = random.uniform(0.8, 1.2)

   enemy = Character("Slime", health, health, damage, defense, "Its Attack", "None", 1, 0, 0)
   print(f"{enemy.name} is attacking!")
   enemy.healthBar()

   player.energy = 0
   enemy.energy = 0

   player.attack(enemy)

def levelUp():

   # If xp is above threshold, level up
   if player.xp >= player.level:

      print("Level up!")
      player.xp -= player.level
      player.level += 1

      stat = random.randint(0, 2)
      if stat == 0:

         player.health += player.health / player.maxHealth
         player.maxHealth += 1
         print("+1 Health")

      elif stat == 1:

         player.damage += 1
         print("+1 Damage")

      else:

         player.defense += 1
         print("+1 Defense")

      levelUp()

weapons = { # [damage, speed, fire, ice, poison]
   
"Your Fists": [0, 1, 0, 0, 0],
"Its Attack": [0, 1.5, 0, 0, 0],
"A Sword": [6, 3, 0, 0, 0]

}

#                 name hlth maxH dmg def                  weapons                  armor level xp eng
player = Character("You", 10, 10, 2, 2, ["Your Fists", "Your Fists", "Your Fists"], "None", 3, 0, 0)

print("")
encounter()
encounter()
encounter()