from pykowski.image import VoxelImage
from pykowski.processes import unique_random_subsets
from pykowski.meshing import mesh_and_extract_largest_connected_surface
from pykowski.io import write_poly_from_mesh


def main():
    im = VoxelImage("data/ketton.tif")

    dx = [50, 50, 50]
    level_set = 0.8
    urs = unique_random_subsets(im.image, 10, dx)
    for subset in urs:
        print subset
        im_sub = im.get_subset(subset, dx, blurred=True, sigma=1.0)
        print im_sub.shape
        print im_sub.min(), im_sub.max()
        mesh = mesh_and_extract_largest_connected_surface(im_sub, level_set)
        print mesh
        out = write_poly_from_mesh("_".join([str(val) for val in subset]), mesh)

if __name__ == "__main__":
    main()

