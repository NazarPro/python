def multiply_by_constant():
    rows1, columns1 = input('Enter size of matrix:').split()
    matrix1 = []
    for i in range(int(rows1)):
        matrix1.append(input().split())
    c = float(input('Enter constant:'))
    print('The result is:')
    for k in range(len(matrix1)):
        for s in range(len(matrix1[0])):
            print((float(matrix1[k][s])) * c, end=' ')
        print()
    print()


def add_matrices():
    rows1, columns1 = input('Enter size of first matrix:').split()
    matrix1 = []
    matrix2 = []
    print('Enter first matrix:')
    for i in range(int(rows1)):
        matrix1.append(input().split())
    rows2, columns2 = input('Enter size of second matrix:').split()
    print('Enter second matrix:')
    for j in range(int(rows2)):
        matrix2.append(input().split())
    if rows1 == rows2 and columns1 == columns2:
        print('The result is:')
        for k in range(len(matrix1)):
            for s in range(len(matrix1[0])):
                print((float(matrix1[k][s]) + float(matrix2[k][s])), end=' ')
            print()
        print()
    else:
        print('The operation cannot be performed.\n')


def multiply_matrices():
    rows1, columns1 = input('Enter size of first matrix:').split()
    matrix1 = []
    matrix2 = []
    print('Enter first matrix:')
    for i in range(int(rows1)):
        matrix1.append(input().split())
    rows2, columns2 = input('Enter size of second matrix:').split()
    print('Enter second matrix:')
    for j in range(int(rows2)):
        matrix2.append(input().split())
    result = 0
    if columns1 == rows2:
        print('The result is:')
        for k in range(len(matrix1)):
            for s in range(len(matrix2[0])):
                for z in range(len(matrix2)):
                    result += float(matrix1[k][z]) * float(matrix2[z][s])
                print(result, end=' ')
                result = 0
            print()
        print()
    else:
        print('The operation cannot be performed.\n')


def transpose():
    typetr = input('1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horisontal line\nYour choice:')
    if typetr == '1':
        rows1, columns1 = input('Enter size of first matrix:').split()
        matrix1 = []
        print('Enter matrix:')
        for i in range(int(rows1)):
            matrix1.append(input().split())
        for k in range(len(matrix1)):
            for s in range(len(matrix1[0])):
                print((matrix1[s][k]), end=' ')
            print()
        print()
    elif typetr == '2':
        rows1, columns1 = input('Enter size of first matrix:').split()
        matrix1 = []
        print('Enter matrix:')
        for i in range(int(rows1)):
            matrix1.append(input().split())
        for k in reversed(range(len(matrix1))):
            for s in reversed(range(len(matrix1[0]))):
                print((matrix1[s][k]), end=' ')
            print()
        print()
    elif typetr == '3':
        rows1, columns1 = input('Enter size of first matrix:').split()
        matrix1 = []
        print('Enter matrix:')
        for i in range(int(rows1)):
            matrix1.append(input().split())
        for k in range(len(matrix1)):
            for s in reversed(range(len(matrix1[0]))):
                print((matrix1[k][s]), end=' ')
            print()
        print()
    elif typetr == '4':
        rows1, columns1 = input('Enter size of first matrix:').split()
        matrix1 = []
        print('Enter matrix:')
        for i in range(int(rows1)):
            matrix1.append(input().split())
        for k in reversed(range(len(matrix1))):
            for s in range(len(matrix1[0])):
                print((matrix1[k][s]), end=' ')
            print()
        print()


def determinant():
    rows, columns = input('Enter size of first matrix:').split()
    print('Enter matrix:')
    matrix = []
    for i in range(int(rows)):
        matrix.append(input().split())
    determ(matrix)


def determ(matr):
    n = len(matr)
    matrx = matr[:]
    for fd in range(n):
        for i in range(fd + 1, n):
            if matrx[fd][fd] == 0:
                matrx[fd][fd] = 0.0000000001
            crscaler = float(matrx[i][fd]) / float(matrx[fd][fd])
            for j in range(n):
                matrx[i][j] = float(matrx[i][j]) - crscaler * float(matrx[fd][j])
    product = 1.0
    for i in range(n):
        product *= float(matrx[i][i])
    print('The result is:\n', product)


def transposeMatrix(m):
    return list(map(list, zip(*m)))

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i] + m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return float(m[0][0]) * float(m[1][1]) - float(m[0][1]) * float(m[1][0])

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1) ** c) * float(m[0][c]) * getMatrixDeternminant(getMatrixMinor(m, 0, c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[float(m[1][1])/determinant, -1 * float(m[0][1]) / determinant],
                [-1 * float(m[1][0]) / determinant, float(m[0][0]) / determinant]]
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m, r, c)
            cofactorRow.append(((-1) ** (r + c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    for row in range(len(cofactors)):
        for column in range(len(cofactors[0])):
            print(round(cofactors[row][column], 3), end=' ')
        print()

x = 1
while x == 1:
    userinp = input('1. Add matrices\n2. Multiply matrix by a constant\n'
                    '3. Multiply matrices\n4. Transpose matrix\n5. Calculate a determinant\n'
                    '6. Inverse matrix\n0. Exit\nYour choice: ')
    if userinp == '0':
        break
    elif userinp == '1':
        add_matrices()
    elif userinp == '2':
        multiply_by_constant()
    elif userinp == '3':
        multiply_matrices()
    elif userinp == '4':
        transpose()
    elif userinp == '5':
        determinant()
    elif userinp == '6':
        rows, columns = input('Enter size of first matrix:').split()
        matrix = []
        print('Enter matrix:')
        for i in range(int(rows)):
            matrix.append(input().split())
        if getMatrixDeternminant(matrix) != 0:
            getMatrixInverse(matrix)
        else:
            print("This matrix doesn't have an inverse.")
    else:
        print('Invalid input')
