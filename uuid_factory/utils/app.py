#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import falcon
import json

from middlewares import middlewares
from error_handler import error_handler

app = falcon.API(middleware=middlewares)
app.add_error_handler(Exception, error_handler)
app.add_error_handler(falcon.HTTPError, error_handler)
