import numpy as np
import math as m


def translation(matrix, tx, ty):
    print('\nObject Matrix After Translation')
    trans_matrix = np.eye(3)
    trans_matrix[0, 2] = tx
    trans_matrix[1, 2] = ty

    return trans_matrix @ matrix


def scaling(matrix, h, k):
    print('\nObject Matrix After Scaling')
    scale_matrix = np.eye(3)
    scale_matrix[0, 0] = h
    scale_matrix[1, 1] = k

    return scale_matrix @ matrix


def rotation(matrix, a, direction):
    rotation_matrix = np.eye(3)
    r = m.radians(a)
    s = m.sin(r)
    c = m.cos(r)
    if direction == 1:
        rotation_matrix[0, :2] = c, -s
        rotation_matrix[1, :2] = s, c
    elif direction == 2:
        rotation_matrix[0, :2] = c, s
        rotation_matrix[1, :2] = -s, c
    else:
        return '\nPlease Choose A Valid Direction For Rotation'

    print('\nObject Matrix After Rotation')
    return rotation_matrix @ matrix


def reflection(matrix, axis):
    reflection_matrix = np.eye(3)
    if axis == 1:
        reflection_matrix[1, 1] = -1
    elif axis == 2:
        reflection_matrix[0, 0] = -1
    else:
        return '\nPlease Choose a Valid Axis for Reflection'

    print('\nObject Matrix After Reflection')
    return reflection_matrix @ matrix


def shearing():
    pass


v = int(input('Enter number of Vertices in the object : '))
obj_matrix = np.empty((3, v))

for i in range(0, v):
    obj_matrix[0, i] = float(input(f'\nEnter x co-ordinate of {i + 1} vertex of object : '))
    obj_matrix[1, i] = float(input(f'Enter y co-ordinate of {i + 1} vertex of object : '))
    obj_matrix[2, i] = 1

print("\n\nHomogeneous Matrix of object's co-ordinates")
print(obj_matrix)

flag = True

while flag:
    print('\n\n-----Transformation-----')
    print('(1)Translation\n(2)Scaling\n(3)Rotation\n(4)Reflection\n(5)Shearing\n(6)Exit')
    option = int(input('\nWhich transformation do you want to perform : '))

    if option == 1:
        print('\n-----Translation-----')
        x = float(input('Enter translation length along x-axis : '))
        y = float(input('Enter translation length along y-axis : '))

        result = translation(obj_matrix, x, y)
        print(result)

    elif option == 2:
        print('\n-----Scaling-----')
        x = float(input('Enter Scaling factor along x-axis : '))
        y = float(input('Enter Scaling factor along y-axis : '))

        result = scaling(obj_matrix, x, y)
        print(result)

    elif option == 3:
        print('\n-----Rotation-----')
        o = float(input('Enter Rotation Angle(in Degree) : '))
        d = int(input('Choose Direction of Rotation\n(1)Anticlockwise\n(2)Clockwise\n'))

        result = rotation(obj_matrix, o, d)
        print(result)

    elif option == 4:
        print('\n-----Reflection-----')
        a = int(input('Choose axis for Reflection\n(1)x-axis\n(2)y-axis\n'))

        result = reflection(obj_matrix, a)
        print(result)

    elif option == 5:
        print('\n-----Shearing-----')

    elif option == 6:
        print('\nExit')
        flag = False
    else:
        print("\nChoose a Valid Option!")