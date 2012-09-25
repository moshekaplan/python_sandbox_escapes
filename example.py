#!/usr/bin/env python
"""
There are many different ways users can attempt to restrict what can be done
inside of a Python script.

This file describes a few approaches to sandboxing, and shows why they are flawed.
"""

###############################################################################
# Methods based on searching for import:

# Searching for the import keyword - we can use __import__()

# If you already have access to sys:
sys.modules['__builtin__'].__import__('evil_foo') 

# If you have access to one of the python-based modules, say os:
os.__builtins__['__import__']('evil_foo')

# Searching for the word 'import' in any context - use ROT13 encoding
# See http://www.python.org/dev/peps/pep-0263/ for more detail

# coding: rot_13
# "import evil_foo" encoded in ROT13
vzcbeg rivy_sbb

