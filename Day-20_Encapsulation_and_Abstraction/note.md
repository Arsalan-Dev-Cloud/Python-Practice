
# Day 20 — Encapsulation and Abstraction in Python

## 1. Introduction

In Object-Oriented Programming (OOP), **encapsulation** and **abstraction** help us organize code, control access to data, and simplify how we interact with objects.

Although these concepts are related, they solve different problems.

- **Encapsulation:** Groups data and methods together and provides ways to control how data is accessed or modified.
- **Abstraction:** Hides unnecessary implementation details and exposes the essential operations that an object supports.

For example, in a laptop-management application:

- Encapsulation helps control how a laptop's battery information is changed.
- Abstraction lets us use a method such as `start()` without needing to know every internal step required to start the laptop.

---

# Part 1 — Encapsulation

## 2. What Is Encapsulation?

**Encapsulation** is an OOP principle that combines an object's data and related methods into a class while providing controlled ways to interact with that data.

Consider a laptop with a battery percentage. We want to prevent invalid values such as `-20` or `150` from being assigned accidentally.

We can create methods that validate the value before updating it.

### Example

```python
class Laptop:

    def __init__(self, battery):
        self.battery = battery

    def show_battery(self):
        print("Battery:", self.battery, "%")


laptop = Laptop(80)

laptop.show_battery()
```

### Output

```text
Battery: 80 %
```

Here:

- `battery` stores the battery percentage.
- `show_battery()` displays that information.
- Both the data and its related behavior are organized in the `Laptop` class.

This is a simple example of grouping data and methods together. Stronger control over changes requires additional validation.

---

## 3. Public Attributes

A **public attribute** can be accessed directly from outside its class.

In Python, attributes without a leading underscore are generally treated as public.

### Example

```python
class Laptop:

    def __init__(self, battery):
        self.battery = battery


laptop = Laptop(80)

print(laptop.battery)

laptop.battery = 60

print(laptop.battery)
```

### Output

```text
80
60
```

### Explanation

- `self.battery = battery` creates a public instance attribute.
- `laptop.battery` reads its value.
- `laptop.battery = 60` changes its value directly.

Public attributes are simple to use, but they do not automatically validate assigned values.

For example:

```python
laptop.battery = 150
print(laptop.battery)
```

Output:

```text
150
```

Python accepts this assignment because no validation has been implemented.

If we want to enforce a range of `0` to `100`, we need a validation mechanism.

---

## 4. Protected-Style Attributes

In Python, an attribute beginning with a single underscore is conventionally treated as **non-public** or **protected-style**.

For example:

```python
class Laptop:

    def __init__(self, model):
        self._model = model

    def show_model(self):
        print("Model:", self._model)


laptop = Laptop("ROG Strix G16")

laptop.show_model()

print(laptop._model)
```

### Output

```text
Model: ROG Strix G16
ROG Strix G16
```

### Explanation

- `self._model` uses a single leading underscore.
- The underscore communicates that the attribute is intended for internal use or use by subclasses.
- Python does not prevent direct access to this attribute.

**Important:** A single underscore is a naming convention, not a strict access restriction. The attribute can still be accessed from outside the class.

---

## 5. Private-Style Attributes

In Python, an attribute beginning with two leading underscores and not ending with two underscores triggers **name mangling**.

Name mangling changes the internal attribute name to reduce accidental conflicts with subclasses and discourage direct access.

### Example

```python
class Laptop:

    def __init__(self, battery):
        self.__battery = battery

    def show_battery(self):
        print("Battery:", self.__battery, "%")


laptop = Laptop(80)

laptop.show_battery()
```

### Output

```text
Battery: 80 %
```

Here, `self.__battery` is a private-style attribute.

Trying to access it directly:

```python
print(laptop.__battery)
```

normally produces an `AttributeError` because the attribute is stored under a mangled name.

For a class named `Laptop`, Python mangles `__battery` to `_Laptop__battery`.

