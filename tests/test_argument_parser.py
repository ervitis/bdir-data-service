# -*- coding: utf-8 -*-

import unittest

from bds.argparser import DataServiceArgumentParser


class TestArgumentParser(unittest.TestCase):

    def tearDown(self):
        pass

    def setUp(self):
        self.argparser = DataServiceArgumentParser()
        self.arguments = {
            'short': '',
            'long': ''
        }

    def test_instance(self):
        self.assertIsNotNone(self.argparser)

    def test_parser(self):
        self.arguments['short'] = '-c'
        self.arguments['long'] = '--collection'
        self.argparser.parse_build(self.arguments)

        self.assertTrue(self.argparser.parser.parse_args(['-c', 'collection']))
        self.assertTrue(self.argparser.parser.parse_args(['--collection', 'test']))

    def test_option_delimeter(self):
        self.arguments['short'] = '-d'
        self.arguments['long'] = '--delimeter'
        self.arguments['dest'] = 'delimeter'
        self.argparser.parse_build(argument=self.arguments, dest=self.arguments['dest'])

        args = self.argparser.parser.parse_args(['-d', ';'])
        self.assertIsNotNone(args.delimeter)
        self.assertTrue(args.delimeter == ';')


if __name__ == '__main__':
    unittest.main(verbosity=2)
