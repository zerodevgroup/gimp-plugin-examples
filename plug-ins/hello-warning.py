#!/usr/bin/env python

from gimpfu import *

def hello_warning(image, drawable):
    pdb.gimp_message("Hello, world!")
    

register(
    "python_fu_hello_warning",
    "Hello world warning",
    "Prints 'Hello, world!' to the error console",
    "ZDG",
    "ZDG",
    "2020",
    "<Image>/File/Hello Warning",
    "RGB",
    [],
    [],
    hello_warning)

main()
