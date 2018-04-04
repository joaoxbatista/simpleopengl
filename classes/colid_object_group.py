#-*- coding: utf-8 -*-

from colid_object import ColidObject

class ColidObjectGroup(object):

	colid_objects = []

	def __init__ (self, colid_objects):
		self.colid_objects = colid_objects

	def addColidObjects(self, colid_object):
		self.colid_objects.push(colid_object)

	def very_collid_objects(self, object, key):
		for obj in self.colid_objects:
			if(object.colid(obj, key)):
				return True
		return False

