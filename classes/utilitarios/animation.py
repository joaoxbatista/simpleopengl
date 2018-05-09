# -*- coding: utf-8 -*-

class Animation(object):

	
	mutations = []
	frames = 0
	count = 0
	flag = True

	def __init__(self, name, mutations):
		self.mutations = mutations
		self.count = 1
		self.flag = True

	def animate(self):

		result = self.count * self.mutations['radius']

		if(result >= self.mutations['limit'] and self.flag):
			self.flag = False

		if(not self.flag and result <= 0):
			self.flag = True

		if(self.flag):
			self.count += 1
		else: 
			self.count -= 1		


		return result

