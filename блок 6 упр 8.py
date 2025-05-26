class Animal:
    def reply(self):
        self.speak()

class Mammal(Animal):
    pass

class Cat(Mammal):
    def speak(self):
        print("meow")

class Dog(Mammal):
    def speak(self):
        print("woof")

class Primate(Mammal):
    def speak(self):
        print("Hello")

class Hacker(Primate):
    pass


if __name__ == '__main__':
    spot = Cat()
    spot.reply()  

    data = Hacker()
    data.reply()  
