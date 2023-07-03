#Alexza Jean R. Catanoy
#BSCPE 1-4
#Abstraction and Encasulation

#Title
print("\033[0;36m*" * 90)
print("\033[1;97mThe Fan Class".center(97))
print("\033[0;36m*" * 90)

print("\033[1;32m\nHello! Your programmers name is Alexza Jean.")
print("\033[1;32m\nShe's from BSCPE 1-4")
print("-" * 90)

#(The Fan Class) Design a class named Fan to represent a fan. The class contains:
class Fan:

    #Three constants named SLOW, MEDIUM, and FAST with the values 1, 2, 3 to denote the fan speed.
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5, color='blue', on=False):
        #A private int data field named on that specifies the speed of the fan.
        self.__speed = speed

        #A private bool data field named on that specifies whether the fan is on (the default is False).
        self.__on = on

        #A private float field named radius that specifies the radius of the fan.
        self.__radius = radius

        #A private string data field named color that specifies the color of the fan.
        self.__color = color

    #The accessor(getters) methods for all four data fields.
    def get_speed(self):
        return self.__speed
    
    def is_on(self):
        return self.__on
    
    def get_radius(self):
        return self.__radius
    
    def get_color(self):
        return self.__color
    
    #The mutator(setters) methods for all four data fields.
    def set_speed(self, speed):
        self.__speed = speed

    def set_on(self, on):
        self.__on = on

    def set_radius(self, radius):
        self.__radius = radius

    def set_color(self, color):
        self.__color = color

      