#1
#1
"""
Calculate the sum and the number of positive elements of the matrix A[N, N]
located above the main diagonal.
"""
n=3
x=[]
for i in range(n):
    y=[]
    for j in range(n):
        print('Enter Yhe Elements:')
        y.append(int(input()))
    x.append(b)
z = 0
o = 0
for i in range(n):
    for j in range(i + 1, n):
        if x[i][j] > 0:
            o += a[i][j]
            z+= 1
print("Num of Positive: " , z)
print("Sum: " , o)

#2
"""
Given a matrix B[N, M]. Find the maximum and minimum elements in each
row of the matrix and swap them with the first and last elements of the row, respectively.
"""
n = 3
x = []
for i in range(n):
    x.append(list(map(int, input().split())))\

def min1(x):
    return list(map(min, x))
min1(x)
#2
#1
"""
An integer square matrix of order n is given. Determine if it is a magic square, that
is, a matrix in which the sums of elements in all rows and columns are the same.
"""
#---
#2
"""
Given a rectangular matrix A[N, N]. Swap first and the last columns are swapped and displayed
"""
n=int(input("enter the number of rows: "))
m=int(input("enter the number of columns: "))
x=[]

for i in range(n):
    y=[]
    for j in range(n):
        print("enter the element: ")
        y.append(int(input()))
    x.append(y)

print("final array: ")
for i in range(m):
    for j in range(n):
        print(x[i][j], end = ' ')
    print()
for i in range(n):
    t = x[i][0]
    x[i][0] = x[i][m-1]
    x[i][m-1] = t

for i in range(n):
    for j in range(m):
        print(x[i][j], end = ' ')
    print()
#3
#1
"""
Determine if the given integer square matrix of the nth order is symmetric
(with respect to the main diagonal).
"""
n = int(input("n range: "))
m = int(input("m range: "))
x = []
for i in range(n):
    x.append(list(map(int, input().split())))

for i in range(m):
    for j in range(n):
        print(x[i][j], end = " ")
    print()

b = "True"

for i in range(m):
    for j in range(n):
        if x[i][j] != x[j][i]:
            b = "False"
            break
print(b)

#2
"""
Given a real matrix of size n x m. By rearranging its rows and columns, ensure
that the largest element (or one of them) is in the upper left corner.
"""
n=int(input("Enter the number of rows: "))
m=int(input("Enter the number of columns: "))
x=[]
for i in range(n):
    y=[]
    for j in range(n):
        print('Enter the elements: ')
        y.append(int(input()))
    x.append(y)

print('Final array look like: ')
for i in range(m):
    for j in range(n):
        print(x[i][j], end=' ')
    print()

max = x[0][0]
iel = jel = 0
for i in range(m):
    for j in range(n):
        if x[i][j] > max:
            max = x[i][j]
            iel = i
            jel = j
x[0], x[iel] = x[iel], x[0]
x[0][0], x[0][jel] = x[0][jel], x[0][0]
for row in x:
    print(row)

#4
#1
"""
Given a rectangular matrix. Find the row with the largest and the row with the
smallest sum of elements. Print the found strings and the sums of their elements.
"""
n = int(input("n range: "))
m = int(input("m range: "))
x = []
for i in range(n):
    x.append(list(map(int, input().split())))
for i in range(m):
    for j in range(n):
        print(x[i][j], end=" ")
    print()
y = []
for i in range(len(x)):
    y.append(sum(x[i]))
print(x[y.index(max(s))] + "largest sum: " + max(y) + x[y.index(min(s))] + "smallest sum: " + min(y))

#2
"""
Given a square matrix A[N, N], Write zeros instead of negative elements of the
matrix, and ones instead of positive ones. Print the lower triangular matrix in the conventional
form.
"""
n = int(input("n range: "))
m = int(input("m range: "))
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
for i in range(m):
    for j in range(n):
        print(arr[i][j], end = " ")
    print()

arr = [[1 if x > 0 else 0 for x in i] for i in arr]
for i in range(len(arr)):
    print(*[arr[i][x] if x <= i else " " for x in range(len(arr[i]))])
#5
#1
"""
Sort in ascending order the elements of each row of an n x m matrix
"""
#--
#2
"""
Given a real matrix of size n x m, all elements of which are different. In each
row, the element with the smallest value is selected. If the number is even, then it is replaced
by zero, odd - by one. Display the new matrix.
"""
def SmallInRow(mat):
    mine = min(mat)
    return mine

