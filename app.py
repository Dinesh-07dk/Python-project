class Prey:
    def flee(self):
        print('the Animal is Fleeing')

class Predator:
    def hunt(self):
        print('the Animal is Hunting')
class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey,Predator):
    pass

rabbit=Rabbit()
hawk=Hawk()
fish=Fish()

rabbit.flee()
hawk.hunt()
print()
print('The Fish Can be both prey and predator ')
fish.flee()
fish.hunt()
print("This is Python Multiple Inheritance...")
