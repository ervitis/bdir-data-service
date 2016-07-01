# -*- coding: utf-8 -*-


import logging


class DataServiceError(Exception):
    __logger = logging.basicConfig()

    def __init__(self, message, *args, **kwargs):
        self.message = message
        super(Exception, self).__init__(self.message, args, kwargs)


class DataLoadersError(DataServiceError):
    pass


class DataLoaderFileError(DataLoadersError):
    pass


class DataLoaderCSVReaderError(DataLoadersError):
    pass


class DataLoaderKeyError(DataLoadersError):
    pass


class DataSaveServiceError(DataServiceError):
    pass


class DataSaveServiceWrongArgumentsError(DataSaveServiceError):
    pass
