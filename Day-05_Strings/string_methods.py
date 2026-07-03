#--------Common String Mehtods-----------
name = "arsalan"
print(name.upper())

name = "ARSALAN"
Print(name.lower())

name = "shaikh arsalan"
print(name.title())

text = "python programming"
print(text.capitalize())

text = "   Python   "
print(text.strip())

text = "I like Java"
print(text.replace("Java", "Python"))

text = "Python Programming"
print(text.find("Programming"))

text = "banana"
print(text.count("a"))

text = "Python"
print(text.startswith("Py"))

text = "report.pdf"
print(text.endswith(".pdf"))

sentence = "Python SQL Azure"
print(sentence.split())

words = ["Python", "SQL", "Azure"]
print(" | ".join(words))


name = "Arsalan"
course = "Python"

print(f"My name is {name}.")
print(f"I am learning {course}.")


#-----------------Output-----------------------
ARSALAN
arsalan
Shaikh Arsalan
Python programming
Python
I like Python
7
3
True
True
['Python', 'SQL', 'Azure']
Python | SQL | Azure
My name is Arsalan.
I am learning Python.
