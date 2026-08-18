"""
Ask the user to enter a sentence.                           

Your program should calculate and display:

Original sentence
Total number of characters
Number of vowels
Number of consonants
Number of spaces
Number of digits
Number of uppercase letters
Number of lowercase letters


Rules:-
input()
variables
for loop
if / elif / else
len()
f-string

Output:-
Enter a sentence: Hello World 123

------------- Result -------------

Original Sentence     : Hello World 123
Characters            : 15
Vowels                : 3
Consonants            : 7
Spaces                : 2
Digits                : 3
Uppercase             : 2
Lowercase             : 8
"""

# Program:-

char_big = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
char_small = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
num = ["0","1","2","3","4","5","6","7","8","9"]
special_char = ['@','!','#','$','%']

characters = 0
vowels = 0
consonents = 0
spaces = 0
uppercase = 0
lowercase = 0
digits = 0
speical = 0

Sentence = input("Enter a Sentence: ")

for character in Sentence:
    characters += 1
    if character == " ":
        spaces += 1

    elif character in num:
        digits += 1

    elif character in char_big:
        uppercase += 1

        if character in ["A","E","I","O","U"]:
            vowels += 1
        else:
            consonents += 1

    elif character in char_small:
        lowercase += 1

        if character in ["a","e","i","o","u"]:
            vowels += 1
        else:
            consonents +=1

    elif character in special_char:
        speical += 1


print("----------------Report-----------------")
print(f"{'Sentence':<20}: {Sentence}")
print(f"{'Characters':<20}: {characters}")
print(f"{'Uppercase':<20}: {uppercase}")
print(f"{'Lowercase':<20}: {lowercase}")
print(f"{'Vowels':<20}: {vowels}")
print(f"{'Consonants':<20}: {consonents}")
print(f"{'Special characters:':<20}: {speical}")
print(f"{'Spaces':<20}: {spaces}")
print(f"{'Digits':<20}: {digits}")