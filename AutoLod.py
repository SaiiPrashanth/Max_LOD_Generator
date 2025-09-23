from pymxs import runtime as rt

def create_lods():
    
    # Get the selected objects
    selection = rt.selection
    if not selection or len(selection) == 0:
        rt.messageBox("Please select one or more objects to create LODs for.")
        return

    # Define LOD levels and their vertex percentage
    lod_levels = {
        1: 50.0,  # LOD1 will have 50% of the vertices
        2: 25.0,  # LOD2 will have 25% of the vertices
        3: 10.0   # LOD3 will have 10% of the vertices
    }

    # Process each selected object
    for obj in selection:
        original_name = obj.name
        print(f"Processing object: {original_name}")

        for lod_num, vertex_percent in lod_levels.items():
            # Clone the original object
            lod_obj = rt.copy(obj)
            
            # Rename the cloned object
            lod_obj.name = f"{original_name}_LOD{lod_num}"

            # Select the new object to ensure it's the focus
            rt.select(lod_obj)

            # Add the ProOptimizer modifier
            pro_optimizer_mod = rt.ProOptimizer()
            rt.addModifier(lod_obj, pro_optimizer_mod)

            # Get the modifier from the object's modifier stack
            mod = lod_obj.modifiers[0]
            
            # Set the vertex percentage
            mod.VertexPercent = vertex_percent
            
            # Calculate the optimization
            mod.Calculate = True

            # Force a complete redraw to ensure the calculation is processed
            rt.completeRedraw()
            
            # Collapse the modifier stack to apply the changes
            rt.collapseStack(lod_obj)
            
            print(f"  Created {lod_obj.name} with {vertex_percent}% vertices.")

    rt.messageBox("LOD generation complete!")

create_lods()
