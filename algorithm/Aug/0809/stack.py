# def push(item, size):
#     global top
#     top += 1
#     if top == size:
#         print('overFlow')
#     else:
#         stack[top] = item
#
# size = 10
# stack = [0] * size
# top = -1
#
# push(10, size)
# top += 1
# stack[top] = 20
#
# def pop(s):
#     if len(s) == 0:
#         # underflow
#         return
#     else:
#         return s.pop()
#
# def pop():
#     global top
#     if top == 1:
#         print('underflow')
#         return 0
#     else:
#         top -= 1
#         return stack[top + 1]
# print(pop())
#
# if top > -1:
#     top -= 1
#     print(stack[top+1])

# stack = [0] * 10
# top = -1
#
# top += 1        # push 1
# stack[top] = 1
# top += 1        # push 2
# stack[top] = 2
# top += 1        # push 3
# stack[top] = 3
# print(stack[top]) # pop()
# top -= 1
# top -= 1          # pop()
# print(stack[top+1])

# 괄호의 짝을 검사하는 프로그램 작성
'''
input::
()()((()))
({)}
}{

'''