from pykowski.image import VoxelImage
from pykowski.processes import unique_random_subsets, run_karambola
from pykowski.meshing import mesh_and_extract_largest_connected_surface
from pykowski.io import write_poly_from_mesh
from pykowski.karambola import KarambolaResults
import os
import click
import numpy as np
import shutil
from tqdm import *

@click.command()
@click.option('--file', default='/images/ketton.tif', help="Image to process")
@click.option('--samples', default=1, help='Number of samples to compute')
@click.option('--dx', nargs=3, default=[50, 50, 50], type=click.Tuple([int, int, int]), help="Tuple of 3 indices indicating the subvolume box size")
@click.option('--seed', default=666, help='Random number generator seed')
@click.option('--dest', default='/results', help="The folder to output results to.")
@click.option('--level', default=0.8, help="Level set to use for construction of mesh.")
def run_app(file, samples, dx, seed, dest, level):

    image_name = file.split("/")[-1].strip(".tif")
    np.random.seed(seed)
    im = VoxelImage(file)
    level_set = level
    urs = unique_random_subsets(im.image, samples, dx)

    print "Computing meshes..."
    for subset in tqdm(urs, total=samples):
        im_sub = im.get_subset(subset, dx, blurred=True, sigma=1.0)
        mesh = mesh_and_extract_largest_connected_surface(im_sub, level_set)
        name = "_".join([str(val) for val in subset])
        out = write_poly_from_mesh(name, mesh)

    files = []
    for file in os.listdir("."):
        if file.endswith(".poly"):
            files.append(file)
    print "Computing tensors..."
    for file in tqdm(files):
        indices = [int(val) for val in file.strip(".poly").split("_")]

        try:
            run_karambola(name, name)
        except:
            print "Failed to run Karambola"

        res = KarambolaResults()
        res.load_from_karambola_output(name+"/", image_name, indices, dx)
        res.write_to_json_format(image_name+"_"+name+".json")

        res_in = KarambolaResults()
        res_in.load_from_json_format(image_name+"_"+name+".json")

    print "Moving results..."
    files = []
    for file in os.listdir("."):
        if file.endswith(".json"):
            files.append(file)

    for file in tqdm(files):
        shutil.copy(file, dest+"/"+file)
    print "Finished. Exiting."

if __name__ == "__main__":
    run_app()