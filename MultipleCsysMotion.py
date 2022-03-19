import numpy as np




def Rx(theta):
    theta = np.radians(theta)
    R = np.array([
        [1, 0, 0, 0],
        [0, np.cos(theta), -np.sin(theta), 0],
        [0, np.sin(theta), np.cos(theta), 0],
        [0, 0, 0, 1]
    ])
    return R

def Ry(theta):
    theta = np.radians(theta)
    R = np.array([
        [np.cos(theta), 0, np.sin(theta), 0],
        [0, 1, 0, 0],
        [-np.sin(theta), 0, np.cos(theta), 0],
        [0,0,0,1]
    ])
    return R

def Rz(theta):
    theta = np.radians(theta)
    R = np.array([
        [np.cos(theta), -np.sin(theta), 0, 0],
        [np.sin(theta), np.cos(theta), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    return R




if __name__=="__main__":
    T1 = np.array([
        [1, 0, 0, 1],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    r1 = np.array([1, 0, 0, 1])

    R = Rz(180)


    rf = T1.dot(R).dot(r1)

    print(rf)