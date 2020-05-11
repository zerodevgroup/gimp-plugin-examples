#!/usr/bin/env python

from gimpfu import *

def example_diagram(image, drawable):
    pdb.gimp_message("Example Diagram")

    box(image, drawable, 750, 100, "#0E0E52")
    box(image, drawable, 750, 300, "#150578")
    box(image, drawable, 750, 500, "#192BC2")
    box(image, drawable, 750, 700, "#449DD1")
    box(image, drawable, 750, 900, "#78C0E0")

    # line(image, drawable, 100, 100, 200, 200, 4, "#000000")

    text(image, drawable, 750, 100, "Router", "#000000")
    text(image, drawable, 750, 300, "Controller", "#000000")
    text(image, drawable, 750, 500, "Service", "#000000")
    text(image, drawable, 750, 700, "Model", "#000000")
    text(image, drawable, 750, 900, "DAO", "#000000")

def box(image, drawable, x, y, box_outline_color):
    box_width = 550
    box_height = 100

    center_x = x - (box_width / 2)
    center_y = y
    corner_radius_x = 50.0
    corner_radius_y = 50.0
    brush = "1. Pixel"
    brush_size = 6

    # Add box
    pdb.gimp_image_select_round_rectangle(image, CHANNEL_OP_ADD, center_x, center_y, box_width, box_height, corner_radius_x, corner_radius_y)
    pdb.gimp_context_set_foreground(box_outline_color)
    pdb.gimp_context_set_brush(brush)
    pdb.gimp_context_set_brush_size(brush_size)
    pdb.gimp_context_set_stroke_method(STROKE_PAINT_METHOD)
    pdb.gimp_edit_stroke(drawable)

    # select none
    pdb.gimp_selection_none(image)

# def line(image, drawable, from_x, from_y, to_x, to_y, line_width, line_color):
    # pdb.gimp_context_set_foreground(line_color)

    # pdb.gimp_context_set_stroke_method(STROKE_LINE)
    # pdb.gimp_context_set_line_cap_style(CAP_SQUARE)
    # pdb.gimp_context_set_line_join_style(JOIN_MITER)
    # pdb.gimp_context_set_line_miter_limit(50)
    # pdb.gimp_context_set_line_width(line_width)
    # pdb.gimp_drawable_edit_stroke_item(drawable, path)

def text(image, drawable, x, y, text, text_color):
    box_width = 350
    box_height = 100

    center_x = x - (box_width / 2)
    center_y = y

    pdb.gimp_context_set_foreground(text_color)

    border = 0
    antialias = True
    size = 40.0
    size_type = PIXELS
    fontname = "Verdana"

    text_width, text_height, text_ascent, text_descent = pdb.gimp_text_get_extents_fontname(text, size, size_type, fontname)

    center_x = center_x + ( ( box_width / 2 ) - ( text_width / 2 ) )
    center_y = center_y + ( ( box_height / 2 ) - ( text_height / 2 ) )

    text_layer = pdb.gimp_text_fontname(image, None, center_x, center_y, text, border, antialias, size, size_type, fontname)

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
