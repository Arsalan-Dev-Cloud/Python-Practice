
# Day 19 — Object Registration and Managing Objects Using a Class-Level List

## 1. What Is Object Registration?

**Object registration** is a technique in which objects register themselves in a shared collection when they are created.

For example, imagine that we create four laptop objects:

- Asus Laptop
- Acer Gaming Laptop
- Dell Office Laptop
- MSI Gaming Laptop

Instead of manually putting every object into a list, we can design our classes so that each new object automatically registers itself.

This technique is useful when building systems that need to track created objects, such as device management systems, product catalogs, and application registries.

---

## 2. Understanding Instance Attributes and Class Attributes

Before learning object registration, we need to understand the difference between instance attributes and class attributes.

### Instance Attributes

Instance attributes belong to a particular object.

For example:

```python
class Laptop:

    def __init__(self, brand):
        self.brand = brand


laptop1 = Laptop("Asus")
laptop2 = Laptop("Dell")

print(laptop1.brand)
print(laptop2.brand)
```

### Output

```text
Asus
Dell
```

Each object stores its own `brand`.

- `laptop1.brand` is `"Asus"`.
- `laptop2.brand` is `"Dell"`.

Changing the brand of one object does not automatically change the brand of the other.

### Class Attributes

A class attribute belongs to the class and is shared through the class unless an instance shadows it with an attribute of the same name.

```python
class Laptop:

    category = "Computer"

    def __init__(self, brand):
        self.brand = brand


laptop1 = Laptop("Asus")
laptop2 = Laptop("Dell")

print(laptop1.category)
print(laptop2.category)
print(Laptop.category)
```

### Output

```text
Computer
Computer
Computer
```

The `category` attribute is defined at the class level, so both objects can access it.

**Important:** A shared mutable class attribute, such as a list, is shared between instances. This behavior is useful for registration, but it should be used intentionally.

---

## 3. Creating a Class-Level List

We can create a list inside a class to store references to objects.

```python
class Laptop:

    all_obj = []


laptop1 = Laptop()
laptop2 = Laptop()

Laptop.all_obj.append(laptop1)
Laptop.all_obj.append(laptop2)

print(Laptop.all_obj)
```

The list `all_obj` belongs to the `Laptop` class.

However, in this example, we still manually append the objects to the list.

Our goal is to automate this process.

---

## 4. Automatically Registering Objects Using `__init__()`

The `__init__()` method runs when an object is initialized.

We can use it to register each new object automatically.

```python
class Laptop:

    all_obj = []

    def __init__(self, brand):
        self.brand = brand
        Laptop.all_obj.append(self)


laptop1 = Laptop("Asus")
laptop2 = Laptop("Dell")
laptop3 = Laptop("HP")

for laptop in Laptop.all_obj:
    print(laptop.brand)
```

### Output

```text
Asus
Dell
HP
```

### Explanation

1. `all_obj = []` creates a class-level list.
2. `self.brand = brand` stores the brand on the current object.
3. `Laptop.all_obj.append(self)` adds the current object to the shared list.
4. Whenever `Laptop(...)` creates and initializes an object, that object registers itself.
5. The loop accesses every registered object.

### What Does `self` Mean Here?

Inside `__init__()`, `self` refers to the particular object currently being initialized.

For example:

```python
laptop1 = Laptop("Asus")
```

During initialization, `self` refers to the new object assigned to `laptop1`.

Therefore:

```python
Laptop.all_obj.append(self)
```

stores a reference to that object in the list.

**Important:** The list stores object references, not just the brand strings.

---

## 5. Why Use `Laptop.all_obj` Instead of `self.all_obj`?

Consider these two expressions:

```python
Laptop.all_obj.append(self)
```

and:

```python
self.all_obj.append(self)
```

When `all_obj` is inherited from `Laptop` and no instance or subclass shadows it, both expressions can access the same inherited list.

However, `Laptop.all_obj.append(self)` explicitly identifies the list belonging to the `Laptop` class. This makes the intention clear in our example.

Using `self.all_obj` can become confusing if a subclass defines its own `all_obj` attribute, because the expression may then access a different list.

For our shared registry, we will use:

```python
Laptop.all_obj.append(self)
```

---

## 6. Registering Child-Class Objects Automatically

Now we can combine inheritance with automatic object registration.

