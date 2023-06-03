import math
pi = math.pi
class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        self.volume = (4/3)*pi*(radius**3)
        self.surface_area = 4*pi*(radius**2)
        self.density = mass/self.volume
    def get_radius(self):
        return (self.radius)
    def get_mass(self):
        return (self.mass)
    def get_volume(self):
        return (round(self.volume,5))
    def get_surface_area(self):
        return (round(self.surface_area,5))
    def get_density(self):
        return (round(self.density,5))  
ball = Sphere(2,50)
ball.get_radius()   
ball.get_mass()
ball.get_volume()
ball.get_surface_area()
ball.get_densreturn 