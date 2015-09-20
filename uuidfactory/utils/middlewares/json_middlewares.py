#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import falcon
import json

class JSONInput(object):
    def process_request(self, req, resp):
        if req.method in ['GET', 'HEAD', 'OPTIONS']:
            return
        if req.content_length in (None, 0):
            return

        body = req.stream.read()
        if not body:
            raise falcon.HTTPBadRequest('Empty request body',
                                        'A valid JSON document is required.')
        try:
            req.context['json'] = json.loads(body.decode('utf-8'))
        except (ValueError, UnicodeDecodeError) as exce:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Malformed JSON',
                                   'Could not decode the request body. The '
                                   'JSON was incorrect or not encoded as '
                                   'UTF-8.')

class JSONOutput(object):
    def process_response(self, req, resp, resource):
        if 'result' not in req.context:
            return

        resp.body = json.dumps({'status': int(resp.status.split(' ')[0]),
            'data': req.context['result']},
            sort_keys=True,
            indent=4, separators=(',', ': ')
        )

middlewares = [JSONInput(), JSONOutput()]
