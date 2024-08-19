import bpy
import math

def setup_spherical_camera_path(max_top_angle=90, max_bottom_angle=90):
    scene = bpy.context.scene
    
    selected_objects = bpy.context.selected_objects
    target_object = None
    
    for obj in selected_objects:
        if obj.type == 'MESH':
            target_object = obj
            break
    
    if target_object is None:
        print("Error: No mesh object selected. Please select a mesh object and run the script again.")
        return
    
    existing_empty = next((obj for obj in bpy.data.objects if obj.name.startswith(f"{target_object.name}_CameraTarget")), None)
    if existing_empty:
        print(f"Error: The selected object '{target_object.name}' already has an orbit camera setup.")
        return
    
    bpy.ops.object.empty_add(type='PLAIN_AXES', location=target_object.location)
    empty_target = bpy.context.active_object
    empty_target.name = f"{target_object.name}_CameraTarget"
    empty_target.parent = target_object
    empty_target.matrix_parent_inverse = target_object.matrix_world.inverted()
    
    bpy.ops.object.camera_add(location=(target_object.location.x, target_object.location.y, target_object.location.z + 5))
    camera = bpy.context.active_object
    camera.name = f"{target_object.name}_OrbitCam"
    camera.parent = target_object
    scene.camera = camera
    
    total_sides = 20
    positions_per_side = 15
    total_frames = total_sides * positions_per_side
    
    scene.frame_end = total_frames
    
    max_top_angle_rad = math.radians(max_top_angle)
    max_bottom_angle_rad = math.radians(max_bottom_angle)
    
    for frame in range(1, total_frames + 1):
        scene.frame_set(frame)
        
        current_side = (frame - 1) // positions_per_side
        position_in_side = (frame - 1) % positions_per_side
        
        longitude = (current_side / total_sides) * 2 * math.pi
        latitude_range = max_top_angle_rad + max_bottom_angle_rad
        latitude = (position_in_side / (positions_per_side - 1)) * latitude_range - max_bottom_angle_rad
        
        radius = 5
        camera.location.x = radius * math.cos(longitude) * math.cos(latitude)
        camera.location.y = radius * math.sin(longitude) * math.cos(latitude)
        camera.location.z = radius * math.sin(latitude)
        
        constraint = camera.constraints.get("Track To")
        if constraint is None:
            constraint = camera.constraints.new(type='TRACK_TO')
            constraint.target = empty_target
            constraint.track_axis = 'TRACK_NEGATIVE_Z'
            constraint.up_axis = 'UP_Y'
        
        camera.keyframe_insert(data_path="location", frame=frame)

    scene.frame_set(1)

    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            area.spaces[0].region_3d.view_perspective = 'CAMERA'
            break

    print("Camera path setup complete.")

setup_spherical_camera_path(max_top_angle=60, max_bottom_angle=60)