```python
class Laptop:

    all_obj = []

    def __init__(self, brand):
        self.brand = brand
        Laptop.all_obj.append(self)


class GamingLaptop(Laptop):

    def __init__(self, brand, gpu):
        super().__init__(brand)
        self.gpu = gpu


class OfficeLaptop(Laptop):

    def __init__(self, brand, ram):
        super().__init__(brand)
        self.ram = ram


laptop1 = Laptop("Asus")
laptop2 = GamingLaptop("Acer", "RTX 5050")
laptop3 = OfficeLaptop("Dell", "16GB")
laptop4 = GamingLaptop("MSI", "RTX 5070")

print("Total registered objects:", len(Laptop.all_obj))
```

### Output

```text
Total registered objects: 4
```

### Explanation

Every object is registered automatically, including objects created from child classes.

The key line is:

```python
super().__init__(brand)
```

When a `GamingLaptop` object is initialized, its constructor calls the parent constructor. The parent constructor then registers the current object.

The same happens with `OfficeLaptop`.

Therefore, we do not need to write this repeatedly:

```python
Laptop.all_obj.append(laptop1)
Laptop.all_obj.append(laptop2)
Laptop.all_obj.append(laptop3)
Laptop.all_obj.append(laptop4)
```

The objects register themselves during initialization.

**Important:** A child class that overrides `__init__()` must call the parent constructor if it relies on the parent constructor to initialize shared attributes or perform registration.

---

## 7. Understanding `super().__init__(brand)`

Let's examine the constructor flow.

```python
class Laptop:

    all_obj = []

    def __init__(self, brand):
        self.brand = brand
        Laptop.all_obj.append(self)


class GamingLaptop(Laptop):

    def __init__(self, brand, gpu):
        super().__init__(brand)
        self.gpu = gpu


laptop = GamingLaptop("Acer", "RTX 5050")
```

When Python executes the last line:

1. Python creates a new `GamingLaptop` object.
2. The `GamingLaptop` constructor receives `"Acer"` and `"RTX 5050"`.
3. `super().__init__(brand)` calls the parent constructor.
4. The parent stores `"Acer"` in `self.brand`.
5. The parent adds the current object to `Laptop.all_obj`.
6. Control returns to the child constructor.
7. The child stores `"RTX 5050"` in `self.gpu`.

The object is registered by the parent constructor even though the object itself is a `GamingLaptop`.

---

## 8. Method Overriding in the Registered Objects

Different laptop types may need to display different information.

We can use method overriding to customize their details.

```python
class Laptop:

    all_obj = []

    def __init__(self, brand):
        self.brand = brand
        Laptop.all_obj.append(self)

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


laptop1 = Laptop("Asus")
laptop2 = GamingLaptop("Acer", "RTX 5050")
laptop3 = OfficeLaptop("Dell", "16GB")
laptop4 = GamingLaptop("MSI", "RTX 5070")

for item in Laptop.all_obj:
    item.show_details()
    print()
```

### Output

```text
Brand: Asus

Brand: Acer
GPU: RTX 5050

Brand: Dell
RAM: 16GB

Brand: MSI
GPU: RTX 5070
```

### Explanation

- `Laptop` defines the common `show_details()` method.
- `GamingLaptop` overrides it to display GPU information.
- `OfficeLaptop` overrides it to display RAM information.
- `super().show_details()` reuses the parent's implementation.
- `Laptop.all_obj` stores all four objects.
- The loop calls `show_details()` on every registered object.

Python selects the appropriate method for each object's class.

This combines **inheritance, constructors, object registration, method overriding, and polymorphism**.

---

## 9. Understanding the Registration List Step by Step

Consider:

```python
class Laptop:

    all_obj = []

    def __init__(self, brand):
        self.brand = brand
        Laptop.all_obj.append(self)


laptop1 = Laptop("Asus")
laptop2 = Laptop("Dell")
laptop3 = Laptop("HP")
```

After these statements execute, the list conceptually contains:

```text
Laptop.all_obj
    |
    |----> laptop1 object: brand = "Asus"
    |
    |----> laptop2 object: brand = "Dell"
    |
    |----> laptop3 object: brand = "HP"
```

The list contains references to the objects.

We can verify the number of registered objects:

```python
print(len(Laptop.all_obj))
```

Output:

```text
3
```

We can access each registered object:

```python
for item in Laptop.all_obj:
    print(item.brand)
```

Output:

```text
Asus
Dell
HP
```

We can also access a particular object by its list index:

