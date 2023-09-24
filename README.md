# Bone-Cleanup

I created this short script with the aid of Chat GTP for the Character rigs in HFW and HZD, as they often have several layers of bones imported, making the extracted rigs hard to pose. 

## Script Setup
Import "Bone_Cleanup.py" into Blender by opening a current or existing project file and navigating to the Scripting tab(should be on the top Right). Once you're there, import the Python script by clicking the folder icon and importing it from there. 

Once you've done that, go under the armature_name variable and put the name of the armature section you want to clean up. Under the mesh_names variable, you can list the meshes the armature chosen has. The format should be { mesh_names = ["MESH1"], ["MESH2"], ["MESH3"], ["Etc"] }. You don't need to worry about the names already under the variables. You can replace them with your mesh and armature. 

If you've followed these steps, then you should be ready. Just click the play button near the folder icon to run the script.

