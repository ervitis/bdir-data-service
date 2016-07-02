# -*- coding: utf-8 -*-

from argparse import ArgumentParser


class DataServiceArgumentParser(object):

    def __init__(self):
        self._parser = ArgumentParser()

    def parse_build(self, short, long, **kwargs):
        self._parser.add_argument(short, long, **kwargs)

        return self

    @property
    def parser(self):
        return self._parser
