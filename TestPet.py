from Pet import Pet

class TestPet:

    def Test(self):

        #Write a program that create an object of the class.
        pet = Pet()

        #Prompts the user to enter the name of pet.
        name = str(inout("Kindly type in the name of your pet: "))
        pet.set_name(name)
        
        #Prompts the user to enter the type of pet.
        #Prompts the user to enter the age of the pet
        #Display the output.
