from Pet import Pet

class TestPet:

    def Test(self):

        #Write a program that create an object of the class.
        pet = Pet()

        #Prompts the user to enter the name of pet.
        name = str(input("Kindly type in the name of your pet: "))
        pet.set_name(name)

        #Prompts the user to enter the type of pet.
        animal_type = str(input("Kindly type in the type of animal of ypur pet: "))
        pet.set_animal_type(animal_type)
        
        #Prompts the user to enter the age of the pet
        #Display the output.
