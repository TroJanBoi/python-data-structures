from rich import print

class Stack:
    def __init__(self):
        self.stk = []

    def push(self, data):
        self.stk.append(data)
        return
    
    def pop(self):
        if self.isEmpty():
            return None
        return self.stk.pop()
        
    def peek(self):
        if self.isEmpty():
            return None
        return self.stk[-1]

    def size(self):
        return len(self.stk)

    def isEmpty(self):
        return len(self.stk) == 0
    
    def display(self):
        print(f"[green]Stack[/green]: {self.stk}")


stk = Stack()

for i in range(10):
    stk.push(i)
stk.display()

print(f"[yellow]peek[/yellow]: {stk.peek()}")
print(f"[yellow]size[/yellow]: {stk.size()}")
print(f"[yellow]pop[/yellow]: {stk.pop()}")
stk.display()

# RESULT
# Stack: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# peek: 9
# size: 10
# pop: 9
# Stack: [0, 1, 2, 3, 4, 5, 6, 7, 8]