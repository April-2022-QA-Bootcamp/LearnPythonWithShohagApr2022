#Class:
class EnthralStudents:

#Constructor--we will get value to initialzed the property
#In python we can also define & initialize propery in constructor--we didnt have name and age propery in the calss...we just defined
    def __init__(self,name, age):
        self.name=name
        self.age=age

#1st Obj---passing the value for the obj property
st1=EnthralStudents("Shoborna",23)
print("Student 1:",st1.name)

#2nd Obj:
st2=EnthralStudents("Noyon",23)
print("Student 2:",st2.name)

