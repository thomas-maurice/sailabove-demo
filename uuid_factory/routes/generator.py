#!/usr/bin/env python
# -*- coding: utf-8 -*-

import falcon
import socket
import uuid

class Uuid(object):
    def on_get(self, req, resp):
        """
        """
        req.context['result'] = {'uuid': str(uuid.uuid4()), 'hostname': socket.getfqdn()}
        return
