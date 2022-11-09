class Color:
    red = 0
    green = 0
    blue = 0

    def __init__(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b

    def to_hex(self):
        return '#%02x%02x%02x' % (self.red, self.green, self.blue)


class ColorAlpha(Color):
    alpha = 1

    def __init__(self, r, g, b, a):
        self.red = r
        self.green = g
        self.blue = b
        self.alpha = a


gray = Color(80, 90, 10)

print(gray.red)

red = ColorAlpha(255, 0, 0, .5)
print(red.red)
