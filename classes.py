my_string = "Hello, world"
print(type(my_string))
#<class 'str'> -ekzemplyar classa
print(type(str))
#<class 'type'> -class

class MyClass:
    pass

print(type(MyClass))
print(type(str))

#<class 'type'>
#<class 'type'>

my_class = MyClass()
print(type(MyClass))
print(type(my_class))

#<class '__main__.MyClass'>

class Ork: 
    def __init__(self, level:int) -> None:
#self - экземпляр класса
        self.level = level
        self.health_points = 100 * level
        self.attack_power = 100 * level

    def attack(self):
        print(f"Ork attacks with {self.attack_power} power")    

    def __str__(self):
        return f"Ork (level: {self.level}), hp: {self.health_points}"    

ork = Ork(level=1)
print(ork.level)        
print(ork.health_points)
print(ork.attack_power)
ork.attack()
print(ork)

#1
#100
#100
#Ork attacks with 100 power

ork.level += 1
print(ork.level)
#2

#Ork (level: 1), hp: 100

