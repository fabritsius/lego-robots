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


def spiral(size):
    stride_pos = 0
    stride_size = size - 1
    turns = 4
    posX = 0
    posY = 0
    dirX = 1
    dirY = 1
    horizontal = True
    while stride_size > 0:
        yield (posX, posY)
        stride_pos += 1
        turned = False
        if horizontal:
            posX += dirX
            if stride_pos >= stride_size:
                dirX = -dirX
                turned = True   
        else:
            posY += dirY
            if stride_pos >= stride_size:
                dirY = -dirY
                turned = True
        if turned:
            horizontal = not horizontal
            turns -= 1
            if turns <= 0: stride_size -= 1

def run_animation(brightness=100):
    face = Face(Orientation.RIGHT)
    for x, y in spiral(5):
        face.set_pixel(x, y, brightness)
        wait_for_seconds(0.1)

# LEDs light draw a spiral
while True:
    run_animation(100)
    run_animation(0)