#----------Program for args_kwargs.py----------

def information(*args, **kwargs):
    print("Arguments:", args)
    print("Keyword Arguments:", kwargs)

information(
    "Python",
    "SQL",
    Name="Arsalan",
    Course="Big Data"
)

# Output:- 
"""
Arguments: ('Python', 'SQL')
Keyword Arguments: {'Name': 'Arsalan', 'Course': 'Big Data'}
"""