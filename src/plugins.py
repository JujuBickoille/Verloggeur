# plugins.py
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
import imp
import os

logger = logging.getLogger(__name__)


class PluginsManager(object):
	def __init__(self, core):
		self.core = core
		self.loaded_plugins = {}
		
	def load_plugin(self, pluginname):
		logger.info("loading plugin %s"%(pluginname))
		
		fp, pathname, description = imp.find_module(pluginname)
		p = imp.load_module(pluginname, fp, pathname, description)
		self.loaded_plugins[pluginname] = p
		return p

	def enable_plugin(self, pluginname):
		plugin = self.load_plugin(pluginname)
		plugin.enable(self.core)

	def disable_plugin(self, pluginname):
		plugin = self.loaded_plugins[pluginname]
		del self.loaded_plugins[pluginname]
		plugin.disable(self.core)
		logger.debug("Unloaded plugin %s" % pluginname)

		