from rich import print

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def append_list(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode.next:
                currentNode = currentNode.next
            currentNode.next = newNode

    def prepend_list(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def find(self, data):
        if self.head == None:
            print("[red]Empty Link List[/red]")
            return
        else:
            currentNode = self.head
            while currentNode:
                if currentNode.data == data:
                    return currentNode.data
                currentNode = currentNode.next
            return None
    
    def insert_value(self, target, data):
        if self.head == None:
            print("[red]Empty Link List[/red]")
            return
        else:
            currentNode = self.head
            while currentNode:
                if currentNode.data == target:
                    newNode =  Node(data)
                    newNode.next = currentNode.next
                    currentNode.next = newNode
                    return
                currentNode = currentNode.next
            return None

    def delete_value(self, data):
        if self.head is None:
            print("[red]Empty Link List[/red]")
            return
        currentNode = self.head
        while currentNode.next:

            if currentNode.next.data == data:
                currentNode.next = currentNode.next.next
                return
            currentNode = currentNode.next
        return None

    def display(self):
        if self.head == None:
            print("[red]Empty Link List[/red]")
            return
        else:
            currentNode = self.head
            while currentNode:
                print(f"[green]{currentNode.data}[/green]")
                currentNode = currentNode.next


linklst = LinkList()

# Append All

print("[yellow]Function Append !![/yellow]")
linklst.append_list(10)
linklst.append_list(20)
linklst.append_list(30)
linklst.display()

print("[yellow]Function Prepend !![/yellow]")
linklst.prepend_list(5)
linklst.display()
 
print("[yellow]Fucntion Find !![/yellow]")
print(f"[green]find[/green]: {linklst.find(5)}")
print(f"[green]find[/green]: {linklst.find(300)}")

print("[yellow]Fucntion Insert Value !![/yellow]")
linklst.insert_value(20, 25)
linklst.display()

print("[yellow]Fucntion Delete Value !![/yellow]")
linklst.delete_value(25)
linklst.display()
