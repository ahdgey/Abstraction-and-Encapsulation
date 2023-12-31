#Alexza Jean R Catanoy
#BSCPE 1-4
#Abstraction and Encapsulation

#Title
print("\033[0;36m*" * 90)
print("\033[1;97mThe Car Class".center(97))
print("\033[0;36m*" * 90)

print("\033[1;32m\nHello! Your programmers name is Alexza Jean.")
print("\033[1;32m\nShe's from BSCPE 1-4")
print("\033[1;32m-" * 90)

#Write a class named Car that has the following data attributes:
class Car:

    def __init__(self, year_model, make, speed=0):

        #_ _year_model(for the car's year model)
        self.__year_model = year_model
    
        #_ _make(for the make of the car)
        self.__make = make
    
        #_ _speed(fpr the car's current speed)
        self.__speed = speed
    
#The class should also have the following methods:
    
    #accelerate()
    def accelerate(self):
    #The accelerate method should add 5 to the speed data attribute each time it is called.
        self.__speed += 5

    #brake()
    def brake(self):
    #The brake method should subtract 5 from the speed data attribute each time it is called.
        self.__speed -= 5

    #get_speed()
    def get_speed(self):
    #The get_speed should return the current speed.
        return self.__speed
    
    def show(self):
        print("\033[0;31mYear Model of the Car: \033[1;37m", self.__year_model)
        print("\033[0;31mMake of the car: \033[1;37m", self.__make)
        print("\033[0;31mInitial speed of the car: \033[1;37m", self.__speed)
        print("\033[0;31m~" * 90)