
# Day 17 — Inheritance in Python

## 1. What Is Inheritance?

**Inheritance** is an Object-Oriented Programming (OOP) concept that allows one class to acquire the attributes and methods of another class.

It helps us reuse existing code instead of writing the same code repeatedly.

- **Parent class:** The class whose attributes and methods are inherited.
- **Child class:** The class that inherits from the parent class.

### Example

```python
class Laptop:

    def show_brand(self):
        print("Brand: Asus")


class GamingLaptop(Laptop):

    def show_gpu(self):
        print("GPU: RTX 5050")


laptop1 = GamingLaptop()

laptop1.show_brand()
laptop1.show_gpu()
```

### Output

```text
Brand: Asus
GPU: RTX 5050
```

### Explanation

1. `Laptop` is the parent class.
2. `GamingLaptop` is the child class.
3. `class GamingLaptop(Laptop):` establishes inheritance.
4. `GamingLaptop` inherits the `show_brand()` method from `Laptop`.
5. The child class also defines its own method, `show_gpu()`.
6. An object of `GamingLaptop` can call both methods.

---

## 2. Why Do We Use Inheritance?

Inheritance is useful because it provides:

1. **Code reusability:** Write common methods once and reuse them.
2. **Less duplication:** Avoid repeating the same code in multiple classes.
3. **Easy maintenance:** Update shared behavior in the parent class.
4. **Extensibility:** Add specialized functionality in child classes.
5. **Better organization:** Represent relationships between related objects.

### Example Without Inheritance

```python
class GamingLaptop:

    def show_brand(self):
        print("Brand: Asus")

    def show_gpu(self):
        print("GPU: RTX 5050")


class OfficeLaptop:

    def show_brand(self):
        print("Brand: Dell")

    def show_ram(self):
        print("RAM: 16GB")
```

Both classes contain a `show_brand()` method.

If many classes need the same common behavior, inheritance can reduce duplication.

### Example With Inheritance

```python
class Laptop:

    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print("Brand:", self.brand)


class GamingLaptop(Laptop):

    def show_gpu(self):
        print("GPU: RTX 5050")


class OfficeLaptop(Laptop):

    def show_ram(self):
        print("RAM: 16GB")


gaming = GamingLaptop("Asus")
office = OfficeLaptop("Dell")

gaming.show_brand()
gaming.show_gpu()

office.show_brand()
office.show_ram()
```

### Output

```text
Brand: Asus
GPU: RTX 5050
Brand: Dell
RAM: 16GB
```

The common brand information and method are defined in the parent class, `Laptop`.

---

## 3. The Five Types of Inheritance

Python supports several inheritance structures. The five commonly studied types are:

1. Single inheritance
2. Multiple inheritance
3. Multilevel inheritance
4. Hierarchical inheritance
5. Hybrid inheritance

### 3.1 Single Inheritance

A single child class inherits from one parent class.

```python
class Laptop:

    def show_brand(self):
        print("Brand: Asus")


class GamingLaptop(Laptop):

    def show_gpu(self):
        print("GPU: RTX 5050")


laptop = GamingLaptop()

laptop.show_brand()
laptop.show_gpu()
```

**Structure:**

```text
Laptop
   |
   v
GamingLaptop
```

**Output:**

```text
Brand: Asus
GPU: RTX 5050
```

### 3.2 Multiple Inheritance

A child class inherits from two or more parent classes.

```python
class Camera:

    def take_photo(self):
        print("Photo captured")


class Phone:

    def make_call(self):
        print("Calling...")


class Smartphone(Camera, Phone):

    def show_device(self):
        print("This is a smartphone")


mobile = Smartphone()

mobile.take_photo()
mobile.make_call()
mobile.show_device()
```

**Structure:**

```text
Camera       Phone
    \         /
     \       /
      Smartphone
```

**Output:**

```text
Photo captured
Calling...
This is a smartphone
```

`Smartphone` inherits methods from both `Camera` and `Phone`.

### 3.3 Multilevel Inheritance

A class inherits from a child class, forming a chain of inheritance.

```python
class Laptop:

    def show_brand(self):
        print("Brand: Asus")


class GamingLaptop(Laptop):

    def show_gpu(self):
        print("GPU: RTX 5050")


class AdvancedGamingLaptop(GamingLaptop):

    def show_ram(self):
        print("RAM: 32GB")


laptop = AdvancedGamingLaptop()

laptop.show_brand()
laptop.show_gpu()
laptop.show_ram()
```

