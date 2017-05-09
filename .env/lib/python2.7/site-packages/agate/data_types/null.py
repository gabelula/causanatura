#!/usr/bin/env python

import six

from agate.data_types.base import DataType
from agate.exceptions import CastError


class Null(DataType):
    """
    Data representing null.

    :param cast_nulls:
        If :code:`True`, values in :data:`.DEFAULT_NULL_VALUES` will also be
        treated as null.
    """
    def __init__(self, cast_nulls=True, **kwargs):
        super(Null, self).__init__(**kwargs)

        self.cast_nulls = cast_nulls

    def cast(self, d):
        """
        Cast a single value to :code:`None`.

        :param d:
            A value to cast.
        :returns:
            :code:`None`
        """
        if d is None:
            return d

        if self.cast_nulls and isinstance(d, six.string_types):
            if d.strip().lower() in self.null_values:
                return None

        raise CastError('Can not parse value "%s" as Null.' % d)
