# -*- coding: utf-8 -*-

import unittest
import os

from bds.dataloaders import DataLoaderCSV
from bds import exceptions
from .utils import get_resource_path


class TestLoadDataFile(unittest.TestCase):

    def setUp(self):
        self._test_path_bad = os.path.join(
            get_resource_path(),
            'this_file_does_not_exist.txt'
        )
        self._test_path = os.path.join(
            get_resource_path(),
            'csv_file1.csv'
        )
        self.data_loader_csv = DataLoaderCSV(self._test_path_bad)

    def tearDown(self):
        pass

    def test_instance(self):
        self.assertIsNotNone(self.data_loader_csv)

    def test_load_data_from_file_raise_exception_file_not_exists(self):
        self.assertRaises(exceptions.DataLoaderFileError, self.data_loader_csv._check_file_exists)

    def test_load_data_from_file(self):
        self.data_loader_csv = DataLoaderCSV(self._test_path)

        try:
            self.data_loader_csv.load_data_file()
        except Exception as e:
            self.fail(e)

    def test_data_as_dict(self):
        self.data_loader_csv = DataLoaderCSV(self._test_path)

        for data in self.data_loader_csv.load_data_file():
            self.assertTrue(isinstance(data, dict))

if __name__ == '__main__':
    unittest.main()
