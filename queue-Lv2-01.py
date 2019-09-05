# 최대 용량이 정해진 FIFO 큐 클래스

class MyStack(object):
    def __init__(self):
        self.lst = list()

    def push(self, x):
        self.lst.append(x)

    def pop(self):
        return self.lst.pop()

    def size(self):
        return len(self.lst)

class MyQueue(object):
    def __init__(self, max_size):
        self.stack1 = MyStack()
        self.stack2 = MyStack()
        self.max_size = max_size
        self.element = 0

    def qsize(self):
        self.size = len(stack1) + len(stack2)
        return self.size

    def push(self, item):
        if self.element >= self.max_size:
            print("False")
        else:
            self.stack1.push(item)
            self.element += 1
            print("True")

    def pop(self):
        if not stack2:
            for i in stack1:
                stack2.push(stack.pop())
            element -= 1
            print(stack2.pop())
        else:
            element -= 1
            print(stack2.pop())

  
n, max_size = map(int, input().strip().split(' '))
myQueue = MyQueue(max_size)
while n:
    instruction = []
    instruction = input().split()

    # instruction[1] = int(instruction[1])
    
    # PUSH
    if instruction[0] == 'PUSH':
        myQueue.push(instruction[1])
    # POP
    elif instruction[0] == 'POP':
        myQueue.pop()
    # SIZE
    elif instruction[0] == 'SIZE':
        myQueue.qsize()
