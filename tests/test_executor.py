# -*- coding: utf-8 -*-

import unittest

from bds.executor import DataServiceExecutor


class TestExecutor(unittest.TestCase):

    def setUp(self):
        self.executor = DataServiceExecutor()

    def tearDown(self):
        pass

    def test_instance(self):
        self.assertIsNotNone(self.executor)

    def test_parameters(self):
        self.assertTrue(self.executor._arguments['delimiter'] == ';')
        self.assertTrue(self.executor._arguments['collection'] == 'transfers')


if __name__ == '__main__':
    unittest.main(verbosity=2)
