def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called")
        func()
        print("Something is happening after the function is called.")


    return wrapper


def say_hello():
    print("Hello!")

my_decorator(say_hello)()    

#Something is happening before the function is called
#Hello!
#Something is happening after the function is called.

@my_decorator
def say_hello():
    print("Hello!")

#mydecorator(say_hello)()

say_hello()    


#Something is happening before the function is called
#Hello!
#Something is happening after the function is called.