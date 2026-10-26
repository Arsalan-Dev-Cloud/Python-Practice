
# Day 18 — Polymorphism in Python

## 1. What Is Polymorphism?

**Polymorphism** is an Object-Oriented Programming (OOP) concept that means **"many forms."**

In Python, polymorphism allows the same method name, function, or operation to behave differently depending on the object or data it works with.

For example, different laptop types can have a method called `show_details()`, but each type can display different information.

### Example

```python
class Laptop:

    def show_type(self):
        print("General laptop")


class GamingLaptop:

    def show_type(self):
        print("Gaming laptop")


class OfficeLaptop:

    def show_type(self):
        print("Office laptop")


laptop1 = Laptop()
laptop2 = GamingLaptop()
laptop3 = OfficeLaptop()

laptop1.show_type()
laptop2.show_type()
laptop3.show_type()
```

### Output

```text
General laptop
Gaming laptop
Office laptop
```

### Explanation

1. All three classes have a method named `show_type()`.
2. Each class implements the method differently.
3. Calling `show_type()` produces output based on the object's class.

The method name is the same, but its behavior differs.

---

## 2. Method Overriding and Polymorphism

Method overriding occurs when a child class provides its own implementation of a method inherited from a parent class.

It is one common way to achieve polymorphism.

### Example

```python
class Laptop:

    def show_details(self):
        print("This is a laptop")


class GamingLaptop(Laptop):

    def show_details(self):
        print("This is a gaming laptop")


class OfficeLaptop(Laptop):

    def show_details(self):
        print("This is an office laptop")


laptop1 = Laptop()
laptop2 = GamingLaptop()
laptop3 = OfficeLaptop()

laptop1.show_details()
laptop2.show_details()
laptop3.show_details()
```

### Output

```text
This is a laptop
This is a gaming laptop
This is an office laptop
```

### Explanation

- `Laptop` defines the original `show_details()` method.
- `GamingLaptop` overrides it.
- `OfficeLaptop` also overrides it.
- Python calls the appropriate implementation for each object.

**Important:** Method overriding requires an inheritance relationship between the parent and child classes. Polymorphism itself is broader and does not always require inheritance.

---

## 3. Polymorphism Using a Common List

One of the most useful features of polymorphism is that we can store objects of different classes in the same list and call the same method on each object.

### Example

```python
class Laptop:

    def show_details(self):
        print("General laptop")


class GamingLaptop(Laptop):

    def show_details(self):
        print("Gaming laptop")


class OfficeLaptop(Laptop):

    def show_details(self):
        print("Office laptop")


laptop1 = Laptop()
laptop2 = GamingLaptop()
laptop3 = OfficeLaptop()

all_laptops = [laptop1, laptop2, laptop3]

for laptop in all_laptops:
    laptop.show_details()
```

### Output

```text
General laptop
Gaming laptop
Office laptop
```

### Explanation

The list contains three different objects:

- `laptop1` is a `Laptop`.
- `laptop2` is a `GamingLaptop`.
- `laptop3` is an `OfficeLaptop`.

The loop calls `show_details()` on every object. Python chooses the correct method implementation for each object.

This makes the code easier to extend. If we add another compatible laptop class, we can add its object to the list without changing the loop.

---

## 4. Polymorphism With `super()`

Sometimes a child class needs to preserve the parent's behavior and add its own information.

We can use `super()` to call the parent's method.

### Example

```python
class Laptop:

    def show_details(self):
        print("Device: Laptop")


class GamingLaptop(Laptop):

    def show_details(self):
        super().show_details()
        print("GPU: RTX 5050")


class OfficeLaptop(Laptop):

    def show_details(self):
        super().show_details()
        print("RAM: 16GB")


laptop1 = GamingLaptop()
laptop2 = OfficeLaptop()

laptop1.show_details()

print()

laptop2.show_details()
```

### Output

```text
Device: Laptop
GPU: RTX 5050

Device: Laptop
RAM: 16GB
```

