#implement a singlely linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)
class LinkedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def add(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.next
        return count
    def search(self, data):
        current = self.head
        found = False
        while current != None and not found:
            if current.data == data:
                found = True
            else:
                current = current.next
        return found
    def remove(self, data):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.data == data:
                found = True
            else:
                previous = current
                current = current.next
        if previous == None:
            self.head = current.next
        else:
            previous.next = current.next
    def __str__(self):
        current = self.head
        s = ""
        while current != None:
            s = s + str(current.data) + " "
            current = current.next
        return s

#Create a linked list
l = LinkedList()
l.add(1)
l.add(2)
l.add(3)

#Print the linked list
print(l)

#size of the linked list
print(l.size())

#search for an item
print(l.search(2))

#remove an item
l.remove(2)

