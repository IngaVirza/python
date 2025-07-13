class Character:
    def __init__(self, *, level:int) -> None:
        self.level = level
        self.health_points = self.base_health_points * level
        self.attack_power = self.base_attack_power * level
    def attack(self): 
        print(f"{self.character_name} attacks with {self.attack_power} power")    

    def __str__(self) -> str:
        return f"{self.character_name} (level:{self.level}, hp: {self.health_points})"    
    
class Ork(Character):
    base_health_points = 100
    base_attack_power = 10
    character_name = "Ork"    


ork_1 = Ork(level=1)
ork_1.attack()   
print(ork_1) 
#Ork attacks with 10 power
#Ork (level:1, hp: 100)


class Elf(Character):
    base_health_points = 400
    base_attack_power = 40
    character_name = "Elf"    

    def attack(self):
        print("This method is from class-inheritor")


elf_1 = Elf(level=1)
elf_1 .attack()   
print(elf_1 ) 

#This method is from class-inheritor
#Elf (level:1, hp: 400)
