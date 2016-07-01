# -*- coding: utf-8 -*-


import unittest

from bds.datasaveservice import DataSaveServiceMongo
from bds import exceptions


class TestSaveData(unittest.TestCase):

    def setUp(self):
        self.mongodb = DataSaveServiceMongo(host='127.0.0.1', port=27017, database='bdirdata')
        self.test_data = {
            'test_id': 1,
            'name': 'try'
        }
        self.collection = 'testcollection'

    def tearDown(self):
        self.mongodb.delete_all(self.collection)

    def test_instance(self):
        self.assertIsNotNone(self.mongodb)

    def test_save_data(self):
        self.mongodb.save_data(self.collection, self.test_data)

    def test_check_arguments_connection(self):
        with self.assertRaises(exceptions.DataSaveServiceWrongArgumentsError):
            self.mongodb._check_args()

    def test_check_arguments_connection_wrong_arguments(self):
        with self.assertRaises(exceptions.DataSaveServiceWrongArgumentsError):
            arguments = {
                'hello': 'hello'
            }
            self.mongodb._check_args(**arguments)

    def test_check_arguments_connection_few_arguments(self):
        with self.assertRaises(exceptions.DataSaveServiceWrongArgumentsError):
            arguments = {
                'port': 12345,
                'database': 'hello'
            }
            self.mongodb._check_args(**arguments)

    def test_delete_data(self):
        self.mongodb.save_data(self.collection, self.test_data)

        self.assertTrue(self.mongodb.delete_data(self.collection, self.test_data) == 1)

    def test_delete_all_data(self):
        self.mongodb.save_data(self.collection, self.test_data)

        self.test_data = {
            'test_id': 2,
            'name': 'anothertest'
        }
        self.mongodb.save_data(self.collection, self.test_data)

        self.assertTrue(self.mongodb.delete_all(self.collection) == 2)

    def test_data_service_raise_error(self):
        with self.assertRaises(exceptions.DataSaveServiceError):
            self.mongodb.save_data(self.collection, self.test_data)
            self.mongodb.save_data(self.collection, self.test_data)


if __name__ == '__main__':
    unittest.main(verbosity=2)
