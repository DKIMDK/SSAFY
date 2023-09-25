class Car:
    def __init__(self, model='default', color='default', speed='default'):
        self.model = model
        self.color = color
        self.speed = speed

    def speedchande(self, v):
        print(f"speed : {v}")
        self.speed = v

# 실습2 생성자 메서드로 바꾸기
car1 = Car()

# 실습3
class Person:
    job = '가수'
    birth = '1993.05.16'
    nat = 'Korea'
    @staticmethod
    def rap():
        print('불꽃카리스마민호')

    @staticmethod
    def dance():
        print('둠칫두둠칫')

    @staticmethod
    def cow_drive():
        print('워우워~')

new_k = Person()
print(new_k.nat)
new_k.rap()
new_k.dance()
new_k.cow_drive()

## magic method 실습
class Circle:

    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14*self.r**2
    
    def __str__(self):
        return f'[원] radius {self.r}'
    
c1 = Circle(3)
print(c1)

## decorator 실습

## dummy decorator
def my_decorator(func):
    def wrapper():
        print('함수 실행 전')
        #원본 함수 호출
        result = func()

        print('함수 실행 후')
        return result
    return wrapper

@my_decorator
def my_function():
    print('원본 함수 실행')
my_function()