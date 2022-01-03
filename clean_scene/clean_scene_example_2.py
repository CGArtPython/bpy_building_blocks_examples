import bpy
import random
import math


def purge_orphans():
    if bpy.app.version >= (3, 0, 0):
        bpy.ops.outliner.orphans_purge(
            do_local_ids=True, do_linked_ids=True, do_recursive=True
        )
    else:
        # call purge_orphans() recursively until there are no more orphan data blocks to purge
        result = bpy.ops.outliner.orphans_purge()
        if result.pop() != "CANCELLED":
            purge_orphans()


def clean_scene():
    """
    Removing all of the objects, collection, materials, particles,
    textures, images, curves, meshes, actions, nodes, and worlds from the scene
    """
    if bpy.context.active_object and bpy.context.active_object.mode == "EDIT":
        bpy.ops.object.editmode_toggle()

    for obj in bpy.data.objects:
        obj.hide_set(False)
        obj.hide_select = False
        obj.hide_viewport = False

    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()

    collection_names = [col.name for col in bpy.data.collections]
    for name in collection_names:
        bpy.data.collections.remove(bpy.data.collections[name])

    # in the case when you modify the world shader
    world_names = [world.name for world in bpy.data.worlds]
    for name in world_names:
        bpy.data.worlds.remove(bpy.data.worlds[name])
    # create a new world data block
    bpy.ops.world.new()
    bpy.context.scene.world = bpy.data.worlds["World"]

    purge_orphans()


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

clean_scene()

max_rotation = math.radians(360)

for i in range(33):
    random_size = random.uniform(0.1, 2.0)
    random_location = (
        random.uniform(-5, 5),
        random.uniform(-5, 5),
        random.uniform(-5, 5),
    )
    random_rotation = (
        random.uniform(-max_rotation, max_rotation),
        random.uniform(-max_rotation, max_rotation),
        random.uniform(-max_rotation, max_rotation),
    )

    bpy.ops.mesh.primitive_monkey_add(
        size=random_size, location=random_location, rotation=random_rotation
    )
