from Fan import Fan

class TestFan:

    def __init__(self):
        fan_1 = Fan(Fan.FAST, 10, 'yellow', True)
        fan_2 = Fan(Fan.MEDIUM, 5, 'blue', False)

        #Fan number 1, assign maximum speed, radius 10, color yellow, and turm it on.
        print("Fan 1:")
        print("The speed of the fan:", fan_1.get_speed())
        print("The radius of the fan:", fan_1.get_radius())
        print("The color of the fan:", fan_1.get_color())
        print("The fan is on:", fan_1.is_on())

        #Fan number 2, assign medium speed, radius 5, color blue, and turn it off.
        print("\nFan 2:")
        print("The speed of the fan:", fan_2.get_speed())
        print("The radius of the fan:", fan_2.get_radius())
        print("The color of the fan:", fan_2.get_color())
        print("The fan is on:", fan_2.is_on())

TestFan()