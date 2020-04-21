#!/usr/bin/env python

from gimpfu import *

def example_diagram(image, drawable):
    pdb.gimp_message("Example Diagram")

    x = 200
    y = 200
    width = 350
    height = 100
    corner_radius_x = 50.0
    corner_radius_y = 50.0
    color = "#0E0E52" # space cadet
    brush = "1. Pixel"
    brush_size = 4

    pdb.gimp_message("Good so far...")

    # Add first box
    pdb.gimp_image_select_round_rectangle(image, CHANNEL_OP_ADD, x, y, width, height, corner_radius_x, corner_radius_y)
    pdb.gimp_context_set_foreground(color)
    pdb.gimp_context_set_brush(brush)
    pdb.gimp_context_set_brush_size(brush_size)
    pdb.gimp_context_set_stroke_method(STROKE_PAINT_METHOD)
    pdb.gimp_edit_stroke(drawable)

    color = "#000000" # black
    pdb.gimp_context_set_foreground(color)


    text = "Test"
    border = 0
    antialias = True
    size = 40.0
    size_type = PIXELS
    fontname = "Verdana"

    text_width, text_height, text_ascent, text_descent = pdb.gimp_text_get_extents_fontname(text, size, size_type, fontname)

    x = x + ( ( width / 2 ) - ( text_width / 2 ) )
    y = y + ( ( height / 2 ) - ( text_height / 2 ) )

    text_layer = pdb.gimp_text_fontname(image, None, x, y, text, border, antialias, size, size_type, fontname)

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
    "*",
    [],
    [],
    example_diagram)

main()
