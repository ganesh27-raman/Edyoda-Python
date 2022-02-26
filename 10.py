from collections import deque
 
 
class MinStack:
    def __init__(self):
        self.s = deque()
        self.min = None
 
    def push(self, val):
        if not self.s:
            self.s.append(val)
            self.min = val
        elif val > self.min:
            self.s.append(val)
        else:
            self.s.append(2*val - self.min)
            self.min = val
 
    def pop(self):
        if not self.s:
            self.print('Stack underflow!!')
            exit(-1)
        top = self.s[-1]
        if top < self.min:
            self.min = 2*self.min - top
        self.s.pop()
 
    def getMin(self):
        return self.min
 
 
if __name__ == '__main__':
 
    s = MinStack()
 
    s.push(6)
    print(s.getMin())
 
    s.push(7)
    print(s.getMin())
 
    s.push(5)
    print(s.getMin())
 
    s.push(3)
    print(s.getMin())
 
    s.pop()
    print(s.getMin())
 
    s.pop()
    print(s.getMin())