The mangled attribute can still be accessed:

```python
print(laptop._Laptop__battery)
```

Output:

```text
80
```

However, accessing it this way bypasses the intended interface and is generally discouraged.

**Important:** Python's double underscore does not create absolute privacy. It performs name mangling, which helps avoid accidental access and naming conflicts.

### Attribute Naming Summary

| Attribute | Example | Meaning |
|---|---|---|
| Public | `self.battery` | Intended for normal external access |
| Protected-style | `self._model` | Conventionally intended for internal or subclass use |
| Private-style | `self.__battery` | Name-mangled to reduce accidental access and conflicts |

---

## 6. Getters and Setters

A **getter** retrieves an attribute's value.

A **setter** updates an attribute's value, often after checking whether the new value is valid.

These methods can provide controlled access to private-style attributes.

### Example

```python
class Laptop:

    def __init__(self, battery):
        self.__battery = battery

    def get_battery(self):
        return self.__battery

    def set_battery(self, battery):

        if 0 <= battery <= 100:
            self.__battery = battery
        else:
            print("Invalid battery percentage")


laptop = Laptop(80)

print(laptop.get_battery())

laptop.set_battery(60)
print(laptop.get_battery())

laptop.set_battery(150)
print(laptop.get_battery())
```

### Output

```text
80
60
Invalid battery percentage
60
```

### Explanation

1. `self.__battery` stores the battery percentage.
2. `get_battery()` returns the current value.
3. `set_battery()` checks whether the new value is between `0` and `100`.
4. If valid, the setter updates the attribute.
5. If invalid, the setter displays an error message and keeps the existing value.

The invalid value `150` does not replace the previous value of `60`.

### Why Use Getters and Setters?

They allow us to:

- Validate new values.
- Reject invalid changes.
- Add logging or other logic when data changes.
- Keep the internal representation separate from the public interface.

---

## 7. Using `@property`

Python's `@property` decorator provides a convenient way to implement controlled attribute access.

It allows us to use attribute-style syntax while running a method behind the scenes.

### Example

```python
class Laptop:

    def __init__(self, battery):
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):

        if 0 <= value <= 100:
            self.__battery = value
        else:
            print("Invalid battery percentage")


laptop = Laptop(80)

print(laptop.battery)

laptop.battery = 60
print(laptop.battery)

laptop.battery = 150
print(laptop.battery)
```

### Output

```text
80
60
Invalid battery percentage
60
```

### Explanation

#### The Getter

```python
@property
def battery(self):
    return self.__battery
```

When we write:

```python
print(laptop.battery)
```

Python calls the getter and returns the stored value.

We do not write `laptop.battery()` because the property is accessed like an attribute.

#### The Setter

```python
@battery.setter
def battery(self, value):
```

When we write:

```python
laptop.battery = 60
```

Python calls the setter.

The setter validates the new value before changing the internal attribute.

### Important Details

- `@property` defines a getter.
- `@battery.setter` defines the corresponding setter.
- The setter method must use the same property name, `battery`.
- `self.__battery` is used for storage to avoid accidentally calling the property again.
- If we define a property without a setter, assigning to that property normally raises an `AttributeError`.

### Validating the Initial Value

In the previous example, the constructor directly assigns the initial value to `self.__battery`. That means the initial value is not validated.

To validate the initial value too, we can use the property setter in the constructor:

```python
class Laptop:

    def __init__(self, battery):
        self.battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):

        if isinstance(value, (int, float)) and not isinstance(value, bool) and 0 <= value <= 100:
            self.__battery = value
        else:
            raise ValueError("Battery must be a number between 0 and 100")


laptop = Laptop(80)

print(laptop.battery)

laptop.battery = 60
print(laptop.battery)
```

### Output

```text
80
60
```

This version validates the initial value and later assignments. Invalid values raise a `ValueError` instead of silently leaving the previous value unchanged.

The `isinstance()` checks also reject non-numeric values and Boolean values.

---

