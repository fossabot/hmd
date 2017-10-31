#!/usr/bin/env python

from setuptools import setup

from hmdc.__init__ import *

setup(
           name = __program__,
        version = __version__,
    description = "hmdc is the next-generation Hierarchial Multiple Dictionary (HMD) compiler.",
        license = __license__,
         author = "Herbert Shin",
            url = "https://github.com/initbar/hmdc",
       zip_safe = True
)
