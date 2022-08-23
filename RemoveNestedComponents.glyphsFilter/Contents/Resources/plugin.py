# encoding: utf-8

###########################################################################################################
#
#
#	Filter without dialog plug-in
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Filter%20without%20Dialog
#
#
###########################################################################################################

from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *


class RemoveNestedComponents(FilterWithoutDialog):
	
	@objc.python_method
	def settings(self):
		self.menuName = Glyphs.localize({
			"en": "Remove Nested Components",
			"de": "Verschachtelte Komponenten entfernen",
			"es": "Eliminar componentes anidados",
			"fr": "Supprimer les composants imbriqués",
			"ja": "ネストされたコンポーネントを削除",
			"ko": "중첩된 구성요소 제거",
			"zh": "移除嵌套组件"
			})

	@objc.python_method
	def filter(self, layer, inEditView, customParameters):

		if not layer.components:
			return
		nested_components = True
		while nested_components:
			for component in layer.components:
				ref_layer = component.component.layers[0]
				if len(ref_layer.components):
					for other_component in layer.components:
						other_component.automaticAlignment = False
					component.decompose()
					nested_components = True
				else:
					nested_components = False

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
