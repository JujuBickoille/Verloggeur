#!/usr/bin/python
#
# verloggeur.py
# Copyright (C) JujuBickoille 2011 <jujubickoille@free.fr>
# 
# Verloggeur is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Verloggeur is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.


import logging
import plugins
import event
import irc

__version__ = "0.1.0"

class Verloggeur(object):
	def __init__(self):
		print self.ascii_art()
		
		self.start_loging()
		self.logger.info("Loading Verloggeur ...")
		self.start_plugins ()

		serv = irc.Irc("127.0.0.1", 6667, False, False)
		#serv2 = irc.Irc("irc.freenode.net", 6667, False, False)
		#serv3 = irc.Irc("irc.quakenet.org", 6667, False, False)
		serv.connect()
		#serv3.connect()
		#serv2.connect()
		#serv.start ()
		import time
		time.sleep(15)
		serv.disconnect()
		#serv2.disconnect()
		#serv3.disconnect()

	def start_loging(self):
		logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s: %(message)s", datefmt="%D %H:%M:%S")
		self.logger = logging.getLogger("Core")

	def start_plugins(self):
		self.logger.info("Loading plugins...")
		self.plugins = plugins.PluginsManager(self)
	#	self.plugins.load_plugin ("plugins/test")
		self.plugins.enable_plugin ("plugins/test")
	#	self.plugins.disable_plugin ("plugins/test")
	#	self.plugins.enable_plugin ("plugins/test")
		
		


	def ascii_art(self):
		"""That's the most important verloggeur's function:
			Return :"Verloggeur" in ascii-art"""
		return \
"""
#############################################################
#   _    _           _                                      #
#  | |  | |         | |                                     #
#  | |  | |___  ____| | ___   ____  ____  ____ _   _  ____  #
#   \ \/ / _  )/ ___) |/ _ \ / _  |/ _  |/ _  ) | | |/ ___) #
#    \  ( (/ /| |   | | |_| ( ( | ( ( | ( (/ /| |_| | |     #
#     \/ \____)_|   |_|\___/ \_|| |\_|| |\____)\____|_|     #
#                           (_____(_____|                   #
#                                            Version %s  #
#############################################################\n"""%(__version__)

if __name__ == "__main__":
	verloggeur = Verloggeur()