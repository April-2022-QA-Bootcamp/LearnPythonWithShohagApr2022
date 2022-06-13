"""
Note: In java-class name(){} ---is constructor
in Python __init__() this magic method is called constructor
same in Python if we dont create constructor-Python inpreter will give us default constructor
-we can have one constructor only-if we create multiple constructor then last constructor should be considered as the final one
****also we need to be careful for passing value for the parameter in the time of obj creation
**first pram in constructor is always self---we can have diff name as well
"""

#Class
class MyClass:

#default constructor------here we commented out becasue we have parameterized constructor which will replace this default constructor
    # def __init__(self):
    #     print("this is default constructor")

#Parametrized constructor -------here we commented out becasue we have next parameterized constructor which will replace this default constructor
    # def __init__(self,name,age):
    #     self.name=name
    #     self.age=age
    #     print("I am initializing the obj ---from 2 param const")

    def __init__(help,name):  #we can also get diff name for self param
        help.name=name
        print("I am initializing the obj ---from  1 param const")
#Obj creation

"""
In Jave as it is typed language,we need to mention the type of ref variable like, MyClass obj=new MyClass()
but in Python we will just put in ref varibale
"""
#in Python ----class name ()----and then put in ref variable

#By default const-commented out, as we have next cons--so we dont need it...if we keep will get an error
#obj1=MyClass()

#By 2pram const-commented out, as we have next cons--so we dont need it...if we keep will get an error
#obj2=MyClass("Sohag",42) #as we have param cons--so we dont need it...if we keep will get an error

#By 1pram cons
obj3=MyClass("Tofayel")