n = int(input("n range: "))
m = int(input("m range: "))
x = []
for i in range(n):
    x.append(list(map(int, input().split())))
for i in range(m):
    for j in range(n):
        print(x[i][j], end = " ")
    print()
b = []
for i in range(n):
    b.append(smallestInRow(x[i]))
print(b)

for i in range(len(b)):
    if b[i] % 2 == 0:
        b[i] = 0
    else:
        b[i] = 1
print(b)
#6
#1
"""
You are given an integer square matrix. Find the largest element in each row
and the smallest element in each column. Display on screen.
"""
#--
#2
"""
Given a real square matrix of order N (N is odd), all elements of which are
different. Find the largest element among those on the main and secondary diagonals and
swap it with the element on the intersection of these diagonals.
"""
def DiagonalMinMax(arr):
    n = len(arr)
    if n == 0:
        return

    pMin = arr[0][0]
    pMax = arr[0][0]
    sMin = arr[0][n - 1]
    sMax = arr[0][n - 1]

    for i in range(1, n):

        for j in range(1, n):

            if i == j:

                if arr[i][j] < pMin:
                    pMin = arr[i][j]

                if arr[i][j] > pMax:
                    pMax = arr[i][j]

            if (i + j) == (n - 1):

                if arr[i][j] < sMin:
                    sMin = arr[i][j]

                if arr[i][j] > sMax:
                    sMax = arr[i][j]

print("Principal diagonal smallest element: " + pMin)
print("Principal diagonal greatest element : " + pMax)

print("Secondary diagonal smallest element: " + sMin)
print("Secondary diagonal greatest element: " + sMax)


matrix = [[1, 2, 3, 4, 5],
          [5, 6, 7, 82, 6],
          [1, 2, 11, 33, 4],
          [5, 6, 8, 5, 8],
          [4, 9, 1, 6, 5]]

DiagonalMinMax(matrix)
#7
#1
"""
A square matrix, symmetric about the main diagonal, is given by the upper
triangle as a one-dimensional array. Restore the original matrix and print row by row.
"""
def low(arr, row, col):
    for i in range(0, row):

        for j in range(0, col):

            if i < j:

                print("0", end = " ")

            else:
                print(arr[i][j],
                      end = " ")

        print(" ")


def upp(arr, row, col):
    for i in range(0, row):

        for j in range(0, col):

            if i > j:
                print("0", end=" ")

            else:
                print(arr[i][j],
                      end=" ")

        print(" ")


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
row = 3
col = 3

print("lower triangular matrix: ")
low(arr, row, col)

print("upper triangular matrix: ")
upp(arr, row, col)

#2
"""
For a given square matrix, form a one-dimensional array of its diagonal elements.
Find the trace of a matrix by summing the elements of a one-dimensional array. Transform the
original matrix according to the rule: divide even rows by the resulting value, leave odd rows
unchanged.
"""
def d(arr):
    n = 3

    for col in range(n):

        scol = col
        srow = 0

        while (scol >= 0 and
               srow < n):
            print(arr[srow][scol], end = " ")

            scol -= 1
            srow += 1

        print()

    for row in range(1, n):
        srow = row
        scol = n - 1

        while (srow < n and scol >= 0):
            print(arr[srow][scol],
                  end = " ")

            scol -= 1
            srow += 1

        print()


arr = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

d(arr)
#8
#1
"""
Given a matrix of order n and a number k. Divide the elements of the kth row
by the diagonal element located in this row.
"""
n = 4

def showMat(arr):
    i = None
    j = None
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print('')


def kthS(mat, n, k):
    mat.sort()

    return mat[k - 1]


def ReplaceD(arr, k):
    i = None
    j = None
    mat = [0] * n

    for i in range(n):
        for j in range(n):
            mat[j] = arr[i][j]
        arr[i][i] = kthS(mat, n, k)
    showMat(arr)


arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]

k = 3
ReplaceD(arr, k)

