import bpy
from bpy.types import Operator
from .utils import setup_spherical_camera_path, modify_spherical_camera_path

class OBJECT_OT_orbit_camera_setup(Operator):
    bl_idname = "object.orbit_camera_setup"
    bl_label = "Setup Orbit Camera"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        props = context.scene.orbit_camera_props
        setup_spherical_camera_path(props.max_top_angle, props.max_bottom_angle)
        return {'FINISHED'}

class OBJECT_OT_orbit_camera_modify(Operator):
    bl_idname = "object.orbit_camera_modify"
    bl_label = "Modify Orbit Camera"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        props = context.scene.orbit_camera_props
        result = modify_spherical_camera_path(props.new_total_sides, props.new_max_top_angle, props.new_max_bottom_angle)
        
        if result is not None:
            self.report({'ERROR'}, result)
            return {'CANCELLED'}
        
        self.report({'INFO'}, "Orbit camera modified successfully.")
        return {'FINISHED'}


def register():
    bpy.utils.register_class(OBJECT_OT_orbit_camera_setup)
    bpy.utils.register_class(OBJECT_OT_orbit_camera_modify)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_orbit_camera_modify)
    bpy.utils.unregister_class(OBJECT_OT_orbit_camera_setup)