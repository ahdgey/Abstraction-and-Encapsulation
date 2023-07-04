from Pet import Pet

class TestPet:

    def Test(self):

        #Write a program that create an object of the class.
        pet = Pet()

        #Prompts the user to enter the name of pet.
        name = str(input("\033[0;33mKindly type in the name of your pet: \033[1;37m"))
        pet.set_name(name)

        #Prompts the user to enter the type of pet.
        animal_type = str(input("\033[0;33mKindly type in the type of animal of ypur pet: \033[1;37m"))
        pet.set_animal_type(animal_type)

        #Prompts the user to enter the age of the pet
        age = int(input("\033[0;33mKindly type in the age of your pet: \033[1;37m"))
        pet.set_age(age)

        #Display the output.
        print("\033[0;31m\nPet's name: \033[1;37m", pet.get_name())
        print("\033[0;31mPet's animal type: \033[1;37m", pet.get_animal_type())
        print("\033[0;31mPet's age: \033[1;37m", pet.get_age())

test = TestPet()
test.Test()
