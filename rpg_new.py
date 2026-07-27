import random
import math

weapons = { # [type, damage, speed, fire, ice, poison]
"Your Fists": [0, 0, 0, 0, 0],
"Its Attack": [0, 0, 0, 0, 0],
"A Sword": [10, 10, 0, 0, 0]
}

class Character:
   def __init__(self, name, health, maxHealth, damage, defense, weapons, armor, level, xp):
      self.name = name
      self.health = health
      self.maxHealth = maxHealth
      self.damage = damage
      self.defense = defense
      self.weapons = weapons
      self.armor = armor
      self.level = level
      self.xp = xp

   def healthBar(self):
      
      for i in range(0, math.ceil(self.health / self.maxHealth * 20)):
         print("=", end="")

      for i in range(0, 20 - math.ceil(self.health / self.maxHealth * 20)):
         print("-", end="")
   
      print("")

   def attack(self, enemy):

      chosenWeapon = self.weapons

      if self.name == "You":
         print("Your weapons:")
         for i in range(3):
            print(f"{i + 1}. {self.weapons[i]}")
         chosenWeapon = self.weapons[int(input("Which weapon would you like to use? 1, 2, or 3? ")) - 1]
      damage = (self.damage + weapons[chosenWeapon][0]) * random.uniform(1, 2)

      enemy.health -= damage

      print("")
      print(f"{self.name} used {chosenWeapon.lower()}!")

      enemy.healthBar()
      print(f"{enemy.name} (LVL {enemy.level}) Health: {math.ceil(enemy.health)}/{enemy.maxHealth}")
      print("")
      
person = Character("You", 10, 10, 1, 0, ["Your Fists", "Your Fists", "Your Fists"], "None", 1, 0)
enemy = Character("Slime", 10, 10, 1, 1, "Its Attack", "None", 1, 0)
person.attack(enemy)
enemy.attack(person)