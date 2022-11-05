class Animals:
    alive = True

    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")


class Rabbit(Animals):
    def run(self):
        print("This rabbit is running")
class Fish(Animals):
    def swim(self):
        print("This fish is swimming")
class Hawk(Animals):
    def fly(self):
        print("This hawk is flying")


rabbit  = Rabbit()
fish    = Fish()
hawk    = Hawk()

print(rabbit.alive)