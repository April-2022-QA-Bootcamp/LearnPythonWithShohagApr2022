"""
Note: When obj created __init__() method is invoked to initialized the obj
but before that another magic method is invoked which __new__() to create the obj
That means __new__()--------------will create the obk
           __init__()-------------will initialize the obj
"""

#lets see __add__method is invoked or not

#class
class MyClass1:
    name="Sohag"

    #__new__()-we are giving some print statement to check it is invoked or not---if we can see that menas invoked
    def __new__(cls, *args, **kwargs):
        print("I am invoked (Executed)---obj is created")


#obj
obj1=MyClass1()   #Note: here __new__method is invoked -so you will see print statement is executed

#if we create another obj---again __new__method is invoked -so you will see print statement is executed so we will print stament again
obj2=MyClass1()

