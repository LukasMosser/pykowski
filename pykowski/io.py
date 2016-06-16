import numpy as np


def import_ply(file_name):
    vertices = []
    faces = []
    with open(file_name, "r") as f:
        data_section = False
        vertices_i = 0
        vertices_count = 0

        faces_section = False
        for i, row in enumerate(f):
            if data_section:
                if vertices_i < vertices_count:
                    vertex = [val.strip("\n") for val in row.split(" ")]
                    vertices.append(vertex)
                    vertices_i += 1
                    if vertices_i == vertices_count:
                        faces_section = True
                elif faces_section:
                    face = [str(int(val.strip("\n"))+1) for val in row.split(" ")[1::]]
                    faces.append(face)
            else:
                if i == 3:
                    vertices_count = int(row.split(" ")[2])
                    print vertices_count
                elif i == 7:
                    faces_count = int(row.split(" ")[2])
                    print faces_count
                elif row.split(" ")[0] == "end_header\n":
                    data_section = True

    faces = np.array(faces)
    vertices = np.array(vertices)
    return faces, vertices