**Structure:**

```text
Laptop
   |
   v
GamingLaptop
   |
   v
AdvancedGamingLaptop
```

**Output:**

```text
Brand: Asus
GPU: RTX 5050
RAM: 32GB
```

`AdvancedGamingLaptop` can access methods from both `GamingLaptop` and `Laptop`.

### 3.4 Hierarchical Inheritance

Multiple child classes inherit from the same parent class.

```python
class Laptop:

    def show_brand(self):
        print("Laptop brand displayed")


class GamingLaptop(Laptop):

    def show_gpu(self):
        print("GPU: RTX 5050")


class OfficeLaptop(Laptop):

    def show_ram(self):
        print("RAM: 16GB")


gaming = GamingLaptop()
office = OfficeLaptop()

gaming.show_brand()
gaming.show_gpu()

office.show_brand()
office.show_ram()
```

**Structure:**

```text
       Laptop
       /    \
      v      v
 Gaming    Office
 Laptop    Laptop
```

**Output:**

```text
Laptop brand displayed
GPU: RTX 5050
Laptop brand displayed
RAM: 16GB
```

Both child classes inherit from the same parent class.

### 3.5 Hybrid Inheritance

Hybrid inheritance combines two or more inheritance types.

```python
class Device:

    def show_device(self):
        print("Electronic device")


class Computer(Device):

    def show_computer(self):
        print("Computer")


class Camera:

    def show_camera(self):
        print("Camera")


class SmartDevice(Computer, Camera):

    def show_smart_device(self):
        print("Smart device")


device = SmartDevice()

device.show_device()
device.show_computer()
device.show_camera()
device.show_smart_device()
```

**Structure:**

```text
       Device       Camera
          |            |
          v            |
       Computer        |
          \            /
           \          /
            SmartDevice
```

**Output:**

```text
Electronic device
Computer
Camera
Smart device
```

The example combines multilevel inheritance (`Device` → `Computer`) with multiple inheritance (`SmartDevice` inherits from `Computer` and `Camera`).

---

## 4. The `__init__()` Constructor in Inheritance

The `__init__()` method is a special method that initializes an object's attributes when the object is created.

### Example

```python
class Laptop:

    def __init__(self, brand):
        self.brand = brand


class GamingLaptop(Laptop):

    def __init__(self, brand, gpu):
        self.brand = brand
        self.gpu = gpu

    def show_details(self):
        print("Brand:", self.brand)
        print("GPU:", self.gpu)


laptop = GamingLaptop("Asus", "RTX 5050")

laptop.show_details()
```

### Output

```text
Brand: Asus
GPU: RTX 5050
```

In this example, the child class initializes both attributes itself. However, this duplicates the parent's initialization logic.

We can use `super()` to reuse the parent constructor.

---

## 5. The `super()` Function

`super()` provides access to methods from a parent class according to Python's method resolution order.

It is commonly used in inheritance to call the parent class's constructor or another parent method.

### Example Using `super().__init__()`

```python
class Laptop:

    def __init__(self, brand):
        self.brand = brand


class GamingLaptop(Laptop):

    def __init__(self, brand, gpu):
        super().__init__(brand)
        self.gpu = gpu

    def show_details(self):
        print("Brand:", self.brand)
        print("GPU:", self.gpu)


laptop = GamingLaptop("Asus", "RTX 5050")

laptop.show_details()
```

### Output

```text
Brand: Asus
GPU: RTX 5050
```

### Explanation

- `super().__init__(brand)` calls the parent class's `__init__()` method.
- The parent constructor assigns `brand` to `self.brand`.
- The child constructor assigns `gpu` to `self.gpu`.
- The child class reuses the parent's initialization logic.

**Important:** When a child class defines its own `__init__()`, Python does not automatically call the parent's `__init__()`. You must explicitly call it when the parent's initialization is needed, commonly using `super().__init__(...)`.

---

## 6. Understanding `self`

`self` refers to the current object.

It allows instance methods to access or modify the attributes belonging to that particular object.

### Example

```python
class Laptop:

    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print("Brand:", self.brand)


laptop1 = Laptop("Asus")
laptop2 = Laptop("Dell")

laptop1.show_brand()
laptop2.show_brand()
```

