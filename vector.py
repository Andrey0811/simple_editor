import math


class Vector:

	def __init__(self, x=0.0, y=0.0, z=0.0):
		self.x = x
		self.y = y
		self.z = z

	def distance(self) -> float:
		return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

	def __add__(self, v: 'Vector') -> 'Vector':
		if isinstance(v, Vector):
			return Vector(self.x + v.x, self.y + v.y, self.z + v.z)
		else:
			raise TypeError('Add not with a vector!')

	def __sub__(self, v: 'Vector') -> 'Vector':
		if isinstance(v, Vector):
			return Vector(self.x - v.x, self.y - v.y, self.z - v.z)
		else:
			raise TypeError('Sub not with a vector!')

	def __neg__(self):
		return Vector(-self.x, -self.y, -self.z)
	
	def __mul__(self, val) -> 'Vector':
		if isinstance(val, int) or isinstance(val, float):
			return Vector(self.x * val, self.y * val, self.z * val)
		elif isinstance(val, Vector):
			return Vector(self.x * val.x, self.y * val.y, self.z * val.z)
		else:
			raise TypeError('Multiplication not with vector, int or float')

	def normalize(self):
		dist = self.distance()
		if dist != 0:
			self.x /= dist
			self.y /= dist
			self.z /= dist
		else:
			raise TypeError('Normalizing zero vector')

	def dot(self, v: 'Vector') -> float:
		if isinstance(v, Vector):
			return self.x * v.x + self.y * v.y + self.z * v.z
		else:
			raise TypeError('Dot not with a vector')

	def cross(self, v: 'Vector') -> 'Vector':
		if isinstance(v, Vector):
			return Vector(self.y * v.z - self.z * v.y, self.z * v.x - self.x * v.z, self.x * v.y - self.y * v.x)
		else:
			raise TypeError('Cross not with a vector')