### Explanation

`super().show_details()` calls the inherited implementation before the child adds its own details.

- `GamingLaptop` displays the common laptop information and GPU.
- `OfficeLaptop` displays the common laptop information and RAM.

The same method name produces different extended behavior.

---

## 5. Duck Typing

**Duck typing** is a Python approach in which an object's suitability depends on the operations or methods it supports, rather than strictly on its class.

The idea is often summarized as:

"If an object behaves like the required type, we can use it for that purpose."

### Example

```python
class Laptop:

    def start(self):
        print("Laptop is starting")


class Smartphone:

    def start(self):
        print("Smartphone is starting")


class SmartTV:

    def start(self):
        print("Smart TV is starting")


def start_device(device):
    device.start()


laptop = Laptop()
phone = Smartphone()
tv = SmartTV()

start_device(laptop)
start_device(phone)
start_device(tv)
```

### Output

```text
Laptop is starting
Smartphone is starting
Smart TV is starting
```

### Explanation

The function `start_device()` does not require every object to inherit from the same parent class.

It only expects the supplied object to provide a callable `start()` method.

Each class implements that method differently, so the function works with all three objects.

**Important:** If an object does not have a suitable `start()` method, calling `device.start()` will normally raise an `AttributeError`.

Duck typing is a common and important form of polymorphic behavior in Python.

---

## 6. Built-in Polymorphism

Python's built-in functions and operators can also behave differently depending on the data they receive.

### Example 1: The `+` Operator

```python
print(10 + 20)

print("Hello " + "Python")

print([10, 20] + [30, 40])
```

### Output

```text
30
Hello Python
[10, 20, 30, 40]
```

### Explanation

The same operator, `+`, performs different operations:

- With numbers, it performs addition.
- With strings, it concatenates text.
- With lists, it combines list contents into a new list.

This is another example of polymorphic behavior.

### Example 2: The `len()` Function

```python
print(len("Python"))

print(len([10, 20, 30]))

print(len({"brand": "Asus", "ram": "16GB"}))
```

### Output

```text
6
3
2
```

The same `len()` function works with different objects:

- A string returns its number of characters.
- A list returns its number of elements.
- A dictionary returns its number of key-value pairs.

The object determines the appropriate behavior.

---

## 7. Polymorphism With Different Method Parameters

Python functions can accept different types of objects. A method can also accept different types of arguments and use them appropriately.

For example:

```python
class Calculator:

    def add(self, a, b):
        return a + b


calculator = Calculator()

print(calculator.add(10, 20))
print(calculator.add("Hello ", "Python"))
print(calculator.add([10, 20], [30, 40]))
```

### Output

```text
30
Hello Python
[10, 20, 30, 40]
```

The `add()` method uses the `+` operator. Its result depends on the types of `a` and `b`.

This example demonstrates flexible behavior through the operation used inside the method.

**Note:** Python does not support traditional method overloading based only on different parameter lists in the same way as languages such as Java. Defining another method with the same name in the same class normally replaces the earlier definition. Python commonly uses default arguments, `*args`, or explicit type checks when one function needs to handle different argument patterns.

---

## 8. Using `isinstance()` With Polymorphism

The built-in `isinstance()` function checks whether an object is an instance of a class or one of its subclasses.

### Example

```python
class Laptop:
    pass


class GamingLaptop(Laptop):
    pass


laptop1 = Laptop()
laptop2 = GamingLaptop()

print(isinstance(laptop1, Laptop))
print(isinstance(laptop2, Laptop))
print(isinstance(laptop2, GamingLaptop))
```

### Output

```text
True
True
True
```

### Explanation

- `laptop1` is a `Laptop`.
- `laptop2` is a `GamingLaptop`.
- Because `GamingLaptop` inherits from `Laptop`, a `GamingLaptop` object is also considered an instance of `Laptop`.

We can use `isinstance()` when we genuinely need to check an object's type. However, when practical, code that relies on a common method or duck typing can be more flexible than repeatedly checking classes.