## 8. Encapsulation Example Using a Laptop Class

This example combines private-style storage, a property getter, and a validating setter.

```python
class Laptop:

    def __init__(self, brand, battery):
        self.brand = brand
        self.battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):

        if isinstance(value, (int, float)) and not isinstance(value, bool) and 0 <= value <= 100:
            self.__battery = value
        else:
            raise ValueError("Battery must be a number between 0 and 100")

    def show_details(self):
        print("Brand:", self.brand)
        print("Battery:", self.battery, "%")


laptop = Laptop("Asus", 80)

laptop.show_details()

laptop.battery = 65

print()

laptop.show_details()
```

### Output

```text
Brand: Asus
Battery: 80 %

Brand: Asus
Battery: 65 %
```

### What We Learned

- `brand` is public.
- `__battery` is private-style storage.
- The property getter provides access to the battery value.
- The setter validates changes.
- `show_details()` uses the public property instead of accessing the storage directly.

This design keeps the battery's storage separate from the way the rest of the program interacts with it.

---

# Part 2 — Abstraction

## 9. What Is Abstraction?

**Abstraction** means exposing essential functionality while hiding unnecessary implementation details.

For example, when we call:

```python
laptop.start()
```

we want to start the laptop without needing to understand every internal operation required to do so.

In Python, abstraction can be implemented using abstract base classes from the `abc` module.

An abstract base class defines methods that subclasses are expected to implement.

---

## 10. The `ABC` Class

Python provides the `ABC` class in the `abc` module.

`ABC` stands for **Abstract Base Class**.

We can inherit from `ABC` when defining a class intended to specify a common interface for its subclasses.

### Example

```python
from abc import ABC, abstractmethod


class Laptop(ABC):

    @abstractmethod
    def start(self):
        pass
```

### Explanation

- `from abc import ABC, abstractmethod` imports the required tools.
- `class Laptop(ABC)` defines an abstract base class.
- `@abstractmethod` marks `start()` as an abstract method.
- `pass` means the method body does nothing.

Because `Laptop` contains an abstract method, we cannot instantiate it until all its abstract methods have been implemented by a concrete subclass.

For example:

```python
laptop = Laptop()
```

This raises a `TypeError`.

---

## 11. The `@abstractmethod` Decorator

The `@abstractmethod` decorator marks a method that concrete subclasses must implement.

### Example

```python
from abc import ABC, abstractmethod


class Laptop(ABC):

    @abstractmethod
    def start(self):
        pass


class GamingLaptop(Laptop):

    def start(self):
        print("Gaming laptop is starting")


laptop = GamingLaptop()

laptop.start()
```

### Output

```text
Gaming laptop is starting
```

### Explanation

1. `Laptop` defines the abstract method `start()`.
2. `GamingLaptop` inherits from `Laptop`.
3. `GamingLaptop` implements `start()`.
4. The child class can now be instantiated.
5. Calling `start()` executes the child's implementation.

The abstract base class specifies what a concrete subclass must provide, while the subclass defines how it works.

---

## 12. Why Can't We Instantiate an Abstract Class?

Consider:

```python
from abc import ABC, abstractmethod


class Laptop(ABC):

    @abstractmethod
    def start(self):
        pass


laptop = Laptop()
```

### Result

Python raises a `TypeError` because `Laptop` still has an unimplemented abstract method.

An abstract class is intended to define a common interface rather than serve as a directly instantiated concrete class.

### Example With an Incomplete Child Class

```python
from abc import ABC, abstractmethod


class Laptop(ABC):

    @abstractmethod
    def start(self):
        pass


class GamingLaptop(Laptop):
    pass


laptop = GamingLaptop()
```

This also raises a `TypeError`.

Although `GamingLaptop` inherits from `Laptop`, it has not implemented the abstract method `start()`.

**Rule:** A subclass must implement all inherited abstract methods before Python allows it to be instantiated.

---

## 13. Implementing Multiple Abstract Methods

