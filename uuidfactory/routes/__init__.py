#!/usr/bin/env python
# -*- coding: utf-8 -*-

import generator

from utils import app

app.add_route('/', generator.Uuid())
