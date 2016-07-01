# -*- coding: utf-8 -*-


import logging

from pymongo import MongoClient

from . import exceptions


class DataSaveServiceInterface(object):

    def _connect(self, *args, **kwargs):
        raise NotImplementedError

    def save_data(self, *args, **kwargs):
        raise NotImplementedError

    def __exit__(self, exc_type, exc_val, exc_tb):
        if hasattr(self, '__logger'):
            self.__logger.shutdown()


class DataSaveServiceMongo(DataSaveServiceInterface):
    __logger = logging.basicConfig()
    __arguments = ['host', 'port', 'database']

    def __init__(self, **kwargs):
        self._connector = self._connect(**kwargs)
        self._enable_log = kwargs['enable_log'] if 'enable_log' in kwargs else False

    def save_data(self, collection, data):
        assert isinstance(data, dict)

        self._connector[collection].insert_one(data)

    def delete_data(self, collection, data):
        assert isinstance(data, dict)

        return self._connector[collection].delete_one(data).deleted_count

    def delete_all(self, collection):
        return self._connector[collection].delete_many({}).deleted_count

    def _connect(self, **kwargs):
        self._check_args(**kwargs)

        return MongoClient(host=kwargs['host'], port=kwargs['port'])[kwargs['database']]

    def _check_args(self, **kwargs):
        if not kwargs or len(kwargs) != len(self.__arguments):
            raise exceptions.DataSaveServiceWrongArgumentsError(
                'You have to pass the {} arguments'.format(', '.join(self.__arguments))
            )

        for argument in kwargs:
            if argument not in self.__arguments:
                raise exceptions.DataSaveServiceWrongArgumentsError('{} wrong argument'.format(argument))
