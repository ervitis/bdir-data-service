# -*- coding: utf-8 -*-

import os


def get_resource_path():
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'resources'
    )
