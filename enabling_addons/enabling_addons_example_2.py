import bpy
import addon_utils


def enable_addon(addon_module_name):

    loaded_default, loaded_state = addon_utils.check(addon_module_name)

    if not loaded_state:
        addon_utils.enable(addon_module_name)


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

enable_addon(addon_module_name="add_mesh_extra_objects")

for i in range(10):
    bpy.ops.mesh.primitive_solid_add(source='12', size=i*0.1)
    bpy.ops.object.modifier_add(type='WIREFRAME')

