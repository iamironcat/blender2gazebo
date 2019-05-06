'''This works with blender gui'''

import bpy

scene = bpy.context.scene

scene.unit_settings.system = 'METRIC'
scene.unit_settings.scale_length = 1.0

models = bpy.data.objects

for model in models:
    print(model.name)
    
    coords = model.location
    pos = []

    pos.append(coords[1] * -1)
    pos.append(coords[0] * -1)
    pos.append(coords[2])

    out = ""
    for p in pos:
        out += ("0" if p == 0.0 else "%.2f" % p)
        out += " "
    print(out + "0 0 0")

##########
# TO-DOS #
##########
# read argparse
# import io_scene_obj.export_obj
# xml.etree
# blender xml parsing - https://blenderartists.org/t/xml-parsing/383339
# don't parse xml from .dae as that doesn't have position

# io_scene_obj.export_obj.save(bpy.context, output_filename, global_matrix=Matrix.Identity(4), use_normals=True)
# output_obj_extension = output_filename.find('.obj')
# output_mtl_file = output_filename[:output_obj_extension] + '.mtl'
