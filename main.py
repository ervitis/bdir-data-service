# -*- coding: utf-8 -*-

from bds.argparser import DataServiceArgumentParser
from bds.datasaveservice import DataSaveServiceMongo
from bds.dataloaders import DataLoaderCSV
from bds.executor import DataServiceExecutor


ARGUMENTS = [
    {
        'short': '-d',
        'long': '--delimeter',
        'default': ';',
        'dest': 'delimeter'
    },
    {
        'short': '-m',
        'long': '--machine',
        'default': '127.0.0.1',
        'dest': 'host'
    },
    {
        'short': '-p',
        'long': '--port',
        'default': 27017,
        'dest': 'port'
    },
    {
        'short': '-c',
        'long': '--collection',
        'default': 'transfers',
        'dest': 'collection'
    },
    {
        'short': '-db',
        'long': '--database',
        'default': 'bdirdata',
        'dest': 'database'
    },
    {
        'short': '-f',
        'long': '--file',
        'dest': 'filename'
    }
]


def parser(argparser):
    for argument in ARGUMENTS:
        if 'default' in argument:
            argparser.parse_build(
                argument['short'], argument['long'],
                default=argument['default'], dest=argument['dest']
            )
        else:
            argparser.parse_build(argument['short'], argument['long'], dest=argument['dest'])
    return argparser


def converse_date_format(date, format_input='%d/%m/%Y', format_output='%Y%m%d'):
    from datetime import datetime

    date = datetime.strptime(date, format_input)
    return date.strftime(format_output)


def main():
    import sys
    argparser = DataServiceArgumentParser()
    argparser = parser(argparser).parser.parse_args(sys.argv[1:])

    service_loader = DataLoaderCSV(path_file=argparser.filename)
    service_mongo = DataSaveServiceMongo(host=argparser.host, port=int(argparser.port), database=argparser.database)

    executor = DataServiceExecutor(delimiter=argparser.delimeter, collection=argparser.collection)
    data = executor.load_data(service_loader)

    for d in data:
        d['fecha_operacion'] = converse_date_format(d['fecha_operacion'])
        d['fecha_valor'] = converse_date_format(d['fecha_valor'])
        executor.save_data_into_db(service_mongo, d)

    exit(0)


if __name__ == '__main__':
    main()
