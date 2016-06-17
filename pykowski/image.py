import tifffile
from skimage.filters import gaussian


class VoxelImage(object):
    def __init__(self, file_name):
        self.image = tifffile.imread(file_name)

    def get_subset(self, ind, dx, blurred=False, sigma=1.0):
        assert(len(ind) == 3)

        try:
            subset = self.image[ind[0]:ind[0]+dx[0], ind[1]:ind[1]+dx[1], ind[2]:ind[2]+dx[2]]
        except IndexError:
            raise "Indices out of bounds."

        if blurred:
            subset = gaussian(subset, sigma=sigma)

        return subset