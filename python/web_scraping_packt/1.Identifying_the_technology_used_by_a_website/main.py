# -*- coding: utf-8 -*-
import builtwith

tecnologias =  builtwith.parse('http://vamoaprogramar.com/blog')
print tecnologias
for key, value in tecnologias.iteritems():
	print key ,": " , value

