"""
To run this you will need the bpybb Python package.

You can watch this video for detailed instructions on how to get the bpybb Python package:
https://cgpython.com/bpybb-install

or

You can install the package as a Blender add-on by following 
this link https://cgpython.com/bpybb
to the latest version of the add-on

If you know how to install Python packages into the embedded Python via pip
you can use the following link to get the pip instructions
https://pypi.org/project/bpy-building-blocks/

"""

import bpy
import addon_utils

from bpybb.addon import enable_addon

# def enable_addon(addon_module_name):

#     loaded_default, loaded_state = addon_utils.check(addon_module_name)

#     if not loaded_state:
#         addon_utils.enable(addon_module_name)


##########################################################
#  _____                          _          _  _     _____
# |  ___|                        | |       _| || |_  |____ |
# | |____  ____ _ _ __ ___  _ __ | | ___  |_  __  _|     / /
# |  __\ \/ / _` | '_ ` _ \| '_ \| |/ _ \  _| || |_      \ \
# | |___>  < (_| | | | | | | |_) | |  __/ |_  __  _| .___/ /
# \____/_/\_\__,_|_| |_| |_| .__/|_|\___|   |_||_|   \____/
#                          | |
#                          |_|
##########################################################

enable_addon(addon_module_name="io_import_images_as_planes")

image_path = r"c:\tmp\365_loop.mp4"

bpy.ops.import_image.to_plane(files=[{"name": image_path}])