```python
print(Laptop.all_obj[0].brand)
print(Laptop.all_obj[1].brand)
print(Laptop.all_obj[2].brand)
```

Output:

```text
Asus
Dell
HP
```

List indexes begin at `0`, so the first registered object is at index `0`.

---

## 10. Automatically Registering Objects Without `__init__()`

It is also possible to register objects without putting the registration code inside `__init__()`, but the registration must happen somewhere else.

For example, we can explicitly register objects using a class method.

```python
class Laptop:

    all_obj = []

    def __init__(self, brand):
        self.brand = brand

    @classmethod
    def register(cls, obj):
        cls.all_obj.append(obj)


laptop1 = Laptop("Asus")
laptop2 = Laptop("Dell")

Laptop.register(laptop1)
Laptop.register(laptop2)

for laptop in Laptop.all_obj:
    print(laptop.brand)
```

### Output

```text
Asus
Dell
```

In this approach, `__init__()` does not register objects. We must call `Laptop.register(...)` separately.

This is useful when registration should be an explicit decision rather than an automatic action.

**Important:** If we do not use `__init__()` or another automatic creation mechanism, Python will not automatically know which objects we want to register. We must register them through some other method or mechanism.

For our Day 19 laptop-management example, registering objects from the parent constructor is the simpler approach.

---

## 11. Important Considerations

### 11.1 Duplicate Registration

If we register the same object more than once, it can appear multiple times in the list.

```python
class Laptop:

    all_obj = []

    def __init__(self, brand):
        self.brand = brand
        Laptop.all_obj.append(self)


laptop1 = Laptop("Asus")

Laptop.all_obj.append(laptop1)

print(len(Laptop.all_obj))
```

Output:

```text
2
```

The same object appears twice because it was registered once during initialization and once manually.

Avoid manually appending an object if the constructor already registers it.

### 11.2 The List Keeps References to Objects

A class-level list can keep objects reachable for as long as the list holds references to them.

If an application creates many objects over time, the registry may grow continuously. In a larger application, you may need a way to remove objects that are no longer needed.

### 11.3 Class-Level Lists Are Shared State

The `all_obj` list is shared state. Every registered object is visible through the same class-level list.

This is convenient for a small learning project, but larger systems may use a dedicated manager, database, or other registry design.

### 11.4 Registration Does Not Automatically Persist Data

The list exists in the running Python process. It does not automatically save objects to a file or database.

When the program exits, the in-memory list disappears unless the data is saved separately.

---

## 12. Day 19 Complete Example

This is the complete example combining the concepts from Day 19.

```python
class Laptop:

    all_obj = []

    def __init__(self, brand):
        self.brand = brand
        Laptop.all_obj.append(self)

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


laptop1 = Laptop("Asus")
laptop2 = GamingLaptop("Acer", "RTX 5050")
laptop3 = OfficeLaptop("Dell", "16GB")
laptop4 = GamingLaptop("MSI", "RTX 5070")

print("Total registered laptops:", len(Laptop.all_obj))
print()

for item in Laptop.all_obj:
    item.show_details()
    print()
```

### Output

```text
Total registered laptops: 4

Brand: Asus

Brand: Acer
GPU: RTX 5050

Brand: Dell
RAM: 16GB

Brand: MSI
GPU: RTX 5070
```

### Concepts Used

1. Class attributes
2. Instance attributes
3. The `__init__()` constructor
4. `self`
5. Inheritance
6. `super().__init__()`
7. Automatic object registration
8. Class-level lists
9. Method overriding
10. Polymorphism
11. Loops and object references

---

## 13. Day 19 Summary

| Concept | Meaning |
|---|---|
| Object registration | Adding an object to a collection for later access |
| Class attribute | An attribute associated with the class |
| Instance attribute | An attribute associated with an individual object |
| Class-level list | A list shared through the class |
| `self` | Refers to the current object |
| `__init__()` | Initializes an object and can perform registration |
| `append()` | Adds an item or object reference to a list |
| `super().__init__()` | Calls the parent constructor through Python's method resolution order |
| Method overriding | Allows a child class to customize a method |
| Polymorphism | Allows the same method call to behave differently for different objects |
| `len()` | Returns the number of items in a list |
| `@classmethod` | Defines a method that receives the class as its first argument |

**Day 19 completed:** Object registration, class-level lists, constructors, inheritance, method overriding, and managing different objects through a common collection.

**Next topic — Day 20:** Encapsulation and abstraction in Python.
