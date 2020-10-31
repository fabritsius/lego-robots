from mindstorms import MSHub
from mindstorms.control import wait_for_seconds


# Create your objects here.
hub = MSHub()

# Write your program here.
hub.speaker.beep()


class Orientation:
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

class Face:
    def __init__(self, orientation=Orientation.UP):
        self.orientation = orientation
        self.size = 5 - 1

    def set_pixel(self, x, y, brightness=100):
        x, y = self.convert_location(x, y)
        hub.light_matrix.set_pixel(x, y, brightness)

    def convert_location(self, x, y):
        if self.orientation == Orientation.RIGHT:
            return (y, self.size - x)
        elif self.orientation == Orientation.DOWN:
            return (self.size - x, self.size - y)
        elif self.orientation == Orientation.LEFT:
            return (self.size - y, x)
        else:
            return (x, y)


def custom_range(n, reversed=False):
    if reversed:
        return range(n-1, -1, -1)
    return range(n)

def run_animation(brightness=100):
    face = Face(Orientation.RIGHT)
    for y in range(5):
        for x in custom_range(5, y % 2 == 1):
            face.set_pixel(x, y, brightness)
            wait_for_seconds(0.1)

# LEDs light one by one given a HUB orientation
while True:
    run_animation(100)
    run_animation(0)