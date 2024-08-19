import bpy
from bpy.types import Panel

class VIEW3D_PT_orbit_camera(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Orbit Camera"
    bl_label = "Orbit Camera Setup"

    def draw(self, context):
        layout = self.layout
        props = context.scene.orbit_camera_props

        layout.prop(props, "max_top_angle")
        layout.prop(props, "max_bottom_angle")
        layout.operator("object.orbit_camera_setup")

        layout.separator()

        layout.prop(props, "new_total_sides")
        layout.prop(props, "new_max_top_angle")
        layout.prop(props, "new_max_bottom_angle")
        layout.operator("object.orbit_camera_modify")

def register():
    bpy.utils.register_class(VIEW3D_PT_orbit_camera)

def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_orbit_camera)