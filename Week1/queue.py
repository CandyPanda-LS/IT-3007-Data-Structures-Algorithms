#implementing the queue data structure
class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[len(self.items)-1]
    def __str__(self):
        return str(self.items)

#Create  a student class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return self.name + " " + str(self.age)

#Create a queue of students
q = Queue()
q.enqueue(Student("John", 21))
q.enqueue(Student("Mary", 22))
q.enqueue(Student("Peter", 23))

#use the __str__ on the queue
print(q)

#peek the top student
print(q.peek())

#size of the queue
print(q.size())

#Print the queue
while not q.isEmpty():
    print(q.dequeue())


