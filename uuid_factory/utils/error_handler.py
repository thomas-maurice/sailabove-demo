#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import falcon
import json
import traceback

def error_handler(exce, req, resp, params):
    if isinstance(exce, falcon.HTTPError):
        resp.status = exce.status
        req.context['result'] = {'error': "%s: %s" % (exce.title, exce.description)}
    else:
        print traceback.print_exc()
        resp.status = falcon.HTTP_500
        req.context['result'] = {'error': str(traceback.format_exc())}
