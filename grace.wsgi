#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/grace/")
sys.path.insert(0,"/var/www/grace/grace/")

import logging
logging.basicConfig(stream=sys.stderr)

from grace import app as application
