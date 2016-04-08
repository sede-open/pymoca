#!/usr/bin/env python
"""
Modelica parse Tree to AST tree.
"""
from __future__ import print_function, absolute_import, division, print_function, unicode_literals

import os
import sys
import unittest
import time

from pymola import parser
from pymola import tree

TEST_DIR = os.path.dirname(os.path.realpath(__file__))

class ParseTest(unittest.TestCase):
    "Testing"

    def setUp(self):
        sys.stdout.flush()
        sys.stderr.flush()

    def tearDown(self):
        sys.stdout.flush()
        sys.stderr.flush()

    def test_aircraft(self):
        sys.stdout.flush()
        sys.stderr.flush()
        with open(os.path.join(TEST_DIR, './Aircraft.mo'), 'r') as f:
            txt = f.read()
        ast_tree = parser.parse(txt)
        flat_tree = tree.flatten(ast_tree, 'Aircraft')
        sys.stdout.flush()
        sys.stderr.flush()

    def test_bouncing_ball(self):
        sys.stdout.flush()
        sys.stderr.flush()
        with open(os.path.join(TEST_DIR, './BouncingBall.mo'), 'r') as f:
            txt = f.read()
        ast_tree = parser.parse(txt)
        flat_tree = tree.flatten(ast_tree, 'BouncingBall')
        sys.stdout.flush()
        sys.stderr.flush()

    def test_estimator(self):
        sys.stdout.flush()
        sys.stderr.flush()
        with open(os.path.join(TEST_DIR, './Estimator.mo'), 'r') as f:
            txt = f.read()
        ast_tree = parser.parse(txt)
        flat_tree = tree.flatten(ast_tree, 'Estimator')
        sys.stdout.flush()
        sys.stderr.flush()

    def test_spring(self):
        sys.stdout.flush()
        sys.stderr.flush()
        with open(os.path.join(TEST_DIR, './Spring.mo'), 'r') as f:
            txt = f.read()
        ast_tree = parser.parse(txt)
        flat_tree = tree.flatten(ast_tree, 'Spring')
        sys.stdout.flush()
        sys.stderr.flush()


if __name__ == "__main__":
    unittest.main()
