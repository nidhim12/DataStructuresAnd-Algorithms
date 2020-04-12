class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        current = self.head
        while current.next!=None:
            current = current.next
        current.next = new_node

    def length(self):
        current = self.head
        total = 0
        while current.next != None:
            current = current.next
            total += 1
        return total

    def display(self):
        elem = []
        current = self.head
        while current.next != None:
            current = current.next
            elem.append(current.data)
        print(elem)

    def get(self, index):
        if index > self.length():
            print("ERROR: 'Get' index out of range!")
            return None
        curr_idx = 0
        current = self.head
        while current.next != None:
##        while True:
            current = current.next
##            curr_idx += 1
            if curr_idx == index:
                return current.data
            curr_idx += 1

    def delete(self, index):
        if index > self.length():
            print("ERROR: 'Get' index out of range!")
            return None
        curr_idx = 0
        current = self.head
        while True:
            last = current
            current = current.next
            if curr_idx == index:
                last.next = current.next
                return
            curr_idx += 1


        
my_list = linked_list()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

my_list.display()
                
            
        
