def my_decorator(func):
    def wrapper(*args, **kwards):
        print("Something is happening before the function is called.")
        func(*args, **kwards)
        print("Something is happening after the function is called")

    return wrapper

@my_decorator
def say_hello(*, name: str) -> None:
    print(f"Hello, {name}!")    


say_hello(name="Sasha")    

#Something is happening before the function is called.
#Hello, Sasha!
#Something is happening after the function is called


def my_decorator2(func):
    def wrapper(*args, **kwargs):
        print("BEFORE")
        result = func(*args, **kwargs)
        print("AFTER")
        return result
    
    return wrapper

@my_decorator2
def add_numbers(*, a:int, b:int) -> int:
    print("ading numbers ...")
    return a+b

result = add_numbers(a=1, b=2)
print(result)

#BEFORE
#ading numbers ...
#AFTER
#3