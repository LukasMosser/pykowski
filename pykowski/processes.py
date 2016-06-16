from os import chdir
from shlex import split
from subprocess import Popen
from numpy.random import randint


def unique_random_subsets(image, n_samples, dx):
    unique_triplets = set()
    for i in xrange(n_samples):
        triplet = get_triplet(image, dx)
        while triplet in unique_triplets:
            triplet = get_triplet(image, dx)

        unique_triplets.add(triplet)
        yield triplet


def get_triplet(image, dx):
    x = randint(low=0, high=image.shape[0]-dx[0]-1)
    y = randint(low=0, high=image.shape[1]-dx[1]-1)
    z = randint(low=0, high=image.shape[1]-dx[1]-1)
    return [x, y, z]


def run_karambola(name, home):
    chdir(home)
    chdir("computation/"+name)
    cmd_line = "../../../../karambola "+name+".poly --nolabels --force w000 --force w100 --force w200 --force w300 --force w010 --force w110 --force w210 --force w310 --force w020 --force w102 --force w120 --force w202 --force w220 --force w320 -o results"
    args = split(cmd_line)
    p = Popen(args)
    p.communicate()
    chdir(home)
    return True
