import time

import numpy as np

from Pygame_GUI.Objects import *
from Pygame_GUI.Screen import Screen



class MapSprite(Sprite):
	def __init__(self, par_surf, /, width=0, height=0, **kwargs):
        	super().__init__(par_surf, **kwargs)
        	self.rect = pg.Rect(0,0, width, height)
        	self.color = (255,255,255)
        	self.robot = PhisicsObject((200, 0), (1.5, 0), 1)
        	self.objects = []
        	self.K = 20
        	
	def add_obj(self, pos, vel, potentioal):
		self.objects.append(PhisicsObject(pos, vel, potentioal))
        	
        	
	def update(self):
		for obj in self.objects:
			dist_vect = self.robot.pos-obj.pos
			dist = np.linalg.norm(dist_vect)
			print(dist)
			force = self.robot.potential*obj.potential/(dist**3)*dist_vect
			print("force", force)
			self.robot.vel += force * self.K
		self.robot.pos = self.robot.pos + self.robot.vel
        
	def draw(self):
         	pg.draw.rect(self.surface, self.color, self.rect)
         	
         	for obj in self.objects:
         		if obj.potential > 0:
         			color = (0, 0, 255)
         		else:
         			color = (0, 255, 0)
         		pg.draw.circle(self.surface, color, obj.pos.astype(int), abs(obj.potential))
         	pg.draw.circle(self.surface, (255,0, 0), self.robot.pos.astype(int), 20)
         	
class PhisicsObject():
	def __init__(self, pos, vel, potential):
		self.vel = vel
		self.potential = potential
		self.pos = np.array(pos)
		
        	
        

width=500
height=500	
screen = Screen(width, height)
screen.init()
running = True
Map = screen.sprite(MapSprite, "map", width=width, height=height)
#Map.add_obj((300, 300), 0, 30)
Map.add_obj((300, 300), 0, -80)
while screen.running:
	screen.step()
	
	
	
	
	
	
	
	
