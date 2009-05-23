#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Foundation import objc

class HaskellFuncItem(objc.lookUpClass('ESBaseItem')):
	"""Itemizer for functions"""
	pass

class HaskellCodeBlockItem(objc.lookUpClass('ESCodeBlockItem')):
	"""Itemizer for code blocks"""
	
	def isTextualizer(self):
		return True
	
	def title(self):
		return '%s %s' % (u'{…}', self.text())
		
	
