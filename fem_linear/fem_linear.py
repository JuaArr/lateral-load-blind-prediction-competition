import numpy as np
from scipy.integrate import quad_vec

from utils.earth_pressure import Ks


def calculate_length(xyz, elem):
    n_elem = elem.shape[0]
    length = np.zeros(n_elem)
    for i in range(n_elem):
        x1 = xyz[elem[i, 0] - 1]
        x2 = xyz[elem[i, 1] - 1]     
        length[i] = x2 - x1

    return length


def calculate_element_properties(xyz, elem, section, properties):
    n_elem = elem.shape[0]
    element_properties = np.zeros((n_elem, 3)) # E, Iz, L
    
    E = properties["E"]
    element_properties[:, 0] = E

    L = calculate_length(xyz, elem)
    element_properties[:, 2] = L
    
    R = properties["R"]
    for i in range(n_elem):
        t = properties["t"][section[i] - 1]
        r = R-t
        Iz = np.pi/4 * (R**4 - r**4)
        element_properties[i, 1] = Iz

    return element_properties


def local_stiffness_matrix(E, Iz, L, Px):
    
    Ke = E*Iz/L**3 * np.array([[12, 6*L, -12, 6*L],
                              [6*L, 4*L**2, -6*L, 2*L**2],
                              [-12, -6*L, 12, -6*L],
                              [6*L, 2*L**2, -6*L, 4*L**2]])

    Kg = Px/(30*L) * np.array([[36, 3*L, -36, 3*L],
                               [3*L, 4*L**2, -3*L, L**2],
                               [-36, -3*L, 36, -3*L],
                               [3*L, L**2, -3*L, 4*L**2]]) # Revisar la obtencion de la matriz

    K = Ke - Kg

    return K


def assign_Fex(f, Fex, n_dof) -> None:
    offset = np.arange(n_dof, 0, -1, dtype=int)
    for node, dof, value in Fex:
        dof_f = node*n_dof - offset[dof-1]
        f[dof_f] = value


def assign_Uex(f, K_, Uex, n_dof) -> None:
    offset = np.arange(n_dof, 0, -1, dtype=int)
    for node, dof, value in Uex:
        dof_u = node*n_dof - offset[dof-1]
        K_[dof_u, :] = 0.0
        K_[dof_u, dof_u] = 1.0
        f[dof_u] = value