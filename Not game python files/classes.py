
class Animal() :
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def eat(self, food):
        pass
    
    def sleep(self):
        print(f"{self.name} died")

class Tiger(Animal):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
    
    def eat(self, animal: Animal):
        if type(animal) != Animal:
            print("eat me bish")
        else: 
            print(f'{self.name} ate {self.age}')

class Cow(Animal):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)


class Dog(Animal):
    """This class makes a dog"""
    legs = 4
    tail = "wagging"
    def __init__(self, name, age, breed) -> None:
        self.age = age
        self.name = name
        self.breed = breed
    
    def speak(self):
        print(f"{self.name} says Woof wood!!")

    def have_birthday(self):
        self.age += 1
        print(f"{self.name} turned {self.age}")
    
    def __repr__(self):
        return f"{self.name} is a {self.age} year old {self.breed}"

daisy = Cow('daisy', 3)
jeff = Tiger('jeff', 5) 
daisy. sleep()

 
# my_dog = Dog(3, 'Steve', 'poddle')
# dog = Dog(2, 'Philip', 'German Sheppard')
# dog.tail = "still"

print()
