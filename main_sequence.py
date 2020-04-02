import numpy as np
import matplotlib.pyplot as plt

# Global Constants
mu =  0.6
X = 0.74
Y = 0.25
Z = 0.01
c = 2.99792458e8 # speed of light (m/s)
sb = 5.670374419e-8 # stefan-boltzman constant
gamma_0 = 5/3
G = 6.67e-11 # gravitational constant
k = 1.38064852e-23# boltzmann constant
m_p = 1.6726219e-27 # proton mass
m_e = 9.10938356e-31 # electron mass

#TODO How is a defined?
a = (4*sb)/c  # Radiation density constant

h_bar = 6.62607004e-31 / (2 * np.pi) # reduced plancks constant

#TODO How is kappa defined?
# kappa = #

def kappa(rho, T):
    kappa_es = 0.02*(1.0 + X)  # m^2/kg
    kappa_ff = 1.0e24*(Z + 0.0001)*((rho/1000.0)**0.7)*T**(-3.5)  # m^2/kg
    kappa_H_neg = 2.5e-32*(Z/0.02)*((rho/1000.0)** 0.5)*(T**9.0)  # m^2/kg

    kappa_main = 1.0/((1.0/kappa_H_neg) + (1.0/max(kappa_es, kappa_ff)))
    return kappa_main

# Takes the mass of the star, density, radius, temperature and dT/dr as inputs
# Returns drho/dr (rate of change of density)
def drho_dr(M, rho, r, T, dT):
    numerator = (G * M * rho) / r**2 + dT * (rho * (k / (mu * m_p)) + (4/3) * a * T**3)
    denominator = ((3 * np.pi**2)**(2/3) * h_bar**2)/(3 * m_e * m_p) * (rho/m_p)**(2/3) + (k * T) / (mu * m_p)

    return -numerator/denominator

# Takes the luminosity of the star, temperature, radius, mass, density and adiabatic index as inputs
# Returns dT/dr (rate of change of temperature)
def dT_dr(L, T, r, M, rho, gamma):
    factor_1 = (3 * kappa(rho, T) * rho * L) / (16 * np.pi * a * c * T**3 * r**2) # First factor which determines temperature change
    numerator = (1 - 1/gamma) * G * M * rho
    denominator = r**2 * ((3 * np.pi**2)**(2/3) * h_bar**2) / (5 * m_e * T) * (rho/m_p)**(5/3) + rho * (k / (mu * m_p)) + (1/3) * a * T**3

    factor_2 = numerator/denominator # second factor which determines temperature change

    return -min(factor_1, factor_2) # Returns the minimum of the 2 factors

# Takes radius and density of inputs
# Returns dM/dr (rate of change of mass)
def dM_dr(r, rho):
    return 4 * np.pi * r**2 * rho

# Takes the density and temperature as inputs.
# Returns the function eps(rho, T), the total specific energy generation rate.
# See equations (8) and (9) of the project description.
def eps(rho, T):
    rho_5 = rho/(10**5)
    T_6 = T/(10**6)
    X_CNO = 0.03 * X

    eps_PP = 1.07e-7 * rho_5 * X*2 * T_6*4
    eps_CNO = 8.24e-26 * rho_5 * X * X_CNO * T_6**19.9

    return eps_PP + eps_CNO
    
# Takes the radius, density and temperature as inputs
# Returns dL/dr (rate of change of luminosity)
def dL_dr(r, rho, T):
    return 4 * np.pi * r**2 * rho * eps(rho, T)

# Takes the density and temperature as inputs
# Returns dtau/dr (rate of change of opacity)
def dtau_dr(rho, T):
    factor_1 = 2.5e-32 * (Z/0.02) * (rho/10**3)**(1/2) * T**9
    factor_1 = 1/factor_1

    factor_2 = max(0.02 * (1 + X), 1e-24 * (Z + 0.0001) * (rho/10**3)**0.7 * T**(-3.5))
    factor_2 = 1/factor_2

    return rho/(factor_1 + factor_2)


def lumin_mass_exact(m):
    if m < 0.7:
        return 0.35 * m ** 2.62
    else:
        return 1.02 * m ** 3.92


def radius_mass_exact(m):
    if m < 1.66:
        return 1.06*m**0.945
    else:
        return 1.33*m**0.555


vrme, vlme = np.vectorize(radius_mass_exact), np.vectorize(lumin_mass_exact)

