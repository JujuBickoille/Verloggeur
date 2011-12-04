# irc.py
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




import threading, socket
import logging
import re

import event

logger = logging.getLogger(__name__)

linesep = re.compile('\r?\n') # thanks to irclib :]
ping = re.compile('^(:(?P<prefix>[^ ]+) +)?PING :(?P<ping>.+)$')

class MessageManager(object):
	def __init__ (self, message):
		pass

class Irc(threading.Thread):
	def __init__(self, host, port, ssl, ipv6):
		threading.Thread.__init__(self)
		self.host = host
		self.port = port
		self.ssl = ssl
		self.ipv6 = ipv6
		
		logger.info("New IRC Instance : %s:%d ssl=%d ipv6=%d"%(host, port, ssl, ipv6))

	def connect(self):
		for res in socket.getaddrinfo(self.host, self.port, socket.AF_INET, socket.SOCK_STREAM):
			af, socktype, proto, cannonname, sa = res
		self._socket= socket.socket(af, socktype, proto)
		if self.ssl:
			import ssl
			ssl.wrap_socket(self._socket)
		self._socket.connect(sa)
		self.start()
		import time
		time.sleep(3)
		self.sendraw("USER juju juju ujuj ujuj ju uj :uj ujujjuujuj\r\n")
		self.sendraw("NICK :JeanNick\r\n")

	def sendraw(self, message):
		if not message.endswith('\r\n'):
			message = message + '\r\n'
		logger.debug("send %s"%(message))
		if self.ssl:
			self._socket.write(message)
		else:
			self._socket.send(message)

	def disconnect(self, quit_message="Bye!\r\n"):
		self._socket.send("QUIT :%s"%(quit_message))

	def run(self):
		prevmsg = str()
		while(1):
			d = self._socket.recv(32)
			line = linesep.split(prevmsg + d)
			prevmsg = line.pop()
			for msg in line:
				if not msg:
					continue
				#logger.debug("receive %s"%msg)
				if ping.match(msg):
					self._socket.send("PONG :%s\r\n"%(ping.match(msg).group('ping')))
					event.log_event ("ping", self._socket, ping.match(msg).group('ping'))
			
			if d == "":
				self._socket.close ()
				break