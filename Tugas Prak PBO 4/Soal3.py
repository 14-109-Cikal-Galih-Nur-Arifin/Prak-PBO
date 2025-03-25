from abc import ABC, abstractmethod

# Exception Class for invalid animal
class InvalidAnimalError(Exception):
    pass

# Abstract class Animal
class Animal(ABC):
    def __init__(self, name, age):
        self.__name = name  # Enkapsulasi
        self.__age = age    # Enkapsulasi

    # Getter method
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age

    # Setter method
    def set_name(self, name):
        self.__name = name
    
    def set_age(self, age):
        self.__age = age

    @abstractmethod
    def make_sound(self):  # Method abstrak
        pass

# Class specific animals inheriting from Animal
class Dog(Animal):
    def make_sound(self):
        return "Bark!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"

# Zoo Management System
class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        if not isinstance(animal, Animal):
            raise InvalidAnimalError("Invalid animal type.")
        self.animals.append(animal)
        print(f"{animal.get_name()} has been added to the zoo.")

    def list_animals(self):
        for animal in self.animals:
            print(f"Name: {animal.get_name()}, Age: {animal.get_age()}, Sound: {animal.make_sound()}")

# Example usage
def main():
    zoo = Zoo()

    try:
        dog = Dog("A", 3)
        cat = Cat("B", 2)
        cow = Cow("C", 5)

        zoo.add_animal(dog)
        zoo.add_animal(cat)
        zoo.add_animal(cow)

        # Trying to add an invalid animal
        zoo.add_animal("NotAnAnimal")  # This should raise an error

    except InvalidAnimalError as e:
        print(e)

    zoo.list_animals()

if __name__ == "__main__":
    main()