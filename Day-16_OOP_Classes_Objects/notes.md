
# Day 16 — Class Methods and Static Methods in Python

## Learning Objectives

By the end of this lesson, you should understand:

- What instance methods, class methods, and static methods are.
- The difference between `self` and `cls`.
- How the `@classmethod` decorator works.
- How the `@staticmethod` decorator works.
- When to use each type of method.
- How to validate input using a static method.

---

## 1. What Is a Method?

A **method** is a function defined inside a class.

Example:

```python
class Laptop:
    def show_message(self):
        print("This is a laptop.")

laptop1 = Laptop()
laptop1.show_message()
```

Output:

```text
This is a laptop.
```

Explanation:

- `class Laptop:` defines a class.
- `show_message()` is a method.
- `laptop1 = Laptop()` creates an object.
- `laptop1.show_message()` calls the method using that object.
- `self` refers to the current object.

Python has three common method types that we studied:

1. Instance methods
2. Class methods
3. Static methods

---

## 2. Instance Methods

An **instance method** works with the data of a particular object.

It normally uses `self` as its first parameter.

### Example

```python
class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_details(self):
        print("Brand:", self.brand)
        print("Price:", self.price)


laptop1 = Laptop("Asus", 150000)
laptop2 = Laptop("Dell", 70000)

laptop1.show_details()
print()
laptop2.show_details()
```

Output:

```text
Brand: Asus
Price: 150000

Brand: Dell
Price: 70000
```

### Explanation

When we execute:

```python
laptop1.show_details()
```

Python calls the method for `laptop1`. Inside that method, `self` refers to `laptop1`.

When we execute:

```python
laptop2.show_details()
```

`self` refers to `laptop2`.

Therefore, the same method can display different information for different objects.

### Key Points

- `self` refers to the current object.
- Instance methods can access and modify an object's attributes.
- `self` is the conventional name for the first parameter of an instance method.

---

## 3. Class Attributes and Class Methods

### What Is a Class Attribute?

A **class attribute** is defined directly inside a class, outside its methods.

It belongs to the class and is shared by instances unless an instance attribute with the same name shadows it.

Example:

```python
class Laptop:
    laptop_count = 0

    def __init__(self, brand):
        self.brand = brand
        Laptop.laptop_count += 1


laptop1 = Laptop("Asus")
laptop2 = Laptop("Dell")
laptop3 = Laptop("Acer")

print("Total laptops:", Laptop.laptop_count)
```

Output:

```text
Total laptops: 3
```

Every time a `Laptop` object is initialized, the counter increases by one.

### What Is a Class Method?

A **class method** works with the class itself rather than a particular object's data.

It uses the `@classmethod` decorator and receives the class as its first parameter, conventionally named `cls`.

### Example

```python
class Laptop:
    laptop_count = 0

    def __init__(self, brand):
        self.brand = brand
        Laptop.laptop_count += 1

    @classmethod
    def show_count(cls):
        print("Total laptops:", cls.laptop_count)


laptop1 = Laptop("Asus")
laptop2 = Laptop("Dell")
laptop3 = Laptop("Acer")

Laptop.show_count()
```

Output:

```text
Total laptops: 3
```

### Understanding the Code

```python
@classmethod
def show_count(cls):
```

- `@classmethod` tells Python that this is a class method.
- `cls` refers to the class through which the method was called.
- `cls.laptop_count` accesses the class attribute.
- `Laptop.show_count()` calls the method through the class.

We do not need to pass `cls` manually.

### Why Use `cls` Instead of the Class Name?

Using `cls` makes the method work more flexibly with subclasses.

```python
class Laptop:
    laptop_count = 0

    @classmethod
    def show_count(cls):
        print(cls.laptop_count)


class GamingLaptop(Laptop):
    laptop_count = 5


Laptop.show_count()
GamingLaptop.show_count()
```

Output:

```text
0
5
```

When called through `GamingLaptop`, `cls` refers to `GamingLaptop`.

### When Should We Use a Class Method?

Use a class method when the operation needs to work with class-level information, such as:

- Reading or updating class attributes.
- Working with class-level configuration.
- Creating objects through alternative constructors.

---

## 4. Static Methods

A **static method** is a function placed inside a class because it is related to that class, but it does not need automatic access to a particular object or to the class itself.

It uses the `@staticmethod` decorator.

A static method does not automatically receive `self` or `cls`.

