import numpy as np

def main():
    mat1 = np.array([
        [1,2,3],
        [4,5,6]
    ])
    
    mat2 = np.array([
        [7,8],
        [9,8],
        [11,12]
    ])

    result_mat = np.dot(mat1,mat2)
    print("RESULT MATRIX")
    print(result_mat)


if __name__ == '__main__':
    main()