---

## 9. Polymorphism With Different Laptop Prices

This example combines objects, inheritance, method overriding, and polymorphism.

```python
class Laptop:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_details(self):
        print("Brand:", self.brand)
        print("Price:", self.price)


class GamingLaptop(Laptop):

    def __init__(self, brand, price, gpu):
        super().__init__(brand, price)
        self.gpu = gpu

    def show_details(self):
        super().show_details()
        print("GPU:", self.gpu)


class OfficeLaptop(Laptop):

    def __init__(self, brand, price, ram):
        super().__init__(brand, price)
        self.ram = ram

    def show_details(self):
        super().show_details()
        print("RAM:", self.ram)


laptop1 = GamingLaptop("Asus", 150000, "RTX 5050")
laptop2 = OfficeLaptop("Dell", 70000, "16GB")
laptop3 = Laptop("HP", 50000)

all_laptops = [laptop1, laptop2, laptop3]

for laptop in all_laptops:
    laptop.show_details()
    print()
```

### Output

```text
Brand: Asus
Price: 150000
GPU: RTX 5050

Brand: Dell
Price: 70000
RAM: 16GB

Brand: HP
Price: 50000
```

### Explanation

1. `Laptop` defines common attributes and a common method.
2. `GamingLaptop` adds a GPU attribute and overrides `show_details()`.
3. `OfficeLaptop` adds a RAM attribute and overrides `show_details()`.
4. `super().__init__(...)` reuses the parent constructor.
5. The list contains objects from three different classes.
6. The loop calls the same method on every object.
7. Python executes the appropriate method for each object.

This is useful when building applications that manage different kinds of devices, products, employees, or other related objects.

---

## 10. A Common Mistake: Forgetting to Call a Method

Consider this example:

```python
class Laptop:

    def show_details(self):
        print("Laptop details")


laptop = Laptop()

print(laptop.show_details())
```

### Output

```text
Laptop details
None
```

### Why Does `None` Appear?

The method prints `"Laptop details"` but does not return a value.

In Python, a function or method that finishes without an explicit `return` statement returns `None`.

To return a value instead, we could write:

```python
class Laptop:

    def show_details(self):
        return "Laptop details"


laptop = Laptop()

print(laptop.show_details())
```

### Output

```text
Laptop details
```

Remember:

- `print()` displays information.
- `return` sends a value back to the caller.
- A method can use either or both, depending on its purpose.

---

## 11. Important Points to Remember

- Polymorphism means "many forms."
- The same method name can produce different behavior for different objects.
- Method overriding is a common way to achieve polymorphism.
- A common list can contain objects from different classes.
- A loop can call the same method on each object without needing to know every class in advance.
- `super()` allows a child method to reuse parent behavior.
- Duck typing focuses on the operations an object supports.
- Built-in operators and functions can work differently with different data types.
- `isinstance()` checks whether an object belongs to a class or its subclasses.
- Python does not support traditional method overloading based only on parameter signatures.
- A function or method without an explicit return value returns `None`.
- Good polymorphic design makes it easier to add new classes without rewriting existing code.

---

## 12. Day 18 Summary

| Concept | Meaning |
|---|---|
| Polymorphism | The same interface can have different behaviors |
| Method overriding | A child class provides its own implementation of an inherited method |
| Common list | Stores different objects and allows a common method to be called on each |
| `super()` | Calls methods through the parent-class method resolution order |
| Duck typing | Uses an object based on the operations it supports |
| Built-in polymorphism | Operators and functions behave appropriately for different types |
| `isinstance()` | Checks whether an object is an instance of a class or its subclass |
| `return` | Sends a value back to the caller |
| `print()` | Displays information |

**Day 18 completed:** Polymorphism, method overriding, duck typing, built-in polymorphism, common lists, and `isinstance()`.

**Next topic — Day 19:** Object registration and managing objects using a class-level list.
