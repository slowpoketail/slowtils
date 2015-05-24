#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# slowtils - various python utilities by slowpoke
#
# Author: slowpoke <mail+git@slowpoke.io>
#
# This program is Free Software under the non-terms
# of the Anti-License. Do whatever the fuck you want.

"""A more convenient tuple imlementation for functional programming."""

from collections import Sequence


class functuple(Sequence):

    def __init__(self, it=tuple()):
        # XXX: don't do ^ this ^ in mutable data structures ever.
        self._storage = tuple(it)

    def __getitem__(self, index):
        try:
            i = int(index)
        except (TypeError, ValueError):
            raise TypeError(
                "indices must be integers, not {}".format(type(index)))
        l = len(self)
        if i >= l or i < -l:
            raise IndexError("index out of range")
        return self._storage[i]

    def __len__(self):
        return len(self._storage)
