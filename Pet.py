#Alexza Jean R. Catanoy
#BSCPE 1-4
#Abstraction and Encapsulation

#Title
print("\033[0;36m*" * 90)
print("\033[1;97mThe Pet Class".center(97))
print("\033[0;36m*" * 90)

print("\033[1;32m\nHello! Your programmers name is Alexza Jean.")
print("\033[1;32m\nShe's from BSCPE 1-4")
print("\033[1;32m-" * 90)

#Write a class named Pet, which should have the following data attributes:
class Pet:

    #The Pet class should have an _ _ init_ _ method that creates these attributes.
    def __init__(self, name="", animal_type="", age=0):

        #_ _name (for the names of pet)
        self.__name = name

        #_ _animal_type (for the type of animal that a pet is. Example values are 'Dog', 'Cat', and 'Bird')
        self.__animal_type = animal_type

        #_ _age (for the pet's age)
        self.__age = age

#It should also have the following methods:
    #set_name()
    def set_name(self, name):
    #This method assigns a value to the _ _name field.
        self.__name = name

    #set_animal_type()
    def set_animal_type(self, animal_type):
    #This method aasigns a value to the _ _animal_type field.
        self.__animal_type = animal_type

    #set_age()
    def set_age(self, age):
    #This method assigns a value to the _ _age field.
        self.__age = age
        
    #get_name()
    #This method returns the value of the _ _name field.
    #get_animal_type()
    #This method returns the value of the _ _animal_type field.
    #get_age()
    #This method returns the value of the _ _age field.