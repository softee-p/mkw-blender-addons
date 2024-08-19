import bpy
from bpy.props import FloatProperty, IntProperty, PointerProperty
from bpy.types import PropertyGroup

class OrbitCameraProperties(PropertyGroup):
    max_top_angle: FloatProperty(
        name="Max Top Angle",
        default=60,
        min=0,
        max=90
    )
    max_bottom_angle: FloatProperty(
        name="Max Bottom Angle",
        default=60,
        min=0,
        max=90
    )
    new_total_sides: IntProperty(
        name="New Total Sides",
        default=20,
        min=4
    )
    new_max_top_angle: FloatProperty(
        name="New Max Top Angle",
        default=75,
        min=0,
        max=90
    )
    new_max_bottom_angle: FloatProperty(
        name="New Max Bottom Angle",
        default=75,
        min=0,
        max=90
    )

def register():
    bpy.utils.register_class(OrbitCameraProperties)
    bpy.types.Scene.orbit_camera_props = PointerProperty(type=OrbitCameraProperties)

def unregister():
    del bpy.types.Scene.orbit_camera_props
    bpy.utils.unregister_class(OrbitCameraProperties)