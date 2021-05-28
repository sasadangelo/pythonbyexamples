class Dog:
    # Class Attribute
    species = 'mammal'
    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

def get_biggest_dog(*dogs):
    oldest_dog=Dog("", 0)
    for dog in dogs:
        if dog.age > oldest_dog.age:
            oldest_dog=dog
    return oldest_dog

oldest_dog=get_biggest_dog(Dog("poppy", 15), Dog("pluto", 10), Dog("pippo", 16))
print("The oldest dog ", oldest_dog.name, " is ", oldest_dog.age , " years old")
