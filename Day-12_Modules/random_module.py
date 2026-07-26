#-----------Random Module------------------
import random
print(random.randint(1,10)) # it may choice any number between 1 and 10 


import random
fruits = ["Apple", "Banana", "Mango"]
print(random.choice(fruits)) # it may choose any fruit from given fruits randomly

import random
numbers = [1,2,3,4,5]
random.shuffle(numbers)
print(numbers) # it may shuffle the given numbers in any order
