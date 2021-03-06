## 2. Systems of equations as matrices ##

import numpy as np

# Set the dtype to float to do float math with the numbers.
matrix = np.asarray([
    [2, 1, 25],
    [3, 2, 40]  
], dtype=np.float32)

matrix[0] = matrix[0] * 2
matrix[0] = matrix[0] - matrix[1]
matrix[1] = matrix[1] - (matrix[0] * 3)
matrix[1] = matrix[1] / 2

## 4. Solving more complex equations ##

import numpy as np

matrix = np.asarray([
    [1, 2, 0, 7],
    [0, 3, 3, 11],
    [1, 2, 2, 11]
], dtype=np.float32)

#matrix[1] = matrix[1] - matrix[2]
matrix[2] = matrix[2] - matrix[0]
matrix[2] = matrix[2] / 2
matrix[1] = matrix[1] / 3
matrix[1] = matrix[1] - matrix[2]
matrix[0] = matrix[0] - 2 * matrix[1]

## 5. Echelon form ##

matrix = np.asarray([
    [0, 0, 0, 7],
    [0, 0, 1, 11],
    [1, 2, 2, 11],
    [0, 5, 5, 1]
], dtype=np.float32)

# Swap the first and the third rows - first swap
matrix[[0,2]] = matrix[[2,0]]
matrix[[1,3]] = matrix[[3,1]]
matrix[[2,3]] = matrix[[3,2]]

## 6. Reduced row echelon form ##

A = np.asarray([
        [0, 2, 1, 5],
        [3, 0, 1, 10],
        [1, 2, 1, 8]
        ], dtype=np.float32)

# First, we'll swap the second row with the first to get a nonzero coefficient in the first column
A[[0,1]] = A[[1,0]]

# Then, we divide the first row by 3 to get a coefficient of 1
A[0] /= 3

# Now, we need to make sure that our 1 coefficient is the only coefficient in its column
# We have to subtract the first row from the third row
A[2] -= A[0]

# Now, we move to row 2
# We divide by 2 to get a one as the leading coefficient
A[1] /= 2

# We subtract 2 times the second row from the third to get rid of the second column coefficient in the third row
A[2] -= (2 * A[1])

# Now, we can move to the third row, but it already looks good.
# We're finished, and our system is solved!

A[2] /= A[2,2]
A[1] -= A[2] * 0.5
A[0] -= A[2]
print(A)

## 7. Inconsistency ##

A = np.asarray([
    [10, 5, 20, 60],
    [3, 1, 0, 11],
    [8, 2, 2, 30],
    [0, 4, 5, 13]
], dtype=np.float32)

B = np.asarray([
    [5, -1, 3, 14],
    [0, 1, 2, 8],
    [0, -2, 5, 1],
    [0, 0, 6, 6]
], dtype=np.float32)
A_consistent,B_consistent = True,False


## 8. Infinite solutions ##

A = np.asarray([
        [2, 4, 8, 20],
        [4, 8, 16, 40],
        [20, 5, 5, 10]
], dtype=np.float32)
A_infinite = True

B = np.asarray([
        [1, 1, 1, 4],
        [3, -2, 5, 8],
        [8, -4, 5, 10]
        ], dtype=np.float32)
        
B_infinite = False