#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# slowtils - various python utilities by slowpoke
#
# Author: slowpoke <mail+git@slowpoke.io>
#
# This program is Free Software under the non-terms
# of the Anti-License. Do whatever the fuck you want.

from collections.abc import Sequence

"""An immutable list implementation."""


class funclist(Sequence):

    """Immutable list for pure functional programming.

    This works basically like a regular list, but doesn't mutate its state. All
    methods on instances of this class which would mutate the state of a normal
    regular list return a new instance with the applied changes instead.

    """

    def __init__(self, it=tuple()):
        self._storage = tuple(it)

    def __getitem__(self, index):
        return self._storage[index]

    def __len__(self):
        return len(self._storage)

    def __repr__(self):
        return "[{}]".format(
            ", ".join([repr(x) for x in self]))

    def append(self, x):
        return self.extend((x,))

    def extend(self, it):
        def iter():
            for x in self._storage:
                yield x
            for x in it:
                yield x
        return funclist(iter())

    def insert(self, i, x):
        def iter():
            for y in self[:i]:
                yield y
            yield x
            for y in self[i:]:
                yield y
        return funclist(iter())

    def remove(self, value):
        i = self.index(value)
        def iter():
            for x in self[:i]:
                yield x
            for x in self[i+1:]:
                yield x
        return funclist(iter())
