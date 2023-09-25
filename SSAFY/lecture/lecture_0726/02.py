class Person:
    count = 0
    name = 'unknown'
    def __init__(self, name):
        self.name = name
        Person.count += 1
    def talk(self):
        print(self.name)

p1 = Person()
p1.talk() # unknown
# p2 인스턴스 변수 설정 전/후

p2 = Person()
p2.talk() #unknown
p2.name = 'Kim'
p2.talk() #Kim

print(Person.name) # unknown
print(p1.name) # unknown
print(p2.name) # Kim

## instance *변수*가 없어서 *class 변수*로 찾아 올라가는 방식은 좋은 방식이 아닙니다. 예시임. 하지마셈.

p1.address = 'korea' ## instance 변수. p1에만 있음 // 독립적!!!
print(p1.address)    ## 잘 나옴


# class method
## def with @classmethod decorator @classmethod라는 method를 불러오는형식이라네요.. 안의 인자로 def를 넣는 방식
## 인스턴스 상태에 의존하지 않는 기능
## 클래스 변수 조작 등의 클래스 레벨의 동작

# static method
## def with @staticmethod decorator
## only 기능(행동)만 수행