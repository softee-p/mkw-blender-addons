import bpy
import math

def modify_spherical_camera_path(new_total_sides, new_max_top_angle, new_max_bottom_angle):
    selected_objects = bpy.context.selected_objects
    target_object = None
    
    for obj in selected_objects:
        if obj.type == 'MESH':
            target_object = obj
            break
    
    if target_object is None:
        print("Error: No mesh object selected. Please select a mesh object with an OrbitCam and run the script again.")
        return

    camera = next((child for child in target_object.children if child.name.endswith("_OrbitCam")), None)
    if camera is None:
        print(f"Error: The selected object '{target_object.name}' does not have an OrbitCam. Please run the main script first.")
        return

    target_empty = next((child for child in target_object.children if child.name.endswith("_CameraTarget")), None)
    if target_empty is None:
        print(f"Error: Camera target empty not found for '{target_object.name}'. Please run the main script first.")
        return

    positions_per_side = 15
    total_frames = new_total_sides * positions_per_side

    bpy.context.scene.frame_end = total_frames

    new_max_top_angle_rad = math.radians(new_max_top_angle)
    new_max_bottom_angle_rad = math.radians(new_max_bottom_angle)

    camera.animation_data_clear()

    for frame in range(1, total_frames + 1):
        bpy.context.scene.frame_set(frame)
        
        current_side = (frame - 1) // positions_per_side
        position_in_side = (frame - 1) % positions_per_side
        
        longitude = (current_side / new_total_sides) * 2 * math.pi
        latitude_range = new_max_top_angle_rad + new_max_bottom_angle_rad
        latitude = (position_in_side / (positions_per_side - 1)) * latitude_range - new_max_bottom_angle_rad
        
        radius = 5
        camera.location.x = radius * math.cos(longitude) * math.cos(latitude)
        camera.location.y = radius * math.sin(longitude) * math.cos(latitude)
        camera.location.z = radius * math.sin(latitude)
        
        camera.keyframe_insert(data_path="location", frame=frame)

    print(f"Camera path modified for '{target_object.name}': {new_total_sides} sides, max top angle: {new_max_top_angle}°, max bottom angle: {new_max_bottom_angle}°")

modify_spherical_camera_path(new_total_sides=30, new_max_top_angle=75, new_max_bottom_angle=75)