class Stacks:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, item):
        self.stack.append(item)

        if len(self.min_stack) == 0:
            self.min_stack.append(item)
        else:
            if self.min_stack[-1] > item:
                self.min_stack.append(item)
            else:
                self.min_stack.append(self.min_stack[-1])
    def pop(self):
        x = self.min_stack.pop()
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def peek_min(self):
        return self.min_stack[-1]
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    def size(self):
        return len(self.stack)
    def display(self):
        for i in self.stack[::-1]:
            print(i)
    def display_min_stack(self):
        for i in self.min_stack[::-1]:
            print(i)
    def reverse_stack(self):
        rev_stk = []
        while len(self.stack):
            temp = self.stack.pop()
            if len(rev_stk) == 0:
                rev_stk.append(temp)
            else:
                if rev_stk[-1] < temp:
                    while len(rev_stk):
                        self.stack.append(rev_stk.pop())
                rev_stk.append(temp)
        self.stack = rev_stk

    def insert_at_bottom(self, data):
        if self.isEmpty():
            self.push(data)
        else:
            temp = self.pop()
            self.insert_at_bottom(data)
            self.push(temp)

    def reverse(self):
        if not self.isEmpty():
            temp = self.pop()
            self.reverse()
            self.insert_at_bottom(temp)

    def my_sort(self):
        if not self.isEmpty():
            temp = self.pop()
            self.my_sort()
            self.insert_at_bottom(temp)

    def decode(self, my_str):
        ## 3[a2[c]]

        exp_str = ""
        for char in my_str:
            if char != ']':
                self.push(char)
            else:

                while self.stack and self.peek() != '[':

                    exp_str = self.pop() + exp_str
                self.pop()
                num = ""
                while self.stack and self.peek().isdigit():
                    num = self.pop() + num
                exp_str =  int(num) * exp_str
        return exp_str
