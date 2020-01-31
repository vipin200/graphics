import numpy as np
import math
import matplotlib.pyplot as plt

def print_mat(mat):
    for i in mat:
        for j in i:
            print(j," ",end="")
        print()


def translation(matrix):
    tx = int(input("Enter translation length along x axis: "))
    ty = int(input("Enter translation length along y axis: "))
    tz = int(input("Enter translation length along z axis: "))
    trans_matrix = np.eye(4)
    trans_matrix[0, 3] = tx
    trans_matrix[1, 3] = ty
    trans_matrix[2, 3] = tz
    return trans_matrix @ matrix


def scaling(matrix):
    ax = int(input("Enter scaling factor along x axis: "))
    ay = int(input("Enter scaling factor along y axis: "))
    az = int(input("Enter scaling factor along z axis: "))
    scal_matrix = np.eye(4)
    scal_matrix[0][0] = ax
    scal_matrix[1][1] = ay
    scal_matrix[2][2] = az

    return scal_matrix @ matrix


def rotation(matrix):
    n = int(input("Enter angle of rotation ( in degrees): "))
    print("Choose axis of rotation: ")
    print("1.About x-axis: ")
    print("2.About y-axis: ")
    print("3.About z axis: ")
    axis = int(input("Enter choice: "))
    sin = math.sin(math.radians(n))
    cos = math.cos(math.radians(n))
    arr = np.eye(4)
    if axis == 1:
        arr[1, 1:3] = cos, -sin
        arr[2, 1:3] = sin, cos
    elif axis == 2:
        arr[0, 0] = cos, -sin
        arr[2, :2] = sin, cos

    return arr  @ matrix

def reflection(matrix):
    ref_matrix = np.eye(3)
    print("Choose axis for reflection:  ")
    print("1.X-axis")
    print("2.Y-axis")
    axis = int(input("Enter a choice: "))
    if axis == 1:
        ref_matrix[1][1] = -1
    else:
        ref_matrix[0][0] = -1
    return  ref_matrix @ matrix

def plot(arr , brr):
    X = arr[0, :]
    Y = arr[1, :]
    X = np.append(X, X[0])
    Y = np.append(Y, Y[0])
    X_tr = brr[0, :]
    Y_tr = brr[1, :]
    X_tr = np.append(X_tr, X_tr[0])
    Y_tr = np.append(Y_tr, Y_tr[0])

    plt.plot(X, Y, color='b', label="Original object")
    plt.plot(X_tr, Y_tr, color='r', label="Transformed Object")
    plt.legend()
    plt.show()


def main():
    n = int(input("Enter number of vertices of the object: "))
    arr = np.zeros((3,n) , dtype = np.int32)
    for i in range(n):
        arr[0][i] = int(input(f'Enter x coordinate of { i+1 }  vertex: '))
        arr[1][i] = int(input(f'Enter y coordinate of {i+1} vertex: '))
        arr[2][i] = 1

    while True:
        print("2-D Transformation: ")
        print("1.Translation ")
        print("2.Scaling ")
        print("3.Rotation ")
        print("4.Reflection ")
        print("5.Exit")
        n = int(input("Enter your choice: "))
        if n == 1:
            brr = translation(arr)
            print('\nObject Matrix After Translation: ')
            print_mat(brr)
            plot(arr,brr)

        elif n == 2:
            brr = scaling(arr)
            print('\nObject Matrix After Scaling: ')
            print_mat(brr)
            plot(arr,brr)
        elif n == 3:
            brr = rotation(arr)
            print('\nObject Matrix After Rotation: ')
            print_mat(brr)
            plot(arr,brr)
        elif n == 4:
            brr = reflection(arr)
            print('\nObject Matrix After Reflection: ')
            print_mat(brr)
            plot(arr,brr)

        else:
            break


if __name__=="__main__":
    main()