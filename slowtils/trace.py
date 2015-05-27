#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# slowtils - various python utilities by slowpoke
#
# Author: slowpoke <mail+git@slowpoke.io>
#
# This program is Free Software under the non-terms
# of the Anti-License. Do whatever the fuck you want.

"""Simple tracing tools for Serious Printf Debugging™."""

import time

def trace(f):
    fname = f.__name__
    def new_f(*args, **kwargs):
        print("CALL   [{}] {}({})".format(
            make_timestamp(),
            fname,
            ", ".join(repr(arg) for arg in args)))
        ret = f(*args)
        print("RETURN [{}] {}() → {}".format(
            make_timestamp(), fname, ret))
        return ret
    return new_f

def make_timestamp():
    return time.strftime("%H:%M:%S", time.localtime())