#2
"""
Given a square matrix. Get the transposed matrix (inverted with respect to the
main diagonal) and display it on the screen
"""
#--
#9
#1
"""
For an integer square matrix, find the number of elements that are multiples
of k and the largest of these elements.
"""
#--
#2
"""
In a given real square matrix of order n, find the element with the greatest
modulus. Get a square matrix of order n - 1 by discarding from the original matrix the row and
column at the intersection of which the element with the found value is located.
"""
def GetCofactor(m, i, j):
    return [row[: j] + row[j + 1:] for row in (m[: i] + m[i + 1:])]


def DeterminantOfMatrix(arr):
    if len(arr) == 2:
        value = arr[0][0] * arr[1][1] - arr[1][0] * arr[0][1]
        return value

    sum = 0

    for current_column in range(len(arr)):
        sign = (-1) ** current_column

        sub_det = determinantOfMatrix(getcofactor(arr, 0, current_column))

        Sum += (sign * arr[0][current_column] * sub_det)

    return sum


arr = [[1, 0, 2, -1],
        [3, 0, 0, 5],
        [2, 1, 4, -3],
        [1, 0, 5, 0]]
print("Determinant of the matrix is : " + DeterminantOfMatrix(arr))

#10
#1
"""
Find the maximum among all elements of those rows of a given matrix
that are ordered (either ascending or descending).
"""
def MaxElement(arr):
    norows = len(arr)
    nocolumn = len(arr[0])

    for i in range(norows):

        max = 0
        for j in range(nocolumn):
            if arr[i][j] > max:
                max = arr[i][j]

        print(max)

arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]

MaxElement(arr)

#2
"""
Arrange the columns of the matrix D[M, N] in ascending order of the
elements of the kth row (1 <= k <= M).
"""
def SortRow(arr):
    for i in range(len(arr)):

        for j in range(len(arr[i])):

            for k in range(len(arr[i]) - j - 1):

                if arr[i][k] > arr[i][k + 1]:
                    x = arr[i][k]
                    arr[i][k] = arr[i][k + 1]
                    arr[i][k + 1] = x

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=" ")
        print()


arr = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

SortRow(arr)
#11
#1
"""
Given a real square matrix of order n, find the sum of the elements of the row
containing the element with the smallest value. It is assumed that there is only one such
element.
"""
n = int(input("Enter the size of the square matrix: "))
x = []
print("Enter your array: ")
for i in range(n):
    x.append([int(j) for j in input().split()])

min1 = [min(i) for i in x]
b = min1.index(min(min1))

print("min of array: " + min(map(min, x)))
print("sum: " + format(sum(a[b])))

#2
"""
2. Among the columns of a given integer matrix containing only such elements that
modulo is not greater than 10, find the column with the minimum product of the elements and
swap with the neighboring one.
"""
#--
#12
#1
"""
For a given square matrix, find k such that the kth row matrix coincides with the kth column.
"""
n = int(input("Enter the size of the matrix (sqare): "))
x = []
print("Enter array: ")
for i in range(n):
    x.append([int(j) for j in input().split()])

rev = list(map(list, zip(*x)))
for i in range(n):
    for j in range(n):
        if x[i] == rev[j]:
            print(i + 1 + "row and" + j + 1, "column are equal")

#2
"""
Given a real matrix of size n x m. It is required to transform the matrix: element
by element subtract the last row from all rows except the last one.
"""
def Spec_Sub(arr):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr[i])):
            arr[i][j] = arr[i][j] - arr[len(arr) - 1][j]
    return arr

n = int(input("Enter n range: "))
m = int(input("Enter m range: "))
x = []
for i in range(n):
    x.append(list(map(int, input().split())))

x = Spec_Sub(arr = x)
for i in range(n):
    for j in range(m):
        print(x[i][j], end = ' ')
    print()
#13
#1
"""
Determine the smallest element of each even row of the matrix A[M, N].
"""


#2
"""
Find the largest and smallest elements of a rectangular matrix and swap them.
"""

#14
#1
"""
Given a square matrix. Swap the row with the maximum element on the
main diagonal with the row with the given number m.
"""


#2
"""
Write a program that fills a square matrix of order n with natural numbers 1, 2, 3,
..., n2, writing them into it "in a spiral".
For example, for n = 5 we get the following matrix: 1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
14 12 11 10 9
"""

#15
#1
"""
Determine the numbers of rows of the matrix R[M, N], at least one element
of which is equal to c, and multiply the elements of these rows by d.
"""


#2
"""
Among those rows of an integer matrix that contain only odd elements, find
the row with the maximum sum of the modules of the elements.
"""