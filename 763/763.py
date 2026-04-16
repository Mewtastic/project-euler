import numpy as np
from numba import njit
import sys

# Change recursion limit. Probably pretty dumb, but hey...
sys.setrecursionlimit(10000)
divisions = 0

while divisions <= 0:
    divisions = input("Enter Amoeaba Divisions (INT): ")
    try:
        divisions = int(divisions)
    except:
        divisions = 0
        print("Please enter an INT greater than 0")

amoebas = 2*divisions+1

@njit
def valid_division(amoeba, culture):
    x = np.array((amoeba[0]+1, amoeba[1], amoeba[2]), dtype='i')
    y = np.array((amoeba[0], amoeba[1]+1, amoeba[2]), dtype='i')
    z = np.array((amoeba[0], amoeba[1], amoeba[2]+1), dtype='i')

    for i in range(culture.shape[0]):
        if np.all(culture[i] == x) or np.all(culture[i] == y) or np.all(culture[i] == z):
            return False
    return True

@njit
def divide(amoeba, culture, step, divisions):
    new_division = np.array([(amoeba[0]+1, amoeba[1], amoeba[2]),
                            (amoeba[0], amoeba[1]+1, amoeba[2]),
                            (amoeba[0], amoeba[1], amoeba[2]+1)], dtype='i')

    developed_culture = np.concatenate((culture, new_division))
    np.delete(developed_culture, amoeba)

    unique = find_divisions(divisions, developed_culture, step+1)
    
    return unique

@njit
def find_divisions(divisions, culture=np.array([(0,0,0)], dtype='i'), step=0):
    unique = 0
    if step == divisions-1:
        for i in culture:
            if valid_division(i, culture):
                unique += 1
    else:
        for i in culture:
            if valid_division(i, culture):
                unique += divide(i, culture, step, divisions)

    return unique

unique = find_divisions(divisions)

print("Total Amoebas: " + str(amoebas))
print("Possible Arrangements: " + str(unique))
