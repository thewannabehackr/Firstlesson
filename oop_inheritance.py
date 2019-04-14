from abc import ABCMeta, abstractmethod
import math

class Polygon:
	__metaclass__ = ABCMeta

	@abstractmethod	
	def area(self):
		pass
	
	@abstractmethod
	def perimeter(self):
		pass

class Triangle(Polygon):
	#Input: three sides 	
	sides = []	
	perimeter = 0
	area = 0

	def __init__(self, sides):
		self.sides = sides

	def perimeter(self):
		self.perimeter = self.sides[0] + self.sides[1] + self.sides[2]
		print('perimeter of triangle: ',self.perimeter)	

	def area(self):
		p = self.perimeter/2.0 
		self.area = math.sqrt(p*(p-self.sides[0])*(p-self.sides[1])*(p-self.sides[2])) 
		print('area of triangle: ', self.area)


class Quadrilateral(Polygon):
	#Quadrilateral is a rectangle
	#Input: width and height

	sides = []
	perimeter = 0
	area = 0
	
	def __init__(self, sides):
		self.sides = sides
		
	def perimeter(self):
		self.perimeter = 2*(self.sides[0] + self.sides[1])
		print('perimeter of rectangle: ', self.perimeter)
	
	def area(self):
		self.area = self.sides[0]*self.sides[1]
		print('area of rectangle: ', self.area)

class Pentagon(Polygon):
	sides = []

	def __init__(self, sides):
		self.sides = sides

	def perimeter(self):
		self.perimeter = 5 * self.sides[0]
		print('perimeter of pentagon: ', self.perimeter)

	def area(self):
		self.area = (math.sqrt(5*(5 + 2*math.sqrt(5))) * self.sides[0]**2)/4.0
		print('area of pentagon: ', self.area)

class Hexagon(Polygon):
	sides = []
	perimeter = 0
	area = 0


	def __init__(self, sides):
		self.sides = sides

	def perimeter(self):
		self.perimeter = 6 * self.sides[0]
		print('perimeter of hexagon: ', self.perimeter)

	def area(self):
		self.area = 3 * math.sqrt(3) * self.sides[0]**2 / 2.0
		print('area of hexagon: ', self.area)



tri = Triangle([3,4,5])
tri.perimeter()
tri.area()

rec = Quadrilateral([4,5])
rec.perimeter()
rec.area()

pen = Pentagon([5])
pen.perimeter()
pen.area()

hexa = Hexagon([6])
hexa.perimeter()
hexa.area()
