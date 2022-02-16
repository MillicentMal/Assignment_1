# implementation of Undoable ordered list

class Node:
    """Node with prev and next pointers
    """
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class OrderedList:
    """
    Ordered list that takes in a value and inserts it in a position such that it is ordered
    """
    def __init__(self):
        self.head = None
        self.undoStack = [] # store undo operations
        self.redoStack = [] # store redo operations

    def insert(self, value):
        """Insets value into the list in an orderly manner
        if list is [1, 2, 3] and value is insert calling self.insert(-1) will give the list as  [-1, 1, 2, 3]
        

        Args:
            value (_int_): _a value to insert into the ordered list_
            
        """
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.value > value:
                stop = True
            else:
                previous = current
                current = current.next

        temp = Node(value)
        if previous == None:
            temp.next = self.head
            self.head = temp
        else:
            temp.next = current
            previous.next = temp
            # inserting the method into our undoStack so that we can easily pop items
        undoItem  = ('insert', value)
        self.undoStack.append(undoItem)
        
    
    def print(self):
        # to print a list representation of our LinkedList
        ordered = []
        if self.head == None:
            return None
        else:
            current = self.head
            while current != None:
                ordered.append(current.value)
                current = current.next
        return ordered
    
    def delete(self, value):
        """Deletes value

        Args:
            value (int): is deleted if found

        Raises:
            ValueError: If value is not found
        """
        try:
            if self.head == None:
                return
            elif self.head.value == value:
                self.prevVersion = self.print()
                self.head.prev = None
                self.head = self.head.next
                return
            current = self.head
            while current.next:
                if current.next.value == value:
                    current.next = current.next.next
                    undoItem  = ('delete', value)
                    self.undoStack.append(undoItem)
                    return self.prevVersion
                current = current.next
        except ValueError:
            return "value not in list"
    

    
    def undo(self):
        """Undo undoes the last operation on our list

        Returns:
        : None 
        """
        if len(self.undoStack) == 0:
            return "Nothing to undo"
        toUnDo = self.undoStack[-1]        
        if toUnDo[0] == 'insert':
            print(toUnDo[1])
            self.delete(toUnDo[1])
            item = self.undoStack.pop()
            self.redoStack.append(item)
        elif toUnDo[0] == 'delete':
            self.insert(toUnDo[1])
            item = self.undoStack.pop()
            self.redoStack.append(item)
    
    def redo(self):
        """Redoes the operation that was cancelled by undo

        Returns:
            None_
        """
        if len(self.redoStack) == 0:
            return "Nothing to redo"
        toReDo = self.redoStack[-1]
        if toReDo[0] == 'insert':
            self.insert(toReDo[1])
        elif toReDo[0] == 'delete':
            self.delete(toReDo[1])
        self.redoStack.pop()
