import numpy as np


def refine_mesh(xyz, elem, section, n=5):
    def map_dof(xyz_id):
        return n*(xyz_id-1) + 1
    

    n_elem = elem.shape[0]
    n_new_xyz = n * n_elem + 1
    n_new_elem = n_new_xyz - 1
    
    new_xyz = np.zeros((n_new_xyz))
    for i in range(n_elem):
        x1 = xyz[elem[i, 0] - 1]
        x2 = xyz[elem[i, 1] - 1]
        x_vals = np.linspace(x1, x2, n+1)
        
        for j in range(n+1):
            new_xyz[i*n+j] = x_vals[j]
    
    new_elem = np.array([[elem_id+1, elem_id+2] for elem_id in range(n_new_elem)], dtype=int)

    new_section = np.zeros((n_new_elem), dtype=int)
    for i in range(n_elem):
        new_section[i*n:(i+1)*n] = section[i]

    return new_xyz, new_elem, new_section, map_dof