An abstract base class can define more than one abstract method.

### Example

```python
from abc import ABC, abstractmethod


class Laptop(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass


class GamingLaptop(Laptop):

    def start(self):
        print("Gaming laptop is starting")

    def shutdown(self):
        print("Gaming laptop is shutting down")


laptop = GamingLaptop()

laptop.start()
laptop.shutdown()
```

### Output

```text
Gaming laptop is starting
Gaming laptop is shutting down
```

### Explanation

`GamingLaptop` implements both required methods:

- `start()`
- `shutdown()`

Therefore, the class is concrete and can be instantiated.

If either abstract method were missing, instantiating `GamingLaptop` would raise a `TypeError`.

---

## 14. An Abstract Method Can Have a Method Body

An abstract method does not always need to contain only `pass`.

It can have a method body that a subclass may reuse through `super()`.

### Example

```python
from abc import ABC, abstractmethod


class Laptop(ABC):

    @abstractmethod
    def show_details(self):
        print("Common laptop details")


class GamingLaptop(Laptop):

    def show_details(self):
        super().show_details()
        print("GPU: RTX 5050")


laptop = GamingLaptop()

laptop.show_details()
```

### Output

```text
Common laptop details
GPU: RTX 5050
```

### Explanation

- `@abstractmethod` marks `show_details()` as abstract.
- The parent method still contains executable code.
- `GamingLaptop` implements the abstract method.
- `super().show_details()` calls the parent's implementation.
- The child adds its own details afterward.

**Important:** The method remains abstract because of the `@abstractmethod` decorator, not because of the presence or absence of `pass`.

An abstract method can therefore provide reusable behavior while still requiring subclasses to implement the method.

---

## 15. Abstraction With Different Laptop Types

Let's build an example with a common abstract interface and multiple concrete implementations.

```python
from abc import ABC, abstractmethod


class Laptop(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def show_details(self):
        pass


class GamingLaptop(Laptop):

    def start(self):
        print("Gaming laptop is starting")

    def show_details(self):
        print("Gaming laptop: RTX 5050")


class OfficeLaptop(Laptop):

    def start(self):
        print("Office laptop is starting")

    def show_details(self):
        print("Office laptop: 16GB RAM")


gaming = GamingLaptop()
office = OfficeLaptop()

gaming.start()
gaming.show_details()

print()

office.start()
office.show_details()
```

### Output

```text
Gaming laptop is starting
Gaming laptop: RTX 5050

Office laptop is starting
Office laptop: 16GB RAM
```

### Explanation

The abstract `Laptop` class defines the operations every concrete laptop type must provide.

The child classes implement those operations differently.

- `GamingLaptop` defines gaming-specific behavior.
- `OfficeLaptop` defines office-laptop behavior.

The code that uses these objects can rely on the shared interface without requiring every laptop type to work internally in the same way.

---

# Part 3 — Encapsulation vs Abstraction

## 16. Difference Between Encapsulation and Abstraction

These concepts are related, but they are not the same.

| Encapsulation | Abstraction |
|---|---|
| Organizes data and methods together and controls how data is accessed or modified. | Exposes essential operations while hiding unnecessary implementation details. |
| Often uses properties, getters, setters, and private-style attributes. | Can use abstract base classes and abstract methods. |
| Focuses on managing and protecting the object's internal state. | Focuses on defining what an object should do without requiring users to know how it works. |
| Example: Validating a battery percentage before updating it. | Example: Requiring each laptop type to implement `start()`. |

### Simple Comparison

**Encapsulation:**

```python
laptop.battery = 65
```

A property setter can validate the new value before storing it.

**Abstraction:**

```python
laptop.start()
```

The user calls a common operation without needing to know its internal implementation.

---

## 17. Complete Example Combining Encapsulation and Abstraction

The following program combines both concepts in a laptop-management system.

