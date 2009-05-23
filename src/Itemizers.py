#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Foundation import objc
from Foundation import NSBundle
from AppKit import NSImage

def iconForName(klass, name):
	"""Return the NSImage instance representing a `name` item."""
	imgpath = NSBundle.bundleForClass_(klass).pathForResource_ofType_(name, 'png')
	img = NSImage.alloc().initWithContentsOfFile_(imgpath)
	img.autorelease()
	return img

class HaskellModuleItem(objc.lookUpClass('ESBaseItem')):
	"""Itemizer for modules"""
	
	def isDecorator(self):
		return True
	
	def image(self):
		return iconForName(self.class__(), 'module')
	

class HaskellTypeItem(objc.lookUpClass('ESBaseItem')):
	"""Itemizer for datatypes"""
	
	def isDecorator(self):
		return True
	
	def image(self):
		return iconForName(self.class__(), 'type')
	
	def isTextualizer(self):
		return True
	
	def title(self):
		return self.text().strip()
	

class HaskellFunctionItem(objc.lookUpClass('ESBaseItem')):
	"""Itemizer for functions"""
	pass

class HaskellCodeBlockItem(objc.lookUpClass('ESCodeBlockItem')):
	"""Itemizer for code blocks"""
	
	def isTextualizer(self):
		return True
	
	def title(self):
		return '%s %s' % (u'{…}', self.text().strip())
		
	
