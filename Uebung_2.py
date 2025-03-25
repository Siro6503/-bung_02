import math

class Vektor3:
    def __init__(self, x ,y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    def __add__(self, other):
        return Vektor3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __mul__(self, other):
      if type(other) == Vektor3:
         return Vektor3(self.x * other.x, self.y * other.y, self.z * other.z)
      
      elif type(other) in [int, float]:
         return Vektor3(self.x * other, self.y * other, self.z * other)
      
      else:
        raise TypeError("TypeError")
      
    def dot(self, other):
       return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):
        cx = self.y * other.z - self.z * other.y
        cy = self.z * other.x - self.x * other.z
        cz = self.x * other.y - self.y * other.x
        return Vektor3(cx, cy, cz)
    
    def normalize(self):
        length = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        if length == 0:
            return Vektor3(0,0,0)
        return Vektor3(self.x/length, self.y/length, self.z/length)
    



v0 = Vektor3(1, 2, 3)
v1 = Vektor3(10, 20, 30)

v2 = v0 * v1

d = v0.cross(v1)

n = v0.normalize()

print(n)
