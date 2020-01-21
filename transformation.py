import numpy as np


def print_mat(mat):
    for i in mat:
        for j in i:
            print(j," ",end="")
        print()


def translation(matrix):
    tx = int(input("Enter scaling factor along x axis: "))
    ty = int(input("Enter scaling factor along y axis: "))
    print('\nObject Matrix After Translation')
    trans_matrix = np.eye(3)
    trans_matrix[0, 2] = tx
    trans_matrix[1, 2] = ty

    return trans_matrix @ matrix


def

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
            print_mat(brr)


if __name__=="__main__":
    main()