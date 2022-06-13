#following Car is the class--as class is the blue print of obj, we can have multiple obj of Car class
class Car:
    model=''
    speed=0
#in java we use new keyword followed by class name and ()-----new Car()
#in python ----Creating the obj----put the name of the class followed by ()

#1st obj:
toyotaCar=Car()
#assigning the value for the obj property
toyotaCar.model="Corolla"
print(toyotaCar.model)

#2nd obj
BMW=Car()
#assigning value for obj propery
BMW.model="430i"
print(BMW.model)

#anotther obj
HondaCar=Car()
#assigning value for obj propery
HondaCar.model="CRV"
print(HondaCar.model)

#Modifying the propery
HondaCar.model="H-CRV"
print(HondaCar.model)
##Note: Wehen assign any value for any obj propery that means
# we are assigning only for that obj propery....it will change for other obj

#We can delete the obj
del BMW
#print(BMW.model)  # if you print--we get an error as obj is not there anymore