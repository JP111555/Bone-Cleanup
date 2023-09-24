import bpy

# Set the name of the armature
armature_name = "Torso"

# List of mesh names you want to work with
mesh_names = ["7_mesh-1-sm-0-material-D808-3C7", "7_mesh-1-sm-1-material-D808-11A", "7_mesh-1-sm-2-material-D808-3BF"]  # Add the names of your meshes here

# Get a reference to the armature object
armature = bpy.data.objects.get(armature_name)

# Check if the armature exists
if armature:
    # Switch to Edit Mode for the armature
    bpy.context.view_layer.objects.active = armature
    armature.select_set(True)
    bpy.ops.object.mode_set(mode='EDIT')
    
    # Create a set to store bone names that are associated with the specified meshes
    valid_bone_names = set()
    
    # Iterate through the specified meshes
    for mesh_name in mesh_names:
        # Get a reference to the current mesh object
        mesh = bpy.data.objects.get(mesh_name)
        
        # Check if the mesh exists and is of type 'MESH'
        if mesh and mesh.type == 'MESH':
            # Create a set of vertex group names from the current mesh
            vertex_groups_mesh = set(vg.name for vg in mesh.vertex_groups)
            
            # Add bone names associated with the mesh to the valid_bone_names set
            for bone_name in armature.data.edit_bones:
                if bone_name.name in vertex_groups_mesh:
                    valid_bone_names.add(bone_name.name)
    
    # Iterate through the bones in Edit Mode and delete bones not associated with the specified meshes
    for bone_name in armature.data.edit_bones:
        if bone_name.name not in valid_bone_names:
            armature.data.edit_bones.remove(bone_name)
    
    # Switch back to Object Mode for the armature
    bpy.ops.object.mode_set(mode='OBJECT')

    print("Deleted bones not weighted to the selected meshes.")
else:
    print("Armature not found. Please check the name.")
