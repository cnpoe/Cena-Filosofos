#Prueba.py

#MODULOS
import random
import sys,pygame
from pygame.locals import *
from array import array

#CONSTANTES
WIDTH = 900
HEIGHT = 506
CONTADOR_DE_MUERTE = 3
PALOS_ACTIVOS = 4
TIEMPO = 2000

class Pusheen(pygame.sprite.Sprite):
	def __init__(self, posX, posY):
		pygame.sprite.Sprite.__init__(self)
		self.image = load_image("pusheen.png",True)
		self.rect = self.image.get_rect()
		self.rect.centerx = posX
		self.rect.centery = posY

class PusheenComiendo(pygame.sprite.Sprite):
	def __init__(self, posX, posY):
		pygame.sprite.Sprite.__init__(self)
		self.image = load_image("pusheen_comiendo.png",True)
		self.rect = self.image.get_rect()
		self.rect.centerx = posX
		self.rect.centery = posY

class PusheenMuerto(pygame.sprite.Sprite):
	def __init__(self, posX, posY):
		pygame.sprite.Sprite.__init__(self)
		self.image = load_image("pusheen_muerto.png",True)
		self.rect = self.image.get_rect()
		self.rect.centerx = posX
		self.rect.centery = posY
		
class Palo(pygame.sprite.Sprite):
	def __init__(self, posX, posY):
		pygame.sprite.Sprite.__init__(self)
		self.image = load_image("palo.png",True)
		self.rect = self.image.get_rect()
		self.rect.centerx = posX
		self.rect.centery = posY
		
def load_image(filename,transparent = False):
	try: image = pygame.image.load(filename)
	except pygame.error, message:
		raise SystemExit, message
	image = image.convert()
	if transparent:
		color = image.get_at((0,0))
		image.set_colorkey(color,RLEACCEL)
	return image

def main():
	screen = pygame.display.set_mode((WIDTH,HEIGHT))
	pygame.display.set_caption("Cena")
	background_image = load_image('fondo.jpg')
	pushens = []
	palos = []
	pushensComiendo = []
	pushensMuertos = []
	muertos = [0,0,0,0,0,0]
	
	pushens.append(Pusheen(300, 100))
	pushens.append(Pusheen(600, 100))
	pushens.append(Pusheen(800, 253))
	pushens.append(Pusheen(600, 406))
	pushens.append(Pusheen(300, 406))
	pushens.append(Pusheen(100, 253))

	pushensComiendo.append(PusheenComiendo(300, 100))
	pushensComiendo.append(PusheenComiendo(600, 100))
	pushensComiendo.append(PusheenComiendo(800, 253))
	pushensComiendo.append(PusheenComiendo(600, 406))
	pushensComiendo.append(PusheenComiendo(300, 406))
	pushensComiendo.append(PusheenComiendo(100, 253))
	
	pushensMuertos.append(PusheenMuerto(300, 100))
	pushensMuertos.append(PusheenMuerto(600, 100))
	pushensMuertos.append(PusheenMuerto(800, 253))
	pushensMuertos.append(PusheenMuerto(600, 406))
	pushensMuertos.append(PusheenMuerto(300, 406))
	pushensMuertos.append(PusheenMuerto(100, 253))

	palos.append(Palo(450, 100))
	palos.append(Palo(750, 100))
	palos.append(Palo(750, 406))
	palos.append(Palo(450, 406))
	palos.append(Palo(150, 406))
	palos.append(Palo(150, 100))
	
	screen.blit(background_image,(0,0))
	
	iteracion = 1
	
	while True:
		terminar = 0
		for element in muertos:
			if element > CONTADOR_DE_MUERTE:
				terminar = terminar + 1 
				
		if terminar == 6:
			sys.exit()

		ocupados = []
		
		print "iteracion: " + str(iteracion)
		iteracion = iteracion + 1
		
		for eventos in pygame.event.get():
			if eventos.type == QUIT:
				sys.exit(0)
		screen.blit(background_image,(0,0))

		while (True):
			x = random.randint(0,5)
			if len(ocupados) == PALOS_ACTIVOS:
				break
			else:
				if not (x in ocupados):
					ocupados.append(x)
					x = random.randint(0,5)

		for x in ocupados:
			print x
		print '*'
		
		cuchara = [0,1,2,3,4,5]
		
		for i in range(6):
			x = i
			y = i-1
			if y == -1:
				y = 5
			print muertos
			if (x in ocupados) and (y in ocupados) and muertos[i] < CONTADOR_DE_MUERTE:
				screen.blit(pushensComiendo[i].image, pushensComiendo[i].rect)
				ocupados.remove(x)
				ocupados.remove(y)
				cuchara.remove(x)
				cuchara.remove(y)
				muertos[i] = 0
			elif muertos[i] < CONTADOR_DE_MUERTE:
				screen.blit(pushens[i].image, pushens[i].rect)
				muertos[i] = muertos[i] + 1
			else:
				screen.blit(pushensMuertos[i].image, pushensMuertos[i].rect)
				muertos[i] = muertos[i] + 1

		for i in range(6):
			if (i in cuchara):
				screen.blit(palos[i].image, palos[i].rect)

		pygame.display.flip()
		pygame.time.delay(TIEMPO)
	return 0

if __name__ == '__main__':
	pygame.init()
	main()
