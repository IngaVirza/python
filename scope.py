def my_function():
    local_var = "I'm local variable"
    print(local_var)

my_function()    


COMFORTABLE_TEMPERATURE = 25

def get_diff_from_comfortable_temperature(*, temperature: int)-> int:
    return COMFORTABLE_TEMPERATURE - temperature
print(get_diff_from_comfortable_temperature(temperature=20))

#5

global_var = "I'm a global variable"

def my_function():
    global global_var
    global_var = "I defined inside inside the scope of my_function"

print(global_var)
my_function()
print(global_var)    

#I'm a global variable
#I defined inside inside the scope of my_function

DEFAULT_LEVEL_EXPERIENCE = 200
def is_leveled_up(*, current_experience: int, gained_experience: int) -> bool:
    total_experience = current_experience + gained_experience
    level_up = False

    if total_experience >= DEFAULT_LEVEL_EXPERIENCE:
        level_up = True

    return level_up

print(is_leveled_up(current_experience=150, gained_experience=60))
print(is_leveled_up(current_experience=10, gained_experience=60))
#True
#False