# -*- coding: utf-8 -*-


class DataServiceExecutor(object):

    def __init__(self, **kwargs):
        self._arguments = {
            'delimiter': kwargs['delimiter'] if 'delimiter' in kwargs else ';',
            'collection': kwargs['collection'] if 'collection' in kwargs else 'transfers'
        }

    def load_data(self, service):
        return service.load_data_file(delimiter=self._arguments['delimiter'])

    def save_data_into_db(self, service, data):
        service.save_data(self._arguments['collection'], data)
