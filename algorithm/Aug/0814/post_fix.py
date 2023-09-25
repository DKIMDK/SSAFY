'''
(6+5*(2-8)/2)
6528-*2/+

'''

stack = [0] * 100
top = -1

icp = {'(' : 3, '*' : 2, '+' : 1 , '-' : 1}
isp = {'(' : 0, '*' : 2, '+' : 1 , '-' : 1}
fx = '(6+5*(2-8)/2'
s = '6528-*2/+'
for x in s:
    if not in '+-/*':
        top += 1
        stack[top] = int(x)
    else:
        op1 = stack[top] # pop
        top -= 1
        op2 = stack[top]    # pop
        top -= 1
        if x == '+': # op2 + op1
            top += 1
            stack[top] = op1 + op2
        elif x == '-':
            top += 1
            stack[top] = op1 - op2

        elif x == '/':
            top += 1
            stack[top] = op1 / op2

        elif x == '*':
            top += 1
            stack[top] = op1 * op2

stack = [0] * 100
top = -1

for x in fx:
    if x not in '(+-*/)':
        s += x
    elif x == ')':
        while stack[top] != '(':    # peek
            s += stack[top]
            top -= 1
        top -= 1                    # '(' 버림. pop

    else:
        if top == -1 or isp[stack[top]] < icp[x]:
            top += 1
            stack[top] = x
        elif isp[stack[top]] >= icp[x]:
            while top -1 and isp[stack[top]] >= icp[x]:
                s += stack[top]
                top -= 1
            top += 1
            stack[top] = x