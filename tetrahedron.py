#!/usr/bin/env python3

import math
import matplotlib.pyplot as plt
import sys


# multiply vector by scalar
def scalar_vector_multiplication(s, v):
    # no error checking
    return [s * i for i in v]

# add n vectors together
def n_vector_addition(nv):
    return list(map(sum, zip(*nv)))

# translate 4d coordinate into 3d coordinate
# c = (X, Y, Z, A)
def coordinate_translation(c, vX, vY, vZ, vA):
    nv = (
        scalar_vector_multiplication(c[0], vX),
        scalar_vector_multiplication(c[1], vY),
        scalar_vector_multiplication(c[2], vZ),
        scalar_vector_multiplication(c[3], vA)
    )
    return n_vector_addition(nv)

def main():
    # initializition
    fig = plt.figure()
    axe = fig.add_subplot(projection = "3d")
    axe.set_box_aspect((1, 1, 1))

    # draw origin/centroid point
    # axe.scatter(0, 0, 0, c = "black", marker = "o")

    # coordinates of a tetrahedron
    # also the vectors which represent our four axes
    vX = (math.sqrt((8 / 9)), 0, -(1 / 3))
    vY = (-math.sqrt((2 / 9)), math.sqrt((2 / 3)), -(1 / 3))
    vZ = (-math.sqrt((2 / 9)), -math.sqrt((2 / 3)), -(1 / 3))
    vA = (0, 0, 1)

    # inverse coordinates of tetrahedron
    inv_vX = scalar_vector_multiplication(-1, vX)
    inv_vY = scalar_vector_multiplication(-1, vY)
    inv_vZ = scalar_vector_multiplication(-1, vZ)
    inv_vA = scalar_vector_multiplication(-1, vA)

    # draw and annotate our four axes
    axe.plot([vX[0], inv_vX[0]], [vX[1], inv_vX[1]], [vX[2], inv_vX[2]], c = "black")
    axe.text(*vX, "X", c = "black")
    axe.plot([vY[0], inv_vY[0]], [vY[1], inv_vY[1]], [vY[2], inv_vY[2]], c = "black")
    axe.text(*vY, "Y", c = "black")
    axe.plot([vZ[0], inv_vZ[0]], [vZ[1], inv_vZ[1]], [vZ[2], inv_vZ[2]], c = "black")
    axe.text(*vZ, "Z", c = "black")
    axe.plot([vA[0], inv_vA[0]], [vA[1], inv_vA[1]], [vA[2], inv_vA[2]], c = "black")
    axe.text(*vA, "A", c = "black")

    for iX in range(0, 2):
        for iY in range(0, 2):
            for iZ in range(0, 2):
                for iA in range(0, 2):
                    axe.scatter(*coordinate_translation((iX, iY, iZ, iA), vX, vY, vZ , vA), c = "green", marker = "o")

    axe.set_xlabel("X")
    axe.set_ylabel("Y")
    axe.set_zlabel("Z")

    plt.show()

if __name__ == "__main__":
    main()

sys.exit()