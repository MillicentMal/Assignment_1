# implementation of Undoable ordered list
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
    
    def getValue(self):
        return self.value
    
    def __repr__(self):
        return self.getValue()
    
    def __str__(self):
        return self.getValue()

class OrderedList:
    def __init__(self, value=None):
        self.head = value


    def add(self, value):
        stop = False
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            
        currentNode = self.head
        while currentNode.next is not None and not stop:
            if currentNode.getValue() > value:
                stop = True
            else:
                previous = currentNode
                currentNode = currentNode.next
        if currentNode is None:
            newNode.next = self.head
        else:
            newNode.next = currentNode
            
        
    def getItems(self):
        currentNode = self.head
        while currentNode.next is not None:
            currentNode.getValue()
            currentNode = currentNode.next
                    

    
first = OrderedList()
first.add(2)
first.add(12)
first.add(1)
print(first.getItems())
