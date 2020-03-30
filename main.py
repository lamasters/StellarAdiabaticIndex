import numpy as np
import matplotlib.pyplot as plt

# Global Constants
mu =  0.6
X = 0.7
Y = 0.3
Z = 0
gamma_0 = 5/3
G = 6.67e-11 # gravitational constant
k = 1.38064852e-23# boltzmann constant
m_p = 1.6726219e-27 # proton mass
m_e = 9.10938356e-31 # electron mass

#TODO How is a defined?
a = #

h_bar = 6.62607004e-31 / (2 * np.pi) # reduced plancks constant

#TODO How is kappa defined?
kappa = #

# Takes the mass of the star, density, radius, temperature and dT/dr as inputs
# Returns drho/dr (rate of change of density)
def drho_dr(M, rho, r, T, dT):
    numerator = (G * M * rho) / r**2 + dT * (rho * (k / (mu * m_p)) + (4/3) * a * T**3)
    denominator = ((3 * np.pi**2)**(2/3) * h_bar**2)/(3 * m_e * m_p) * (rho/m_p)**(2/3) + (k * T) / (mu * m_p)

    return -numerator/denominator

# Takes the luminosity of the star, temperature, radius, mass, density and adiabatic index as inputs
# Returns dT/dr (rate of change of temperature)
def dT_dr(L, T, r, M, rho, gamma):
    factor_1 = (3 * kappa * rho * L) / (16 * np.pi * a * c * T**3 * r**2) # First factor which determines temperature change
    
    numerator = (1 - 1/gamma) * G * M * rho
    denominator = r**2 * ((3 * np.pi**2)**(2/3) * h_bar**2) / (5 * m_e * T) * (rho/m_p)**(5/3) + rho * (k / (mu * m_p)) + (1/3) * a * T**3)

    factor_2 = numerator/denominator # second factor which determines temperature change

    return -min(factor_1, factor_2) # Returns the minimum of the 2 factors

# Takes radius and density of inputs
# Returns dM/dr (rate of change of mass)
def dM_dr(r, rho):
    return 4 * np.pi * r**2 * rho

# Takes the radius, density and temperature as inputs
# Returns dL/dr (rate of change of luminosity)
def dL_dr(r, rho, T):
    return 4 * np.pi * r**2 * rho**2 * X**2 * (1.07e-12 * (T/10**6)**4 + 8.24e-31 * 0.03 * (T/10**6)**19.9)

# Takes the density and temperature as inputs
# Returns dtau/dr (rate of change of opacity)
def dtau_dr(rho, T):
    factor_1 = 2.5e-32 * (Z/0.02) * (rho/10**3)**(1/2) * T**9
    factor_1 = 1/factor_1

    factor_2 = max(0.02 * (1 + X), 1e-24 * (Z + 0.0001) * (rho/10**3)**0.7 * T**(-3.5))
    factor_2 = 1/factor_2

    return rho/(factor_1 + factor_2)