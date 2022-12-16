#implementing the stack data structure
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

#Create  a student class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return self.name + " " + str(self.age)

#Create a stack of students
s = Stack()
s.push(Student("John", 21))
s.push(Student("Mary", 22))
s.push(Student("Peter", 23))

#peek the top student
print(s.peek())

#size of the stack
print(s.size())

#Print the stack
while not s.isEmpty():
    print(s.pop())
