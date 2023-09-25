class Person:
    # 속성(변수)
    blood_color = 'red'

    # 메서드
    def __init__(self, name): ## initialize 초기화
        self.name = name ## magic method, constructor method
    
    def singing(self):
        return f'{self.name}가 노래합니다.'
    
    def eat(self, food):
        return f'{self.name} eats {food}'
    
singer1 = Person('iu')
singer2 = Person('bts')
print(singer2.eat('coke'))
print(singer1.blood_color)
print(singer2.blood_color)