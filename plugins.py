#!/bin/env python

import os
from shutil import copy

pluginsKey = "SSO_PLUGINS"
pluginsVolume = "/opt/plugins"

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

def main():
    for plugin in getPlugins():
        copyIfExists(plugin)

main()
