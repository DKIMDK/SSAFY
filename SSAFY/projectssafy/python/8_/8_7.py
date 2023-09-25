class UserInfo:
    def __init__(self):
        pass

    def get_user_info(self):
        end = False
        while not end:
            try:
                self.name = str(input('이름을 입력하세요: '))
            
                self.age = int(input('나이를 입력하세요: '))
                end = True
            except ValueError:
                print('나이는 숫자로 입력해야 합니다.')
        

    def display_user_info(self):
        if self.name.strip() == '':
                    print('사용자 정보가 입력되지 않았습니다.')
        else: print(f'사용자 정보:\n이름: {self.name}\n나이: {self.age}')

u = UserInfo()
u.get_user_info()
u.display_user_info()
