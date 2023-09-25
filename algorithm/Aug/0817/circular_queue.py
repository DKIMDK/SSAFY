front = rear = 0
Qsize = 4
Q = [0] * Qsize
## mod 연산자를 통해서
def enQ(data):
    global rear
    if isFull():
        print('Q is full')
    else:
        rear = (rear + 1) % Qsize
        Q[rear] = data
def deQ():
    global front
    if isEmpty():
        print('Q is empty')
        return -1
    else:
        front = (front + 1) % Qsize
        return Q[front]
def isEmpty():
    return front == rear
def isFull():
    return (rear + 1) % Qsize == front

enQ(1)
enQ(2)
enQ(3)
print(deQ())
enQ(4)