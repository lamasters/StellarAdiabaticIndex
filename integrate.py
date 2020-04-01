import numpy as np
from main_sequence import *

M_sun = 1.9885e30 # Mass of the sun

# Calculate the values of each parameter for the
# current integration step
# Returns the updated array of variables
def step(conds, r, gamma):
    M, L, T, tau, rho = conds

    dM = dM_dr(r, rho)
    dL = dL_dr(r, rho, T)
    dT = dT_dr(L, T, r, M, rho, gamma)
    dtau = dtau_dr(rho, T)
    drho = drho_dr(M, rho, r, T, dT)

    return np.array([dM, dL, dT, dtau, drho])

# Calculate the 4th order Runge-Kutta values,
# find the delta in each condition from these and
# return the new values
def rk_solve(conds, R, dr, gamma):
    k1 = dr * step(conds, R, gamma)
    k2 = dr * step(conds + k1/2, R + dr/2, gamma)
    k3 = dr * step(conds + k2/2, R + dr/2, gamma)
    k4 = dr * step(conds + k3, R + dr, gamma)

    diff = (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return conds + diff

# Calculate the value of the optical
# depth at the surface
# Returns inf if undefined
def surf_bound(conds, R, gamma):
    drho = drho_dr(conds[0], conds[4], R, conds[2], dT_dr(conds[1], conds[2], R, conds[0], conds[4], gamma))
    if drho != 0:
        tau_lim = kappa(conds[4], conds[2]) * conds[4]**2 / drho
    else:
        tau_lim = np.inf

    return tau_lim

# Integrate the differential equations with the 
# given initial conditions
# Returns the final state when the opacity target
# is reached or the mass of the star is greater than
# 1000M_sun
def integrate_functions(conds):
    dr = 10000
    R = dr / 1000
    gamma = 5/3
    dtau = dtau_dr(conds[4], conds[2])
    tau_lim = abs(surf_bound(conds, R, gamma))
    
    # Check whether the opacity or mass condition has been met
    while dtau < tau_lim and conds[0] < 1e3 * M_sun:
        conds = rk_solve(conds, R, dr, gamma)
        R += dr
        dtau = dtau_dr(conds[4], conds[2])
        tau_lim = abs(surf_bound(conds, R, gamma))

    return conds