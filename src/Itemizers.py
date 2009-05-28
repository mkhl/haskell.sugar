#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Foundation import objc
from Foundation import NSBundle
from AppKit import NSImage

haskellBundleIdentifier = 'org.purl.net.mkhl.haskell'

def iconForName(name):
	"""Return the NSImage instance representing a `name` item."""
	bundle = NSBundle.bundleWithIdentifier_(haskellBundleIdentifier)
	imgpath = bundle.pathForResource_ofType_(name, 'png')
	img = NSImage.alloc().initWithContentsOfFile_(imgpath)
	img.autorelease()
	return img

class HaskellModuleItem(objc.lookUpClass('ESBaseItem')):
	"""Itemizer for modules"""
	
	def isDecorator(self):
		return True
	
	def image(self):
		return iconForName('module')
	

class HaskellTypeItem(objc.lookUpClass('ESBaseItem')):
	"""Itemizer for datatypes"""
	
	def isDecorator(self):
		return True
	
	def image(self):
		return iconForName('type')
	
	def isTextualizer(self):
		return True
	
	def title(self):
		return self.text().lstrip()
	

class HaskellFunctionItem(objc.lookUpClass('ESBaseItem')):
	"""Itemizer for functions"""
	pass

class HaskellCodeBlockItem(objc.lookUpClass('ESCodeBlockItem')):
	"""Itemizer for code blocks"""
	
	def isTextualizer(self):
		return True
	
	def title(self):
		return '%s %s' % (u'{…}', self.text().lstrip())
		
	
