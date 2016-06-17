from pykowski.image import VoxelImage
from pykowski.processes import unique_random_subsets, run_karambola
from pykowski.meshing import mesh_and_extract_largest_connected_surface
from pykowski.io import write_poly_from_mesh
from pykowski.karambola import KarambolaResults
import os
import numpy as np

def main():

    im = VoxelImage("data/ketton.tif")

    dx = [300, 300, 300]
    level_set = 0.8
    urs = unique_random_subsets(im.image, 1, dx)
    for subset in urs:
        print subset
        im_sub = im.get_subset(subset, dx, blurred=True, sigma=1.0)
        print im_sub.shape
        print im_sub.min(), im_sub.max()
        mesh = mesh_and_extract_largest_connected_surface(im_sub, level_set)
        print mesh
        name = "_".join([str(val) for val in subset])
        out = write_poly_from_mesh(name, mesh)

    mesh_files = []
    for file in os.listdir("."):
        if file.endswith(".poly"):
            indices = [int(val) for val in file.strip(".poly").split("_")]

            try:
                run_karambola(name, name)
            except:
                print "couldnt run"

            res = KarambolaResults()
            res.load_from_karambola_output(name+"/", "ketton", indices, dx)
            res.write_to_json_format(name+".json")

            res_in = KarambolaResults()
            res_in.load_from_json_format(name+".json")
            print "wrote results"

    print "done"

if __name__ == "__main__":
    main()

