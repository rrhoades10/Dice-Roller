import random


class Character():
    def __init__(self, strength, intelligence, wisdom, dexterity, constitution, charisma):
        self.strength = strength
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.dexterity = dexterity
        self.constitution = constitution
        self.charisma = charisma

    def roll_strength(self):
        dice_roll = random.randint(1, 20)
        print(f"Dice {dice_roll}")        
        if self.strength >= 30:
            dice_roll += 10
        elif self.strength >= 28:
            dice_roll += 9
        elif self.strength >= 26:
            dice_roll += 8
        elif self.strength >= 24:
            dice_roll += 7
        elif self.strength >= 22:
            dice_roll += 6
        elif self.strength >= 20:
            dice_roll += 5
        elif self.strength >= 18:
            dice_roll += 4
        elif self.strength >= 16:
            dice_roll += 3
        elif self.strength >= 14:
            dice_roll += 2
        elif self.strength >= 12:
            dice_roll += 1
        elif self.strength >= 10:
            dice_roll += 0
        elif self.strength >= 8:
            dice_roll -= 1
        elif self.strength >= 6:
            dice_roll -= 2
        elif self.strength >= 4:
            dice_roll -= 3
        elif self.strength >= 2:
            dice_roll -= 4
        else:
            dice_roll -= 5
         
        print(f"With modifier {dice_roll}")
    
    def roll_intelligence(self):
        dice_roll = random.randint(1, 20)
        print(f"Dice {dice_roll}")        
        if self.intelligence >= 30:
            dice_roll += 10
        elif self.intelligence >= 28:
            dice_roll += 9
        elif self.intelligence >= 26:
            dice_roll += 8
        elif self.intelligence >= 24:
            dice_roll += 7
        elif self.intelligence >= 22:
            dice_roll += 6
        elif self.intelligence >= 20:
            dice_roll += 5
        elif self.intelligence >= 18:
            dice_roll += 4
        elif self.intelligence >= 16:
            dice_roll += 3
        elif self.intelligence >= 14:
            dice_roll += 2
        elif self.intelligence >= 12:
            dice_roll += 1
        elif self.intelligence >= 10:
            dice_roll += 0
        elif self.intelligence >= 8:
            dice_roll -= 1
        elif self.intelligence >= 6:
            dice_roll -= 2
        elif self.intelligence >= 4:
            dice_roll -= 3
        elif self.intelligence >= 2:
            dice_roll -= 4
        else:
            dice_roll -= 5
         
        print(f"With modifier {dice_roll}")

    
    def roll_wisdom(self):
        dice_roll = random.randint(1, 20)
        print(f"Dice {dice_roll}")        
        if self.wisdom >= 30:
            dice_roll += 10
        elif self.wisdom >= 28:
            dice_roll += 9
        elif self.wisdom >= 26:
            dice_roll += 8
        elif self.wisdom >= 24:
            dice_roll += 7
        elif self.wisdom >= 22:
            dice_roll += 6
        elif self.wisdom >= 20:
            dice_roll += 5
        elif self.wisdom >= 18:
            dice_roll += 4
        elif self.wisdom >= 16:
            dice_roll += 3
        elif self.wisdom >= 14:
            dice_roll += 2
        elif self.wisdom >= 12:
            dice_roll += 1
        elif self.wisdom >= 10:
            dice_roll += 0
        elif self.wisdom >= 8:
            dice_roll -= 1
        elif self.wisdom >= 6:
            dice_roll -= 2
        elif self.wisdom >= 4:
            dice_roll -= 3
        elif self.wisdom >= 2:
            dice_roll -= 4
        else:
            dice_roll -= 5
         
        print(f"With modifier {dice_roll}")

    
    def roll_dexterity(self):
        dice_roll = random.randint(1, 20)
        print(f"Dice {dice_roll}")        
        if self.dexterity >= 30:
            dice_roll += 10
        elif self.dexterity >= 28:
            dice_roll += 9
        elif self.dexterity >= 26:
            dice_roll += 8
        elif self.dexterity >= 24:
            dice_roll += 7
        elif self.dexterity >= 22:
            dice_roll += 6
        elif self.dexterity >= 20:
            dice_roll += 5
        elif self.dexterity >= 18:
            dice_roll += 4
        elif self.dexterity >= 16:
            dice_roll += 3
        elif self.dexterity >= 14:
            dice_roll += 2
        elif self.dexterity >= 12:
            dice_roll += 1
        elif self.dexterity >= 10:
            dice_roll += 0
        elif self.dexterity >= 8:
            dice_roll -= 1
        elif self.dexterity >= 6:
            dice_roll -= 2
        elif self.dexterity >= 4:
            dice_roll -= 3
        elif self.dexterity >= 2:
            dice_roll -= 4
        else:
            dice_roll -= 5
         
        print(f"With modifier {dice_roll}")

    
    def roll_constitution(self):
        dice_roll = random.randint(1, 20)
        print(f"Dice {dice_roll}")        
        if self.constitution >= 30:
            dice_roll += 10
        elif self.constitution >= 28:
            dice_roll += 9
        elif self.constitution >= 26:
            dice_roll += 8
        elif self.constitution >= 24:
            dice_roll += 7
        elif self.constitution >= 22:
            dice_roll += 6
        elif self.constitution >= 20:
            dice_roll += 5
        elif self.constitution >= 18:
            dice_roll += 4
        elif self.constitution >= 16:
            dice_roll += 3
        elif self.constitution >= 14:
            dice_roll += 2
        elif self.constitution >= 12:
            dice_roll += 1
        elif self.constitution >= 10:
            dice_roll += 0
        elif self.constitution >= 8:
            dice_roll -= 1
        elif self.constitution >= 6:
            dice_roll -= 2
        elif self.constitution >= 4:
            dice_roll -= 3
        elif self.constitution >= 2:
            dice_roll -= 4
        else:
            dice_roll -= 5
         
        print(f"With modifier {dice_roll}")

    
    def roll_charisma(self):
        dice_roll = random.randint(1, 20)
        print(f"Dice {dice_roll}")        
        if self.charisma >= 30:
            dice_roll += 10
        elif self.charisma >= 28:
            dice_roll += 9
        elif self.charisma >= 26:
            dice_roll += 8
        elif self.charisma >= 24:
            dice_roll += 7
        elif self.charisma >= 22:
            dice_roll += 6
        elif self.charisma >= 20:
            dice_roll += 5
        elif self.charisma >= 18:
            dice_roll += 4
        elif self.charisma >= 16:
            dice_roll += 3
        elif self.charisma >= 14:
            dice_roll += 2
        elif self.charisma >= 12:
            dice_roll += 1
        elif self.charisma >= 10:
            dice_roll += 0
        elif self.charisma >= 8:
            dice_roll -= 1
        elif self.charisma >= 6:
            dice_roll -= 2
        elif self.charisma >= 4:
            dice_roll -= 3
        elif self.charisma >= 2:
            dice_roll -= 4
        else:
            dice_roll -= 5
         
        print(f"With modifier {dice_roll}")

    
        

player = Character(30, 15, 13, 12, 11, 10)

player.roll_charisma()

