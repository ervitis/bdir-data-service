# -*- coding: utf-8 -*-


import logging


class DataLoadersError(Exception):
    __logger = logging.basicConfig()

    def __init__(self, message):
        self.message = message
        super(Exception, self).__init__(self.message)

    def __str__(self):
        self.__logger.log(msg=self.message, level=logging.ERROR)
        print(self.message)


class DataLoaderFileError(DataLoadersError):
    pass


class DataLoaderCSVReaderError(DataLoadersError):
    pass


class DataLoaderKeyError(DataLoadersError):
    pass
