Tạo lớp kế thừa
Bạn có biết siêu nhân gao chứ? Siêu nhân gao là siêu nhân, tuy nhiên nó cũng không phải siêu nhân. Ý mình là, lớp siêu nhân cũng có thể miêu tả được siêu nhân gao, tuy nhiên một siêu nhân gao còn cần phải có một vài thứ khác để phân biệt với các siêu nhân khác mà ta không thể viết nó chung một lớp với các siêu nhân khác được vì như vậy sẽ thiếu một số đặc điểm riêng.

Vậy ý tưởng của ta là tạo ra một lớp mới là một lớp siêu nhân gao. Lớp này có đặc điểm là một lớp nâng cấp của lớp siêu nhân. Có nghĩa là nó có nhiều thứ mà lớp siêu nhân chưa có.

Trước mắt là chúng ta cứ viết lại một lớp siêu nhân gao có đầy đủ những thứ của lớp siêu nhân có cái đã. Nhưng viết thế nào? Dễ mà, copy paste là được. Như vậy thì chẳng giống lập trình tí nào, vậy nên ở lập trình hướng đối tượng không riêng gì Python, nó cho phép bạn gọi là kế thừa, lấy những gì mà lớp cũ có. Vậy ta muốn tạo lớp siêu nhân gao kế thừa từ lớp siêu nhân thì như thế nào?

VD:
class SieuNhan:
    pass
class SieuNhanGao(SieuNhan):
    pass
gao_do = SieuNhanGao()
print(gao_do)

- Khống muốn kế thừa lại thì đơn giản là viết cái thuộc tính đó là được.
- Thằng cha có hàm constructor thì đồng nghĩa khi thằng con kế thừa thằng cha thì cũng sẽ kế thừa luôn cái constructor đó.



Trong Python, các "hàm special" (còn được gọi là "magic methods" hoặc "dunder methods" với "dunder" là viết tắt của "double underscore") là những phương thức đặc biệt có tên bắt đầu và kết thúc bằng hai dấu gạch dưới (`__`). Các hàm special này giúp bạn tùy chỉnh hành vi của các đối tượng của lớp khi gặp các tình huống cụ thể. Dưới đây là một số hàm special quan trọng trong Python:

1. `__init__(self, ...)`: Được gọi khi một đối tượng mới của lớp được tạo ra. Đây là hàm khởi tạo (constructor).

2. `__str__(self)`: Được gọi bởi hàm `str(object)` và hàm `print()`, để trả về biểu diễn dạng chuỗi của đối tượng.

3. `__repr__(self)`: Được gọi bởi hàm `repr(object)`, để trả về biểu diễn chuỗi của đối tượng dùng cho mục đích debug.

4. `__len__(self)`: Được gọi bởi hàm `len(object)`, để trả về kích thước của đối tượng (số lượng phần tử, ký tự, ...).

5. `__getitem__(self, key)`: Được gọi khi bạn truy cập vào một phần tử trong đối tượng bằng cú pháp `object[key]`.

6. `__setitem__(self, key, value)`: Được gọi khi bạn gán giá trị cho một phần tử trong đối tượng bằng cú pháp `object[key] = value`.

7. `__delitem__(self, key)`: Được gọi khi bạn xóa một phần tử khỏi đối tượng bằng cú pháp `del object[key]`.

8. `__eq__(self, other)`: Được gọi khi sử dụng toán tử so sánh `==`, để so sánh hai đối tượng có bằng nhau hay không.

9. `__lt__(self, other)`, `__gt__(self, other)`, `__le__(self, other)`, `__ge__(self, other)`: Các hàm này được gọi khi sử dụng các toán tử so sánh `<`, `>`, `<=`, `>=`.

10. `__add__(self, other)`: Được gọi khi sử dụng toán tử `+`, để thực hiện phép cộng giữa hai đối tượng.

11. `__sub__(self, other)`, `__mul__(self, other)`, `__truediv__(self, other)`: Các hàm này tương tự như `__add__`, nhưng cho các phép trừ, nhân và chia.

12. `__call__(self, ...)`: Cho phép bạn gọi một đối tượng như một hàm bằng cú pháp `object()`.

Đây chỉ là một số ví dụ về các hàm special trong Python. Có nhiều hàm special khác mà bạn có thể tìm hiểu để tùy chỉnh hành vi của lớp theo ý muốn.


Ví dụ:
Dưới đây là một số ví dụ cụ thể về việc sử dụng các hàm special trong Python:

1. `__init__` và `__str__`:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, {self.age} years old"

person = Person("Alice", 30)
print(person)  # Kết quả: Alice, 30 years old
```

2. `__eq__`:

```python
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
```

3. `__getitem__` và `__setitem__`:

```python
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
print(my_list[0])  # Kết quả: 10
print(my_list[1])  # Kết quả: 20
```

4. `__len__`:

```python
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
```

Nhớ rằng các hàm special có thể được tùy chỉnh theo nhu cầu của bạn để tạo ra các lớp và đối tượng hoạt động theo cách mà bạn mong muốn.
