import tifffile
from skimage.filters import gaussian


class VoxelImage(object):
    def __init__(self, file_name):
        self.image = tifffile.imread(file_name)
        self.blurred_image = None

    def apply_gaussian(self, sigma=1.0):
        self.blurred_image = gaussian(self.image, sigma=sigma)

    def get_subset(self, ind, blurred=False):
        assert(len(ind) == 3)

        ix = ind[0]
        iy = ind[1]
        iz = ind[2]

        try:
            if blurred:
                subset = self.blurred_image[ix[0]:ix[1], iy[0]:iy[1], iz[0]:iz[1]]
            else:
                subset = self.image[ix[0]:ix[1], iy[0]:iy[1], iz[0]:iz[1]]
        except IndexError:
            raise "Indices out of bounds."
        return subset