slowtils
========

Overview
--------
This is just a growing collection of reusable code that I find myself using very
often, but which don't compromise enough functionality on their own to warrant a
library for themselves. As such, I have decided to put them together as one
package so I (and maybe others) can easily reuse this code in the future.

Components
----------

Note that the API is designed so that you can 

    from slowtils import MODULE

and use the module name as the namespace. It's NOT recommended to do * imports
from them because some of the functions and classes *will* override definitions
in the standard namespace.

slowtils.file
^^^^^^^^^^^^^

A module of file-related utilities, among them handy wrapper functions for
easily checking file existence, reading file contents, or hashing contents.

slowtils.func
^^^^^^^^^^^^^

Some tools for functional programming. Currently only contains immutable
alternatives to standard Python data structures.
