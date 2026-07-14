#-------------Local Scope-------------
def demo():
    x = 10
    print(x) # 10

demo()


#-------------Global Scope-------------
x = 100

def demo():
    print(x) # 100

demo()

