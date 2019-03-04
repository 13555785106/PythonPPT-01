#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import logging
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chapter19.settings")
django.setup()

logger = logging.getLogger()
logger.error("ADASD")
