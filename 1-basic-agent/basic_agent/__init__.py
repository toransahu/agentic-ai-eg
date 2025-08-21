#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# created_on: 2025-08-21 09:34

"""Init.

This is important to expose the agent module. Otherwise it throws:

AttributeError: module 'basic_agent' has no attribute 'agent'
"""

from basic_agent import agent


__author__ = "Toran Sahu <toran.sahu@yahoo.com>"
__license__ = "Distributed under terms of the MIT license"
