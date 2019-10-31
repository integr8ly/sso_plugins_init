#!/bin/env python

import os
import cgi
import urllib.request
import random
import string
from shutil import copyfileobj
from distutils.dir_util import copy_tree
from distutils import log

extensionsKey = "KEYCLOAK_EXTENSIONS"
extensionsVolume = "/opt/extensions"
themesPath = "/opt/themes"

def randomFileName():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10)) + ".jar"

# Try to get the filename from the response headers and return
# a random name if that fails
def parseHeader(headers):
    header = headers["Content-Disposition"]
    if not header:
        return randomFileName()

    _, params = cgi.parse_header(header)
    return params["filename"]

# Download a single extension
def downloadExtension(url):
    print("downloading extension from " + url)
    response = urllib.request.urlopen(url)
    filename = extensionsVolume + "/" + parseHeader(response.info())
    outfile = open(filename, "wb")
    copyfileobj(response, outfile)

# Parse the environment variable and return a list of extensions
# to download
def getExtensions():
    result = list()
    if extensionsKey in os.environ and not (not os.environ[extensionsKey]):
        extensions = os.environ[extensionsKey].split(",")
        for extension in extensions:
            result.append(extension)
    return result

def copyThemes():
    copy_tree('./themes', themesPath, verbose=1)

def main():
    log.set_verbosity(log.INFO)
    log.set_threshold(log.INFO)

    # Handle extensions
    for extension in getExtensions():
        try:
            downloadExtension(extension)
        except Exception as e:
            print(e)

    copyThemes()

main()
