from Car import Car

class TestCar:

    def Test(self):
        car = Car(2023, "Mazda 5")
        car.show()

        #Call the accelerate method five times.
        for i in range(5):
            car.accelerate()
            print("The car's current speed after it accelerates", i+1, "times is:", car.get_speed())
            
        #Call the brake method five times. 