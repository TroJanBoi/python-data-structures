class priNode:
    def __init__(self, data, next = None, secn = None):
        self.secn = secn
        self.data = data
        self.next = next

class secNode:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class twowaylinklist:
    def __init__(self):
        self.head = None

    def append_primary(self, pri_data):
        newNode = priNode(pri_data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def delete_primary(self, pri_data):
        current = self.head
        prev = None
        tmp = None
        while current:
            if current.data == pri_data:
                tmp = current
                break
            prev = current
            current = current.next
        if tmp is None:
            print(f"Node {pri_data} Not Found")
            return
        if prev:
            prev.next = tmp.next
        else:
            self.head = tmp.next
        current = None

    def append_secondary(self, pri_data, sec_data):
        current = self.head
        tmp = None
        while current:
            if current.data == pri_data:
                tmp = current
                break
            current = current.next
        if tmp is None:
            print(f"Node {pri_data} Not Found")
            return
        newNode = secNode(sec_data)
        if tmp.secn is None:
            tmp.secn = newNode
        else:
            sec_current = tmp.secn
            while sec_current.next:
                sec_current = sec_current.next
            sec_current.next = newNode
    
    def delete_secondary(self, pri_data, sec_data):
        current = self.head
        tmp = None
        while current:
            if current.data == pri_data:
                tmp = current
                break
            current = current.next
        if tmp is None:
            print(f"Node {pri_data} Not found")
            return
        sec_current = tmp.secn
        prevs = None
        sec_tmp = None
        while sec_current:
            if sec_current.data == sec_data:
                sec_tmp = sec_current
                break
            prevs = sec_current
            sec_current = sec_current.next
        if sec_tmp is None:
            print(f"Node {pri_data} Not Found")
            return
        if prevs:
            prevs.next = sec_tmp.next
        else:
            tmp.secn = sec_tmp.next
        sec_current = None

    def print_list(self):
        current = self.head
        while current:
            sec_tmp = current.secn
            lst = []
            while sec_tmp:
                lst.append(sec_tmp.data)
                sec_tmp = sec_tmp.next
            print(f"{current.data}: {', '.join(lst)}")
            current = current.next

lst = twowaylinklist()
lst.append_primary("A")
lst.append_primary("B")
lst.append_primary("C")
lst.append_secondary("B", "B1")
lst.append_secondary("B", "B2")
lst.append_secondary("A", "A1")
lst.append_secondary("A", "A2")
lst.append_secondary("C", "C1")
lst.append_secondary("C", "C2")
lst.print_list()