def greating(name):
    print("Hello," + name )


greating("alice!")


def greetings():
    print(f"Hi mosh hamidani")

greetings()


def get_greting(fist_name, last_name):
    print(f"Hi {fist_name} {last_name}")
    print("good to see you" )

get_greting("Akorede", "Mujaheed")



def greeting(name):
    return (f"Hi {name}")

Message=greeting("Akorede")

print(Message)


def save_user(**user):
    print(user["name"])


save_user(id=1, name="john", age=22)
