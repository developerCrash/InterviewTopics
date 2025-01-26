class Stack:
    def __init__(self):
        self.my_stack = []
        self.max_stack = []
    def push(self, data):
        
        if len(self.my_stack) == 0 and len(self.max_stack) == 0:
            self.max_stack.append(data)
        else:
            if data > self.max_stack[-1]:
                self.max_stack.append(data)
            else:
                self.max_stack.append(self.max_stack[-1])
        self.my_stack.append(data)
    def pop(self):
        if len(self.my_stack):
            self.max_stack.pop()
            return self.my_stack.pop()
        else:
            raise Exception("Stack is empty")
    def display(self):
        for i in self.my_stack:
            print(i)
    def max_stacks(self):
        if len(self.max_stack):
            print( self.max_stack[-1])
        else:
            raise Exception("Stack is empty")
    
    

my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
my_stack.push(40)
my_stack.push(50)
my_stack.push(60)
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
my_stack.push(40)
my_stack.display()
print("\n")
my_stack.pop()
my_stack.display()
print("\n")
my_stack.max_stacks()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.display()
print("This is the max ")
my_stack.max_stacks()
