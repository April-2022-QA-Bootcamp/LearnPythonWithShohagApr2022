#Note----
#When we create obj----internally it is calling __init__() method----which is constructor in python
#__ini__() is called magaic/dunder method too.
#__init__method is responsible to initialize the obj

#class
class MyClass:
    name="sohag"

#Obj
myObj=MyClass()

##Lets check how internally __init__() magic method is being invoked
#class
class MyClass1:
    name="Sohag"

    #__init__()----we are giving some print statement to see it is invoked or not (when obj created print statement will be executed)
    def __init__(self):
        print("I am from __init__method")

#obj
obj1=MyClass1()   #Note: __init__() is invoked here---so you will see print statement is executed

#if we create another obj---again it will invoke __init__method, so we will see print statement again
obj2=MyClass1()