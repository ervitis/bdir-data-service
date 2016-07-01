# -*- coding: utf-8 -*-


import logging


class DataLoadersError(Exception):
    __logger = logging.basicConfig()

    def __init__(self, message, *args, **kwargs):
        self.message = message
        super(Exception, self).__init__(self.message, args, kwargs)


class DataLoaderFileError(DataLoadersError):
    pass


class DataLoaderCSVReaderError(DataLoadersError):
    pass


class DataLoaderKeyError(DataLoadersError):
    pass


class DataSaveServiceWrongArgumentsError(DataLoadersError):
    pass