### Output

```text
Brand: Asus
Brand: Dell
```

Here:

- `self.brand = brand` stores the brand on the current object.
- `laptop1` stores `"Asus"`.
- `laptop2` stores `"Dell"`.

Each object has its own instance attributes.

---

## 7. Method Overriding

**Method overriding** occurs when a child class defines a method with the same name as a method inherited from its parent class.

When the method is called on a child object, Python generally uses the child's implementation.

### Example

```python
class Laptop:

    def show_type(self):
        print("General laptop")


class GamingLaptop(Laptop):

    def show_type(self):
        print("Gaming laptop")


laptop1 = Laptop()
laptop2 = GamingLaptop()

laptop1.show_type()
laptop2.show_type()
```

### Output

```text
General laptop
Gaming laptop
```

Although both classes have a method called `show_type()`, the implementation used depends on the object's class.

### Overriding With `super()`

Sometimes, we want to extend the parent's behavior rather than replace it completely.

```python
class Laptop:

    def show_details(self):
        print("Laptop details")


class GamingLaptop(Laptop):

    def show_details(self):
        super().show_details()
        print("GPU: RTX 5050")


laptop = GamingLaptop()

laptop.show_details()
```

### Output

```text
Laptop details
GPU: RTX 5050
```

`super().show_details()` runs the parent's method first. The child method then adds its own behavior.

---

## 8. Combining Inheritance, Constructors, and Overriding

The following example combines the main concepts learned in Day 17.

```python
class Laptop:

    def __init__(self, brand):
        self.brand = brand

    def show_details(self):
        print("Brand:", self.brand)


class GamingLaptop(Laptop):

    def __init__(self, brand, gpu):
        super().__init__(brand)
        self.gpu = gpu

    def show_details(self):
        super().show_details()
        print("GPU:", self.gpu)


class OfficeLaptop(Laptop):

    def __init__(self, brand, ram):
        super().__init__(brand)
        self.ram = ram

    def show_details(self):
        super().show_details()
        print("RAM:", self.ram)


laptop1 = GamingLaptop("Asus", "RTX 5050")
laptop2 = OfficeLaptop("Dell", "16GB")

laptop1.show_details()

print()

laptop2.show_details()
```

### Output

```text
Brand: Asus
GPU: RTX 5050

Brand: Dell
RAM: 16GB
```

### What This Example Demonstrates

1. `Laptop` is the parent class.
2. `GamingLaptop` and `OfficeLaptop` are child classes.
3. Both child classes inherit from `Laptop`.
4. `super().__init__(brand)` reuses the parent's constructor.
5. Each child class initializes its own additional attribute.
6. Both child classes override `show_details()`.
7. `super().show_details()` reuses the parent's method before adding child-specific information.

---

## 9. Important Points to Remember

- Inheritance allows one class to reuse another class's attributes and methods.
- The parent class is also called the base class.
- The child class is also called the derived class.
- Python supports single, multiple, multilevel, hierarchical, and hybrid inheritance.
- `__init__()` initializes an object.
- `self` refers to the current object.
- `super()` accesses methods through the parent-class method resolution order.
- A child constructor does not automatically execute the parent's constructor.
- Method overriding allows a child class to customize inherited behavior.
- `super().method_name()` can call the parent's implementation.
- Inheritance should represent a meaningful relationship between classes, not merely be used to avoid every instance of code duplication.

---

## 10. Day 17 Summary

| Concept | Meaning |
|---|---|
| Inheritance | Reusing behavior from another class |
| Parent class | Class being inherited from |
| Child class | Class that inherits from another class |
| `__init__()` | Initializes object attributes |
| `self` | Refers to the current object |
| `super()` | Accesses methods through the parent-class method resolution order |
| Method overriding | Redefining an inherited method in a child class |
| Single inheritance | One child inherits from one parent |
| Multiple inheritance | One child inherits from multiple parents |
| Multilevel inheritance | Inheritance forms a chain |
| Hierarchical inheritance | Multiple children share one parent |
| Hybrid inheritance | A combination of inheritance types |

**Day 17 completed:** Inheritance, its five common types, constructors, `self`, `super()`, and method overriding.

**Next topic — Day 18:** Polymorphism in Python.
