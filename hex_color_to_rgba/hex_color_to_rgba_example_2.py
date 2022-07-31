import bpy

import math


def hex_color_to_rgb(hex_color):
    """
    Converting from a color in the form of a hex triplet string (en.wikipedia.org/wiki/Web_colors#Hex_triplet)
    to a Linear RGB

    Supports: "#RRGGBB" or "RRGGBB"

    Note: We are converting into Linear RGB since Blender uses a Linear Color Space internally
    https://docs.blender.org/manual/en/latest/render/color_management.html
    """
    # remove the leading '#' symbol if present
    if hex_color.startswith("#"):
        hex_color = hex_color[1:]

    assert len(hex_color) == 6, f"RRGGBB is the supported hex color format: {hex_color}"

    # extracting the Red color component - RRxxxx
    red = int(hex_color[:2], 16)
    # dividing by 255 to get a number between 0.0 and 1.0
    srgb_red = red / 255
    linear_red = convert_srgb_to_linear_rgb(srgb_red)

    # extracting the Green color component - xxGGxx
    green = int(hex_color[2:4], 16)
    # dividing by 255 to get a number between 0.0 and 1.0
    srgb_green = green / 255
    linear_green = convert_srgb_to_linear_rgb(srgb_green)

    # extracting the Blue color component - xxxxBB
    blue = int(hex_color[4:6], 16)
    # dividing by 255 to get a number between 0.0 and 1.0
    srgb_blue = blue / 255
    linear_blue = convert_srgb_to_linear_rgb(srgb_blue)

    return tuple([linear_red, linear_green, linear_blue])


def hex_color_to_rgba(hex_color, alpha=1.0):
    """
    Converting from a color in the form of a hex triplet string (en.wikipedia.org/wiki/Web_colors#Hex_triplet)
    to a Linear RGB with an Alpha passed as a parameter

    Supports: "#RRGGBB" or "RRGGBB"
    """
    linear_red, linear_green, linear_blue = hex_color_to_rgb(hex_color)
    return tuple([linear_red, linear_green, linear_blue, alpha])


def convert_srgb_to_linear_rgb(srgb_color_component):
    """
    Converting from sRGB to Linear RGB
    based on https://en.wikipedia.org/wiki/SRGB#From_sRGB_to_CIE_XYZ
    """
    if srgb_color_component <= 0.04045:
        linear_color_component = srgb_color_component / 12.92
    else:
        linear_color_component = math.pow((srgb_color_component + 0.055) / 1.055, 2.4)

    return linear_color_component


##########################################################
#  _____                          _          _  _     _____
# |  ___|                        | |       _| || |_  / __  \
# | |____  ____ _ _ __ ___  _ __ | | ___  |_  __  _| `' / /'
# |  __\ \/ / _` | '_ ` _ \| '_ \| |/ _ \  _| || |_    / /
# | |___>  < (_| | | | | | | |_) | |  __/ |_  __  _| ./ /___
# \____/_/\_\__,_|_| |_| |_| .__/|_|\___|   |_||_|   \_____/
#                          | |
#                          |_|
##########################################################

# add an ico sphere and shade it smooth
bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=5)
bpy.ops.object.shade_smooth()

# set the Background color to Black
bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[0].default_value = (0, 0, 0, 1)

# set the render engine to CYCLES
bpy.context.scene.render.engine = "CYCLES"

# add a area light with the energy set to 100 and color #FF4858"
bpy.ops.object.light_add(type="AREA", radius=5, location=(0, -2, 0), rotation=(math.radians(90), 0, 0))
bpy.context.object.data.energy = 100
bpy.context.object.data.color = hex_color_to_rgb("#FF4858")

# add a area light with the energy set to 100 and color #F2CB05
bpy.ops.object.light_add(type="AREA", radius=5, location=(0, 2, 0), rotation=(math.radians(-90), 0, 0))
bpy.context.object.data.energy = 100
bpy.context.object.data.color = hex_color_to_rgb("#F2CB05")
