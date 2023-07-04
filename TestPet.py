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
        age = int(input("Kindly type in the age of your pet: "))
        pet.set_age(age)

        #Display the output.
        print("\nPet's name: ", pet.get_name())
        print("Pet's animal type: ", pet.get_animal_type())
        print("Pet's age: ", pet.get_age())
        
