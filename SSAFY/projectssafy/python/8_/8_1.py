# ws_8_1.py

# 아래 클래스를 수정하시오.
class Animal:
    
    num_of_animals = 0

    def __init__(self):
        pass
    def __str__(self):
        pass

class Dog(Animal):
    sound = '멍멍!'
    def __init__(self):
        Animal.num_of_animals +=1

    def bark(self):
        print(self.sound)


class Cat(Animal):
    sound = '야옹!'
    def __init__(self):
        Animal.num_of_animals +=1
   
    def meow(self):
        print(self.sound)


class Pet(Dog, Cat):
    sound = ''
    def __init__(self, type):
        if type == Cat:
            Cat.__init__(self)
            self.sound = Cat.sound
        if type == Dog:
            self.sound = super().sound
            super().__init__()    
    def __str__(self):
        return f'애완동물은 {self.sound} 소리를 냅니다.'

    def play(self):
        print('애완동물과 놀기')

    def make_sound(self):
        print(self.sound)
    @classmethod
    def access_num_of_animal(cls):
        return f'동물의 수는 {Animal.num_of_animals}마리 입니다.'


pet1 = Pet(Cat)
print(pet1)
pet2 = Pet(Dog)
print(pet2)
print(Animal.num_of_animals)