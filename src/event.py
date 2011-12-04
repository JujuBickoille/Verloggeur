# event.py
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






class EventManager(object):
	def __init__(self):
		self.callbacks = {}
		
	def emit(self, type, obj, data):
		print 'emit launched %s %s %s'%(type, obj, data)
		if self.callbacks.has_key(type):
			self.callbacks[type][0].__call__ (obj, data)
	def add_callback(self, function, type, obj, args, kwargs):
		self.callbacks[type] = (function, obj, args, kwargs)
		
	def remove_callback(self, function, type=None, obj=None):
		pass

EVENT_MANAGER = EventManager()


def add_callback(function, type=None, obj=None, *args, **kwargs):
	print 'add Callback : function=%s, type=%s, obj=%s, args=%s, kwargs=%s'%(function, type, obj, args, kwargs)
	EVENT_MANAGER.add_callback(function, type, obj, args, kwargs)

def log_event(type, obj, data):
	print 'log_event type=%s, obj=%s, data=%s'%(type, obj, data)
	EVENT_MANAGER.emit (type, obj, data)