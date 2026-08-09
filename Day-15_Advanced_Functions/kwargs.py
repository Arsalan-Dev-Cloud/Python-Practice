#----------Program for **kwargs-----------

def student(**details):
    print(details,"\n")

student(
    Name = "Arsalan",
    Course = "Big Data",
    Marks = "90"
)


#---------Loop through **kwargs---------

def student(**details):
    for key, value in details.items():
        print(f"{key:<10}: {value}")


student(
    Name="Arsalan",
    Course="Big Data",
    Marks="90"
)