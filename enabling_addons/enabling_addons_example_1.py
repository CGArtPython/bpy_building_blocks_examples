import bpy
import addon_utils


def enable_addon(addon_module_name):

    loaded_default, loaded_state = addon_utils.check(addon_module_name)

    if not loaded_state:
        addon_utils.enable(addon_module_name)


##########################################################
#  _____                          _          _  _     __
# |  ___|                        | |       _| || |_  /  |
# | |____  ____ _ _ __ ___  _ __ | | ___  |_  __  _| `| |
# |  __\ \/ / _` | '_ ` _ \| '_ \| |/ _ \  _| || |_   | |
# | |___>  < (_| | | | | | | |_) | |  __/ |_  __  _| _| |_
# \____/_/\_\__,_|_| |_| |_| .__/|_|\___|   |_||_|   \___/
#                          | |
#                          |_|
##########################################################


enable_addon(addon_module_name="add_curve_extra_objects")

bpy.ops.curve.spirals(
    spiral_type="LOG",
    radius=1.42,
    turns=265,
    steps=128,
    dif_z=0.1,
    B_force=0.99,
    edit_mode=False,
)

bpy.context.object.data.bevel_depth = 0.01
