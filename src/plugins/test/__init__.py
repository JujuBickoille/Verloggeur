# Sample plugin

Version='0.0.1'
Authors=['JujuBickoille <jujubickoille@free.fr>',]
Name='Hellow Wouorldeuh'
Description='Plugin a la con'

import test
import event

def enable(verloggeur):
	test.toto()
	event.add_callback(frite, "ping")

def disable(verloggeur):
	print "plugin disabled"
	print verloggeur

def frite(object, data):
	print object, data
	print 'TALAAAA'