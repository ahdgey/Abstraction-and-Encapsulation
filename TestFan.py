from Fan import Fan

class TestFan:

    def __init__(self):
        fan_1 = Fan(Fan.FAST, 10, 'yellow', True)
        fan_2 = Fan(Fan.MEDIUM, 5, 'blue', False)

        #Fan number 1, assign maximum speed, radius 10, color yellow, and turm it on.
        print("\033[0;33mFan 1:")
        print("\033[0;31mThe speed of the fan: \033[1;37m", fan_1.get_speed())
        print("\033[0;31mThe radius of the fan: \033[1;37m", fan_1.get_radius())
        print("\033[0;31mThe color of the fan: \033[1;37m", fan_1.get_color())
        print("\033[0;31mThe fan is on: \033[1;37m", fan_1.is_on())

        #Fan number 2, assign medium speed, radius 5, color blue, and turn it off.
        print("\033[0;33m\nFan 2:")
        print("\033[0;31mThe speed of the fan: \033[1;37m", fan_2.get_speed())
        print("\033[0;31mThe radius of the fan: \033[1;37m", fan_2.get_radius())
        print("\033[0;31mThe color of the fan: \033[1;37m", fan_2.get_color())
        print("\033[0;31mThe fan is on: \033[1;37m", fan_2.is_on())

TestFan()