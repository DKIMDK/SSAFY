def enQ(data):
    global rear
    if rear == Qsize - 1:
        print('Q is full')
    else:
        rear += 1
        Q[rear] = data


def deQ():
    global front
    if front == rear:
       print('Q is empty')
       return -1

    else:
        front += 1
        return Q[front]

def isEmpty():
    return front == rear

def isFull():
    return rear == len(Q) - 1

def Qpeek():
    if isEmpty():
        print('Q is empty')
    else:
        return Q[front + 1]
Qsize = 3
Q = [0] * Qsize
front = -1
rear = -1

enQ(1)
enQ(2)
enQ(3)
# while front != rear:            # Q가 비어있지 않으면
#     front += 1
#     print(Q[front])             # deQ시 어떻게든 검사를 하는 것(비었는지)이 필요
# print(deQ())
# print(deQ())
# print(deQ())
print(Q)