# Automated LOD Tool

An automation script for **Autodesk 3ds Max** that rapidly generates Levels of Detail (LODs) for game assets using the **ProOptimizer** modifier.

## Overview

Creating LODs manually is tedious. This tool takes your high-poly mesh and automatically generates three lower-resolution variants, maintaining the original naming convention for easy integration into game engines like Unreal or Unity.

## Features

- **One-Click Generation**: Select objects and run the script to generate all LODs instantly.
- **Standardized Reduction**:
  - **LOD1**: 50% vertex count.
  - **LOD2**: 25% vertex count.
  - **LOD3**: 10% vertex count.
- **Non-Destructive**: Clones the original object, leaving your source mesh untouched.
- **Stack Collapse**: Automatically collapses the modifier stack on generated LODs for clean geometry.

## Prerequisites

- **Autodesk 3ds Max** (Requires `pymxs` support).

## Usage

1. Open 3ds Max.
2. Select one or more mesh objects.
3. Run the script `Scripts/AutoLod.py` (Scripting > Run Script...).
4. The tool will create new objects in the scene:
   - `ObjectName_LOD1`
   - `ObjectName_LOD2`
   - `ObjectName_LOD3`

## Script Reference

### `Scripts/AutoLod.py`
The automation logic.
- **`create_lods()`**: The main entry point.
- **LOD Logic**: Defines a dictionary of levels (`{1: 50.0, 2: 25.0, 3: 10.0}`).
- **ProOptimizer**: Applies the `ProOptimizer` modifier to clones of the selected mesh, sets the vertex percentage, calculates the reduction, and collapses the stack to bake the changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
Copyright (c) 2026 ARGUS