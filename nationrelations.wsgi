#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/NationRelations/")

from NationRelations import app as application

#print("Flaskhello")
