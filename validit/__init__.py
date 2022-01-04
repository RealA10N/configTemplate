from .schema import Schema

from .string import String
from .boolean import Boolean
from .number import Number, Integer

from .dictionary import Dictionary
from .union import Union, Optional

__all__ = [
    # base
    'Schema',

    # primitive
    'String',
    'Boolean',
    'Number',
    'Integer',

    # nested
    'Dictionary',
    'Optional',
    'Union',
]

__version__ = '2.0.0-dev'
__author__ = 'Alon Krymgand Osovsky'
