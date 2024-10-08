class stack:
    def __init__(self):
        self.data = []

    def isEmpty(self):
        return (len(self.data) == 0)

    def push_right(self, data):
        self.data.append(data)
    
    def push_left(self, data):
        self.data.insert(0, data)
    
    def pop_left(self):
        if not self.isEmpty():
            return(self.data.pop(0))
        return None

    def pop_right(self):
        if not self.isEmpty():
            return(self.data.pop())
        return None

    def stack_data(self):
        return (self.data)

class tbox:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.boxes = [[stack() for _ in range(col)] for _ in range(row)]

    def add_data(self, tround):
        i = 1
        for _ in range(tround):
            for row in range(self.row):
                for col in range(self.col):
                    self.boxes[row][col].push_right(f"{i}")
                    i += 1
    
    def pop_data(self):
        i = 1
        for row in range(self.row):
            for col in range(self.col):
                print(f"Box ({i}) :", end="")
                while not self.boxes[row][col].isEmpty():
                    print(self.boxes[row][col].pop_left(), end=" ")
                i += 1
                print()

Tbox = tbox(2, 3)
Tbox.add_data(3)
Tbox.pop_data()