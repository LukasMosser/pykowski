import numpy as np


class KarambolaResults(object):
    def __init__(self, direc):
        self.direc = direc
        self.shortest_edge, self.longest_edge = None
        self.smallest_area, self.largest_area = None
        self.surface_type = None

        self.w000, self.w010, self.w020 = None
        self.w100, self.w110, self.w120, self.w102 = None
        self.w200, self.w210, self.w220, self.w202 = None
        self.w300, self.w310 = None

        self.eigs = None
        self.eigs_w102, self.eigs_w202 = None
        self.beta_102, self.gamma_102 = None

        self.beta_202, self.gamma_202 = None

        self.load_surface_results(self.direc)
        self.load_w000_w100_w200_w300(self.direc)
        self.load_w010_w110_w210_w310(self.direc)
        self.load_tensors(self.direc)
        self.assign_tensors()
        self.compute_eigenvalues()

    def load_surface_results(self, direc):
        temp = []
        with open(direc+"surface_props", "r") as f:
            for row in f:
                vals = [val.strip("\n") for val in row.split(" ")]
                vals = [val for val in vals if val not in ["=", ""]]
                temp.append(vals)
        self.shortest_edge = float(temp[0][2])
        self.longest_edge = float(temp[1][2])
        self.smallest_area = float(temp[2][2])
        self.largest_area = float(temp[3][2])
        self.surface_type = temp[6][1]

    def load_w000_w100_w200_w300(self, direc):
        temp = []
        with open(direc+"w000_w100_w200_w300", "r") as f:
            for row in f:
                vals = [val.strip("\n") for val in row.split(" ")]
                if "#" in vals:
                    pass
                else:
                    vals = [val for val in vals if val not in ["=", ""]]
                    temp.append(vals)

            try:
                self.w000 = float(temp[0][1])
            except ValueError:
                self.w000 = -9999999999.99

            try:
                self.w100 = float(temp[1][1])
            except ValueError:
                self.w100 = -9999999999.99

            try:
                self.w200 = float(temp[2][1])
            except ValueError:
                self.w200 = -9999999999.99

            try:
                self.w300 = float(temp[3][1])
            except ValueError:
                self.w300 = -9999999999.99

    def load_w010_w110_w210_w310(self, direc):
            temp = []
            with open(direc+"w010_w110_w210_w310", "r") as f:
                for row in f:
                    vals = [val.strip("\n") for val in row.split(" ")]
                    if "#" in vals:
                        pass
                    else:
                        vals = [val for val in vals if val not in ["=", ""]]
                        temp.append(vals)

                try:
                    self.w010 = np.array([float(val) for val in temp[0][1:4]])
                except ValueError:
                    self.w010 = np.ones((3, 1))*-9999999999.99

                try:
                    self.w110 = np.array([float(val) for val in temp[1][1:4]])
                except ValueError:
                    self.w110 = np.ones((3, 1))*-9999999999.99

                try:
                    self.w210 = np.array([float(val) for val in temp[2][1:4]])
                except ValueError:
                    self.w210 = np.ones((3, 1))*-9999999999.99

                try:
                    self.w310 = np.array([float(val) for val in temp[3][1:4]])
                except ValueError:
                    self.w310 = np.ones((3, 1))*-9999999999.99

    def load_tensors(self, direc):
        self.tensors = {}
        tensor_names = ["w020", "w102", "w120", "w202", "w220", "w320"]
        for tensor_name in tensor_names:
            temp = []
            with open(direc+tensor_name, "r") as f:
                for row in f:
                    vals = [val.strip("\n") for val in row.split(" ")]
                    if "#" in vals:
                        pass
                    else:
                        vals = [val for val in vals if val not in ["=", ""]]
                        temp.append(vals)

                values = temp[0][1:10]
                new_values = []
                for val in values:
                    new_values.append(val.replace("ERROR", "-9999999999.99"))

                self.tensors[tensor_name] = np.array([float(val) for val in new_values]).reshape(3,3)
    def assign_tensors(self):
        self.w020 = self.tensors["w020"]
        self.w102 = self.tensors["w102"]
        self.w120 = self.tensors["w120"]
        self.w220 = self.tensors["w220"]
        self.w202 = self.tensors["w202"]

    def compute_eigenvalues(self):
        self.eigs = np.linalg.eig(self.w220)
        self.eigs_w102 = np.linalg.eig(self.w102)
        self.beta_102 = min(self.eigs_w102[0])/max(self.eigs_w102[0])
        self.gamma_102 = sorted(self.eigs_w102[0])[1]/max(self.eigs_w102[0])
        self.eigs_w202 = np.linalg.eig(self.w202)
        self.beta_202 = min(self.eigs_w202[0])/max(self.eigs_w202[0])
        self.gamma_202 = sorted(self.eigs_w202[0])[1]/max(self.eigs_w202[0])
