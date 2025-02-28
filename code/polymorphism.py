def petLover(animal):
    animal.talk()
    if hasattr(animal, 'walk'):
        animal.walk()

class Duck:
    def talk(self):
        print('duck is talking')
    
    def walk(self):
        print('duck is walking')

class Dog:
    def talk(self):
        print('dog is barking')

animalType = Duck()
petLover(animalType)