```python
from abc import ABC, abstractmethod


class Laptop(ABC):

    def __init__(self, brand, battery):
        self.brand = brand
        self.battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):

        if isinstance(value, (int, float)) and not isinstance(value, bool) and 0 <= value <= 100:
            self.__battery = value
        else:
            raise ValueError("Battery must be a number between 0 and 100")

    @abstractmethod
    def start(self):
        pass

    def show_details(self):
        print("Brand:", self.brand)
        print("Battery:", self.battery, "%")


class GamingLaptop(Laptop):

    def __init__(self, brand, battery, gpu):
        super().__init__(brand, battery)
        self.gpu = gpu

    def start(self):
        print("Gaming laptop is starting")

    def show_details(self):
        super().show_details()
        print("GPU:", self.gpu)


class OfficeLaptop(Laptop):

    def __init__(self, brand, battery, ram):
        super().__init__(brand, battery)
        self.ram = ram

    def start(self):
        print("Office laptop is starting")

    def show_details(self):
        super().show_details()
        print("RAM:", self.ram)


gaming = GamingLaptop("Asus", 80, "RTX 5050")
office = OfficeLaptop("Dell", 90, "16GB")

gaming.start()
gaming.show_details()

print()

office.start()
office.show_details()
```

### Output

```text
Gaming laptop is starting
Brand: Asus
Battery: 80 %
GPU: RTX 5050

Office laptop is starting
Brand: Dell
Battery: 90 %
RAM: 16GB
```

### Concepts Demonstrated

1. **Abstraction:** `Laptop` defines the abstract `start()` method.
2. **Encapsulation:** `__battery` is private-style storage.
3. **Validation:** The `battery` property rejects invalid values.
4. **Inheritance:** `GamingLaptop` and `OfficeLaptop` inherit from `Laptop`.
5. **Constructor reuse:** `super().__init__(brand, battery)` initializes common attributes.
6. **Method overriding:** Child classes implement `start()` and customize `show_details()`.
7. **Code reuse:** `super().show_details()` reuses common display logic.

This example demonstrates how OOP concepts work together in a practical program.

---

## 18. Important Points to Remember

### Encapsulation

- Encapsulation groups data and related methods inside a class.
- Public attributes can be accessed directly.
- A single leading underscore indicates a non-public attribute by convention.
- Two leading underscores trigger name mangling.
- Name mangling does not provide absolute privacy.
- Getters retrieve values, while setters update them.
- `@property` supports attribute-style access with getter logic.
- `@property_name.setter` defines the setter for a property.
- Validation can prevent invalid state changes.

### Abstraction

- Abstraction exposes essential operations and hides unnecessary implementation details.
- `ABC` is available from Python's `abc` module.
- `@abstractmethod` marks a method as abstract.
- Abstract classes cannot be instantiated while abstract methods remain unimplemented.
- A concrete subclass must implement all inherited abstract methods.
- Abstract methods can contain executable code.
- `super()` can call an abstract method's parent implementation when that method has a body.

---

## 19. Day 20 Summary

| Concept | Meaning |
|---|---|
| Encapsulation | Organizing data and methods and controlling access to internal state |
| Public attribute | An attribute intended for normal external access |
| Protected-style attribute | A single-underscore attribute intended for internal use by convention |
| Private-style attribute | A double-leading-underscore attribute subject to name mangling |
| Getter | Retrieves an attribute's value |
| Setter | Updates an attribute, potentially after validation |
| `@property` | Provides attribute-style access to getter logic |
| `@battery.setter` | Defines a setter for the `battery` property |
| Abstraction | Exposes essential operations while hiding unnecessary implementation details |
| `ABC` | Base class for defining abstract base classes |
| `@abstractmethod` | Marks a method that concrete subclasses must implement |
| `super()` | Calls methods through the parent-class method resolution order |

**Day 20 completed:** Encapsulation, public and non-public attributes, name mangling, getters, setters, properties, abstraction, abstract base classes, and abstract methods.

**Next step:** Continue to Day 21 of the Python practice plan.
