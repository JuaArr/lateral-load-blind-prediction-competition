import numpy as np


def earth_pressure_coefficient(theta):
    rad_theta = np.deg2rad(theta)

    k0 = 1-np.sin(rad_theta)
    ka = np.square(np.tan(np.pi/4 - rad_theta/2))
    kp = np.square(np.tan(np.pi/4 + rad_theta/2))

    return k0, ka, kp

def Ks(s, sa, sp, theta, alpha1=1.0, alpha2=1.0):

    k0, ka, kp = earth_pressure_coefficient(theta)

    ks = np.piecewise(s, [s <= sa, (s > sa) & (s <= 0.0), (s > 0.0) & (s < sp), s >= sp],
                      [ka,
                       lambda s: k0 - (k0 - ka) * (s/sa) * np.exp(alpha1 * (1.0 - s/sa)),
                       lambda s: k0 - (k0 - kp) * (s/sp) * np.exp(alpha2 * (1.0 - s/sp)),
                       kp])

    return ks


def dKs(s, sa, sp, theta, alpha1=1.0, alpha2=1.0):

    k0, ka, kp = earth_pressure_coefficient(theta)

    dks = np.piecewise(s, [s <= sa, (s > sa) & (s <= 0.0), (s > 0.0) & (s < sp), s >= sp],
                       [0,
                        lambda s: (k0 - ka) * (alpha1*s - sa)/sa**2 * np.exp(alpha1 * (1.0 - s/sa)),
                        lambda s: (k0 - kp) * (alpha2*s - sp)/sp**2 * np.exp(alpha2 * (1.0 - s/sp)),
                        0])

    return dks