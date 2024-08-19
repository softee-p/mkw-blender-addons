bl_info = {
    "name": "Orbit Camera Setup",
    "author": "monkeyworks",
    "version": (0, 1, 0),
    "blender": (4, 2, 0),
    "location": "View3D > Sidebar > Orbit Camera",
    "description": "Setup and modify orbital cam to render images used for Gaussian Splat rendering",
    "warning": "",
    "doc_url": "",
    "category": "Camera",
}

import bpy
from . import operators, panels, properties

def register():
    properties.register()
    operators.register()
    panels.register()

def unregister():
    panels.unregister()
    operators.unregister()
    properties.unregister()

if __name__ == "__main__":
    register()