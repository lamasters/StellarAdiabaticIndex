import numpy as np
from main_sequence import *

def step(conds, r, gamma):
    dM = dM_dr(r, conds['rho'])
    dL = dL_dr(r, conds['rho'], conds['T'])
    dT = dT_dr(conds['L'], conds['T'], r, conds['M'], conds['rho'], gamma)
    dtau = dtau_dr(conds['rho'], conds['T'])
    drho = drho_dr(conds['M'], conds['rho'], r, conds['T'], dT)

    return np.array({'M' : dM, 'L' : dL, 'T' : dT, 'tau' : dtau, 'rho' : drho})

#def rk_solve(diffs, init_conds, R, dr):
