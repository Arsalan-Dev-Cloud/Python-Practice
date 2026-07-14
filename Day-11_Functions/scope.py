#-------------Local Scope-------------
def demo():
    x = 20
    print(x) # 20

demo()


#-------------Global Scope-------------
x = 100

def demo():
    print(x) # 100

demo()

