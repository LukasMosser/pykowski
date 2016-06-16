from trimesh import Trimesh
from skimage.measure import marching_cubes


def mesh_and_extract_largest_connected_surface(volume, level_set):
    vertices, faces = marching_cubes(volume, level_set)
    mesh = Trimesh()
    mesh.vertices = vertices
    mesh.faces = faces
    meshes = mesh.split(only_watertight=False)
    sorted_meshes = sorted(meshes, key=lambda x: len(x.vertices))
    return sorted_meshes[-1]
