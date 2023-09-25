'''
가능한 날짜가 총 몇 개가 있는지 알려주는 프로그램을 작성하시오.
[세부사항]
1. 10, 11, 12월은 두 자릿수로 표현하고, 1~9월은 한 자릿수로 표현한다.
2. 년도는 네 자리로 표현한다.
3. 날짜는 모든 달이 1~31일 이라고 가정한다. 1~9일은 한 자릿수로 표현한다.
4. 년도 부분에 찢어질 수 도 있지만, 년도가 찢어지는 것은 무시한다.
5. X의 개수는 최대 8개까지 될 수 있다.
[입력가능 예시]
202X.1X.XX
2XXX.XX.X
2001.X.XX
2033.8.3X

[입력]
첫 번째 줄에 Y,M,D의 형식으로 날짜 정보가 주어집니다.
[출력]
가능한 날짜의 개수를 출력합니다.
'''
calendar = input()
YY, MM, DD = calendar.split('.')
if MM == 'X':
    m_count = 9
elif MM == '1X' or MM == 'XX':
    m_count = 3
else:
    m_count = 1

if len(DD) == 2:
    if DD == 'XX':
        d_count = 22
    elif DD[1] == 'X':
        d_count = 10
    elif DD[0] == 'X':
        if DD[1] == '1' or DD[1] == '0':
            d_count = 3
        else:
            d_count = 2
    else:
        d_count = 1
else:
    if DD == 'X':
        d_count = 9
    else:
        d_count = 1


ans = d_count * m_count
print(ans)


