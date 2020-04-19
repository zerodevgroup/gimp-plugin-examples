#!/usr/bin/env python

from gimpfu import *

def example_diagram(image, drawable):
    pdb.gimp_message("Example Diagram")

    # Add first box
    pdb.gimp_image_select_round_rectangle(image, 0, 200, 200, 350, 100, 50, 50)
    pdb.gimp_context_set_foreground( ("#0E0E52") ) # space cadet
    pdb.gimp_context_set_brush("1. Pixel")
    pdb.gimp_context_set_brush_size(4)
    pdb.gimp_context_set_stroke_method(1)
    pdb.gimp_edit_stroke(drawable)

    pdb.gimp_context_set_foreground( ("#000000") ) # black
    font = "Serif"
    text_layer = pdb.gimp_text_layer_new(image, "test", font, 40.0, 0)
    pdb.gimp_image_insert_layer(image, text_layer, None, 0)

    # select none
    pdb.gimp_selection_none(image)
    

register(
    "python_fu_example_diagram",
    "Example Diagram",
    "Example Diagram",
    "ZDG",
    "ZDG",
    "2020",
    "<Image>/File/Example Diagram",
    "RGB",
    [],
    [],
    example_diagram)

main()
