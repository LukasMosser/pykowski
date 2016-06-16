import numpy as np
from trimesh.io.export import export_mesh


def import_ply(file_name):
    vertices = []
    faces = []

    try:
        with open(file_name+".ply", "r") as f:
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
    except IOError:
        print "no file with name"+file_name

    faces = np.array(faces)
    vertices = np.array(vertices)
    return faces, vertices


def write_poly_from_mesh(name, mesh, export_off=False):
    vertices = mesh.vertices
    faces = mesh.faces
    if export_off:
        export_success = export_mesh(mesh, name+".off", file_type='off')
    try:
        with open(name+".poly", "wb") as f:
            f.write("POINTS\n")
            for i, vertex in enumerate(vertices):
                f.write(str(i+1)+": "+" ".join([str(val) for val in vertex])+"\n")

            f.write("POLYS\n")
            for j, face in enumerate(faces):
                f.write(str(j+1)+": "+" ".join([str(val+1) for val in face])+" <\n")

            f.write("END")
    except IOError:
        print "could not create file"


def write_poly(file_name, vertices, faces):
    try:
        with open(file_name+".poly", "wb") as f:
            f.write("POINTS\n")
            for i, vertex in enumerate(vertices):
                f.write(str(i+1)+": "+" ".join([str(val) for val in vertex])+"\n")

            f.write("POLYS\n")
            for j, face in enumerate(faces):
                f.write(str(j+1)+": "+" ".join([str(int(val)) for val in face])+" <\n")

            f.write("END")
    except IOError:
        print "could not create file"