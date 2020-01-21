import numpy as np
import math

def print_mat(mat):
    for i in mat:
        for j in i:
            print(j," ",end="")
        print()


def translation(matrix):
    tx = int(input("Enter translation length along x axis: "))
    ty = int(input("Enter translation length along y axis: "))

    trans_matrix = np.eye(3)
    trans_matrix[0, 2] = tx
    trans_matrix[1, 2] = ty

    return trans_matrix @ matrix


def scaling(matrix):
    ax = int(input("Enter scaling factor along x axis: "))
    ay = int(input("Enter scaling factor along y axis: "))
    scal_matrix = np.eye(3)
    scal_matrix[0][0] = ax
    scal_matrix[1][1] = ay

    return scal_matrix @ matrix


def rotation(matrix):
    n = int(input("Enter angle of rotation ( in degrees): "))
    print("1.Clock-wise Rotation")
    print("2.Anti clock-wise Rotation")
    sin = math.sin(math.radians(n))
    cos = math.cos(math.radians(n))
    arr = np.eye(3)
    arr[0, :2] = cos, -sin
    arr[1, :2] = sin, cos
    return arr  @ matrix




def main():
    n = int(input("Enter number of vertices of the object: "))
    arr = np.zeros((3,n) , dtype = np.int32)
    for i in range(4):
        arr[0][i] = int(input(f'Enter x coordinate of { i+1 }  vertex: '))
        arr[1][i] = int(input(f'Enter y coordinate of {i+1} vertex: '))
        arr[2][i] = 1

    while True:
        print("1.Translation ")
        n = int(input("Enter your choice: "))
        if n == 1:
            brr = translation(arr)
            print('\nObject Matrix After Translation')
            print_mat(brr)
        elif n == 2


if __name__=="__main__":
    main()