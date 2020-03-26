# Phys 375 Stellar Adiabatic Index Group

## Introduction

This repository contains the code for calculating the properties of main sequence starts and then analyzing the effects of varying the adiabatic index.

## Code Style

An emphasis should be put on understandable code meaning the following measures should be taken:

1. Commenting

    All functions should have a brief description of what they're doing as well as any necessary information on inputs/outputs
    Any important features such as main loops or notable calculations should also be commented explaining their purpose
    The project section (Ex. 2.2.2) should be noted to keep track of what purpose the code serves

2. Functions

    It's in the best interest of organization and testing to represent each formula and calculation as its own function.
    Global variables such as universal constants and actions such as generating plots can be used

3. Testing

    Unit tests should be written for each function to make sure that the formulas are actually doing what they're intended to.
    This will help when presneting our results to prove that they are reliable. If there are any notable test cases formula
    the project description or known values (eg. surface temperature of the sun) these should be used, otherwise boundary conditions
    and values within expected ranges should be used.

4. Style Guide

    To keep consistent style across the project we should try to adhere to the Google style guide found [here](https://google.github.io/styleguide/pyguide.html)

5. Contributing

    In the interest of avoiding breaking code please follow these steps when contributing code.
    
    1. Create a new branch from the master branch

    2. Commit code to new branch

    3. Push code to new branch

    4. Create pull request to merge new branch back into master branch

    Each pull request should be reviewed and tested by another group member before being approved.