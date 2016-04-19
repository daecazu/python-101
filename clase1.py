import math

class Punto:
	def mover(self,x,y):
		self.x = x
		self.y = y
	def reiniciar(self):
		self.mover(0,0)
	def calcular_distancia(self, otro_punto):
		return math.sqrt(
			(self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2)

p = Punto()
p1 = Punto()
p2 = Punto()
Punto.reiniciar(p1)
p2.mover(5,0)

print(p2.calcular_distancia(p1))