# class Person:
#     def __init__(self, name):
#         self.name = name
#         # self.age = age

#     def talk(self):
#         print(f'안녕 나는 {self.name}.')


# class Professor(Person):

#     def __init__(self, name, age, department):
#         # Person.__init__(self,name,age)
#         super().__init__(name, age)
#         self.department = department


# class Student(Person):

#     def __init__(self, name, age, gpa):
#         # Person.__init__(self,name,age)
#         super().__init__(name, age)
#         self.department = gpa


# # p1 = Professor('구교수', 44, '컴공')
# # s1 = Student('성학생', 44, 3.5)

# # p1.talk()
# # s1.talk()

# class Mom(Person):
#     gene = 'XX'

#     def swim(self):
#         return '엄마가 수영'


# class Dad(Person):
#     gene = 'XY'

#     def walk(self):
#         return '아빠가 걷기'


# class FirstChild(Dad,Mom):
#     def swim(self):
#         return '첫째가 수영'
    
#     def cry(self):
#         return '첫째가 응애'
    

# baby1 = FirstChild('아가')
# print(baby1.cry())
# print(baby1.swim())
# print(baby1.walk())
# print(baby1.gene)

class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
    def info(self):
        print(f'model : {self.model}, color : {self.color}')
    
class Hyundai(Car):
    color = 'white'
    def speed(self):
        return '80km/h'
class Kia(Car):
    color = 'black'
    def engine(self):
        return '1.6 turbo'
class CarDrive(Hyundai, Kia):
    def speed(self):
        return '100km/h'
    def power(self):
        return '1.999cc'


a = CarDrive('sonata','white')
a.info()
# print(a.speed()) ## overriding
# print(a.engine())
# print(a.power())
# print(a.color)
print(CarDrive.mro())
object