try:
    num = int(input('100으로 나눌 값을 입력하세요: '))
    print(100 / num)
except (ValueError,ZeroDivisionError):
    print('정수를 입력하세요')
# except ZeroDivisionError:
#     print('0으로 나눌 수 없습니다')
except:
    print('무슨에러지')