import numpy as np
import math
import dataSet.SensitivePenDataSet

"""
Usefull mainly for the sensitiv pen, it has some methods that calculates angle of the mvunio
"""

def getInclinaison(U):
    """
    Calculate angles between a vector and x,y,z axes
    :param U: vector
    :return: angles
    """
    norm = np.linalg.norm(U)

    alpha = math.acos(U[0] / norm)
    beta = math.acos(U[1] / norm)
    gamma = math.acos(U[2] / norm)

    angle = np.array([alpha, beta, gamma]) * 360 / (2 * np.pi)
    return angle

def computePenAngles(sentivePendataSet):
    """

    :param sentivePendataSet:
    :return:
    """
    # --- Getting initial euler angles
    initRotationMatrix = rotationMatrixCreation(sentivePendataSet.acceleration[15], sentivePendataSet.magnetometer[15])
    sentivePendataSet.initPsi = math.atan2(initRotationMatrix[0, 1], initRotationMatrix[0, 0])

    for k in range(len(sentivePendataSet.time)):
        # --- Getting rotation matrix from filtered data
        rotationMatrix = rotationMatrixCreation(sentivePendataSet.acceleration[k], sentivePendataSet.magnetometer[k])

        # --- Get inclinaison of the pen (theta)
        sentivePendataSet.posAngAcc.append(getInclinaison(sentivePendataSet.acceleration[k]))
        theta = sentivePendataSet.posAngAcc[k][0] - 90

        # --- getting orientation of the pen (for psi)
        a00 = rotationMatrix[0, 0]  # N.x
        a01 = rotationMatrix[0, 1]  # E.x

        if (abs(theta) > 360):  # set the lim to 80 but not usefull now
            psi = 0
        else:
            psi = (math.atan2(a01, a00) - sentivePendataSet.initPsi) * 180 / math.pi

            if -180 > psi >= -360:
                psi += 360
            elif 180 < psi <= 360:
                psi -= 360

        sentivePendataSet.sensitivePenAngles.append(np.array([psi, theta]))

    sentivePendataSet.posAngAcc = np.array(sentivePendataSet.posAngAcc)
    sentivePendataSet.sensitivePenAngles = np.array(sentivePendataSet.sensitivePenAngles)

    return sentivePendataSet.sensitivePenAngles

def isRotationMatrix(R):
    """
    Verify if a given matrix is a rotation matrix.

    :param R: rotation matrix
    :return: boolean
    """
    Rt = np.transpose(R)
    shouldBeIdentity = np.dot(Rt, R)
    I = np.identity(3, dtype=R.dtype)
    n = np.linalg.norm(I - shouldBeIdentity)

    return n < 1e-6


def rotationMatrixCreation(u, v):
    """
    Calculate a rotation matrix given 2 vectors

    A revoir

    :param u: vector
    :param v: vector
    :return: Rotation matrix
    """
    #normalisation
    D = u / np.linalg.norm(u)
    m = v / np.linalg.norm(v)

    #coordinates creation
    E = np.cross(D, m)
    E /= np.linalg.norm(E)

    N = np.cross(E,D)
    N /= np.linalg.norm(N)

    #matrix
    R = np.mat([N, E, D]).T #we transpose to have N, E, D in the column
    return R


def rotationMatrixToEulerAngles(R):
    """
    Calculates euler angles given Rotation Matrix.

    :param R: Rotation matrix
    :return: Euler angles
    """
    assert (isRotationMatrix(R))

    sy = math.sqrt(R[0, 0] * R[0, 0] + R[1, 0] * R[1, 0])
    singular = sy < 1e-6

    if not singular:
        x = math.atan2(R[2, 1], R[2, 2])
        y = math.atan2(-R[2, 0], sy)
        z = math.atan2(R[1, 0], R[0, 0])
    else:

        x = math.atan2(-R[1, 2], R[1, 1])
        y = math.atan2(-R[2, 0], sy)
        z = 0

    return np.array([x,y,z])

def eulerAnglesToRotationMatrix(theta) :
    """
    Calculates Rotation Matrix given euler angles.

    :param theta: Euler angles
    :return: Rotation Matrix
    """
    R_x = np.array([[1,         0,                  0                   ],
                    [0,         math.cos(theta[0]), -math.sin(theta[0])],
                    [0,         math.sin(theta[0]), math.cos(theta[0])]
                    ])

    R_y = np.array([[math.cos(theta[1]),    0,      math.sin(theta[1])],
                    [0,                     1,      0                   ],
                    [-math.sin(theta[1]),   0,      math.cos(theta[1])  ]
                    ])

    R_z = np.array([[math.cos(theta[2]),    -math.sin(theta[2]),    0],
                    [math.sin(theta[2]),    math.cos(theta[2]),     0],
                    [0,                     0,                      1]
                    ])

    R = np.dot(R_z, np.dot(R_y, R_x))

    return R