### Example: Calculating a Discount

```python
class Laptop:
    @staticmethod
    def calculate_discount(price, discount):
        if discount < 0 or discount > 100:
            return "Invalid discount"

        final_price = price - (price * discount / 100)
        return final_price


print(Laptop.calculate_discount(250000, 10))
print(Laptop.calculate_discount(250000, 0))
print(Laptop.calculate_discount(250000, 100))
print(Laptop.calculate_discount(250000, -1))
print(Laptop.calculate_discount(250000, 110))
```

Output:

```text
225000.0
250000.0
0.0
Invalid discount
Invalid discount
```

### Explanation

The method receives two arguments:

- `price`: the original price of the laptop.
- `discount`: the discount percentage.

This condition checks whether the discount is outside the valid range:

```python
if discount < 0 or discount > 100:
```

If the discount is invalid, the method returns a message.

Otherwise, Python calculates:

```python
final_price = price - (price * discount / 100)
```

For a price of `250000` and a discount of `10`:

- Discount amount = `250000 * 10 / 100`
- Discount amount = `25000`
- Final price = `250000 - 25000`
- Final price = `225000`

### Why Is This a Static Method?

The calculation only needs the values passed into it.

It does not need to access:

- `self.brand`
- Any particular object's attributes
- A class attribute through `cls`

Therefore, a static method is suitable.

### Difference Between `return` and `print`

```python
return final_price
```

Returns a value to the caller.

```python
print(final_price)
```

Displays a value on the screen.

Returning a value is more flexible because the caller can store it, use it in another calculation, or print it later.

---

## 5. Comparing the Three Method Types

| Feature | Instance Method | Class Method | Static Method |
|---|---|---|---|
| Decorator | None usually | `@classmethod` | `@staticmethod` |
| First parameter | `self` | `cls` | No automatic parameter |
| Receives object automatically | Yes | No | No |
| Receives class automatically | No | Yes | No |
| Main purpose | Work with object data | Work with class data | Utility operations |

### How to Choose the Correct Method

Ask yourself these questions:

**Question 1:** Does the method need an object's data?

Use an instance method.

**Question 2:** Does the method need the class itself or class-level information?

Consider a class method.

**Question 3:** Does the method only need the arguments passed into it?

A static method may be suitable.

These are guidelines. Choose the simplest method type that fits the task.

---

## 6. Common Mistakes

### Mistake 1: Forgetting `self`

Incorrect:

```python
class Laptop:
    def show_brand():
        print("Asus")


laptop1 = Laptop()
laptop1.show_brand()
```

This raises a `TypeError` because Python passes the object automatically, but the method does not accept a parameter for it.

Correct:

```python
class Laptop:
    def show_brand(self):
        print("Asus")


laptop1 = Laptop()
laptop1.show_brand()
```

Output:

```text
Asus
```

### Mistake 2: Forgetting `@classmethod`

A class method should be defined with the appropriate decorator.

```python
@classmethod
def show_count(cls):
    print(cls.laptop_count)
```

### Mistake 3: Expecting a Static Method to Receive `self`

A static method does not automatically receive an object.

```python
@staticmethod
def calculate_discount(price, discount):
    ...
```

Pass the required values as arguments.

### Mistake 4: Confusing `return` and `print`

- `print()` displays a value.
- `return` sends a value back to the caller.

A method can return a value without displaying anything.

---

## 7. Day 16 Summary

### Instance Method

- Uses `self`.
- Works with an individual object's data.
- Can read or modify object attributes.

### Class Method

- Uses the `@classmethod` decorator.
- Receives `cls`.
- Works with class-level information.

### Static Method

- Uses the `@staticmethod` decorator.
- Does not automatically receive `self` or `cls`.
- Is useful for related utility calculations and validation.

### Additional Concepts

- A class attribute is defined on the class and can be shared by instances.
- Input validation checks whether a value follows expected rules.
- `return` provides a result to the caller.
- `print()` displays a result.

---

## 8. Revision Checklist

Before moving to the next topic, make sure you can explain:

- [ ] What `self` means.
- [ ] What `cls` means.
- [ ] What an instance method does.
- [ ] Why `@classmethod` is used.
- [ ] Why `@staticmethod` is used.
- [ ] The difference between `return` and `print()`.
- [ ] How the laptop discount calculation works.
- [ ] When to choose an instance, class, or static method.

**End of Day 16 Notes**
