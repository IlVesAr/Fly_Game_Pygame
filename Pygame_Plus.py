import pygame

class Figura:
    def __init__(self, x, y, vel, color):
        self.x = x
        self.y = y
        self.vel = vel
        self.color = color


class color:
    white = (255, 255, 255)
    black = (0, 0, 0)

    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    yellow = (255, 255, 0)
    pink = (255, 44, 180)
    purple = (153, 90, 233)
    orange = (255, 130, 46)
    cyan = (0, 255, 255)
    magenta = (255, 0, 255)


class Kvadrat(Figura):
    def __init__(self, x, y, w, h, width, vel, color):
        super().__init__(x, y, vel, color)
        self.w = w
        self.h = h
        self.width = width

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.w, self.h), self.width)


class Krag(Figura):
    def __init__(self, x, y, radius, width, vel, color):
        super().__init__(x, y, vel, color)
        self.radius = radius
        self.width = width

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius, self.width)


class Liniq(Figura):
    def __init__(self, x, y, x_end, y_end, width, vel, color):
        super().__init__(x, y, vel, color)
        self.x_start = x
        self.y_start = y
        self.x_end = x_end
        self.y_end = y_end
        self.width = width

    def draw(self, win):
        pygame.draw.line(win, self.color, (self.x_start, self.y_start), (self.x_end, self.y_end), self.width)


class Polygon(Figura):
    def __init__(self, tochki, width, vel, color):
        super().__init__(vel, color)
        self.tochki = tochki
        self.width = width

    def draw(self, win):
        pygame.draw.polygon(win, self.color, self.tochki, self.width)


class Ellipse(Figura):
    def __init__(self, tochki, width, vel, color):
        super().__init__(vel, color)
        self.tochki = tochki
        self.width = width

    def draw(self, win):
        pygame.draw.ellipse(win, self.color, self.tochki, self.width)


class AA_Liniq(Figura):
    def __init__(self, x, y, x_end, y_end, blend, vel, color):
        super().__init__(x, y, vel, color)
        self.x_start = x
        self.y_start = y
        self.x_end = x_end
        self.y_end = y_end
        self.blend = blend

    def draw(self, win):
        pygame.draw.aaline(win, self.color, (self.x_start, self.y_start), (self.x_end, self.y_end), self.blend)


class AA_Linii(Figura):
    def __init__(self, tochki, closed, blend, vel, color):
        super().__init__(vel, color)
        self.tochki = tochki
        self.blend = blend
        self.closed = closed

    def draw(self, win):
        pygame.draw.aalines(win, self.color, self.closed, self.tochki, self.blend)


