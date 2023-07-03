from Fan import Fan

class TestFan:

    def __init__(self):
        fan_1 = Fan(Fan.FAST, 10, 'yellow', True)
        fan_2 = Fan(Fan.MEDIUM, 5, 'blue', False)

    #Fan number 1, assign maximum speed, radius 10, color yellow, and turm it on.
    #Fan number 2, assign medium speed, radius 5, color blue, and turn it off.
    