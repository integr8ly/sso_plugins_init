#!/bin/env python

import os
from shutil import copy
from distutils.dir_util import copy_tree
from distutils import log

pluginsKey = "SSO_PLUGINS"
pluginsVolume = "/opt/plugins"
themesPath = "/opt/themes"

def getPlugins():
    if "SSO_PLUGINS" in os.environ:
        return os.environ[pluginsKey].split(",")
    else:
        return []

def copyIfExists(plugin):
    pluginPath = './' + plugin + '.jar'
    if os.path.isfile(pluginPath):
        print("Copying plugin: " + plugin)
        copy(pluginPath, pluginsVolume)

def copyThemes():
    log.set_verbosity(log.INFO)
    log.set_threshold(log.INFO)
    copy_tree('./themes', themesPath, verbose=1)

def main():
    for plugin in getPlugins():
        copyIfExists(plugin)
    copyThemes()

main()
