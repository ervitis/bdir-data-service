# -*- coding: utf-8 -*-

import csv
import os
import logging

from . import exceptions


class DataLoaderInterface(object):

    def load_data_file(self, *args, **kwargs):
        raise NotImplementedError

    def __exit__(self, exc_type, exc_val, exc_tb):
        if hasattr(self, '__logger'):
            self.__logger.shutdown()


class DataLoaderCSV(DataLoaderInterface):
    __logger = logging.basicConfig()

    def __init__(self, path_file, **kwargs):
        self.data = None
        self._path_file = path_file
        self._enable_log = kwargs['enable_log'] if 'enable_log' in kwargs else False

    def load_data_file(self, delimiter=';'):
        self._check_file_exists()

        with open(self._path_file, 'r') as csv_file:
            try:
                self.data = csv.DictReader(csv_file, delimiter=delimiter)
            except csv.Error as e:
                raise exceptions.DataLoaderCSVReaderError('CSV Reader error: {}'.format(e))

            for row in self.data:
                try:
                    yield {
                        key: value for key, value in row.items()
                    }
                except KeyError as e:
                    raise exceptions.DataLoaderKeyError('CSV Key Error: {}'.format(e))

    def _check_file_exists(self):
        if not os.path.exists(self._path_file):
            raise exceptions.DataLoaderFileError('File {} not found'.format(self._path_file))
