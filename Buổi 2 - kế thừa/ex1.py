# class A:
#     def sayHello(self):
#         print("Hello world!")
#     def intro(self):
#         print("I am a codeer")
# class B(A):
#     def age(self):
#         print("I am 20 years old")
#     def __str__(self):
#         return 

# student = B()
# student.sayHello()
# student.intro()
# student.age()
# Do class B co chung thuoc tinh voi class A ma class lai co nhieu hon 1 phuong thuc => class nen duoc ke thua tu class A
# Thêm một số thuộc tính vào class a bằng hàm khởi tạo __init__
# Sau đó tạo thêm một thuộc tính mới ở class con B .


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, {self.age} years old"

person = Person("Alice", 30)
print(person)  # Kết quả: Alice, 30 years old

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0
    
    def __len__(self):
        return len(self.items)

stack = Stack()
stack.push(5)
stack.push(10)
print(len(stack))  # Kết quả: 2

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

point1 = Point(1, 2)
point2 = Point(1, 2)
point3 = Point(3, 4)
print(point1 == point2)  # Kết quả: True
print(point1 == point3)  # Kết quả: False


class MyList:
    def __init__(self):
        self.items = []
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, value):
        self.items[index] = value

my_list = MyList()
my_list[0] = 10 
my_list[1] = 20
print(my_list[0])  # Kết quả: 10 lấy ra giá trị mà chúng ta muốn lấy/
print(my_list[1])  # Kết quả: 20