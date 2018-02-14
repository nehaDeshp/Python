'''
Matrix multiplication
'''

row1 = int(input("enter no.of rows for Matrix1: "))
col1 = int(input("enter no.of columns for Matrix1 : "))
row2 = int(input("enter no.of rows for Matrix1 :"))
col2 = int(input("enter no.of columns for Matrix2 : "))
if col1 != row2:
    print("columns in matrix1 is not equal to rows in matrix2")
else:
    mat1 = []
    mat2 = []
    for i in range(row1):
        list = []
        for j in range(col1):
            data = int(input("enter elements "))
            list.append(data)
        mat1.append(list)
    for i in range(row2):
        list = []
        for j in range(col2):
            data = int(input("enter elements "))
            list.append(data)
        mat2.append(list)
    c = []
    for i in range(row1):
        list = []
        for j in range(col1):
            k = 0
            sum = 0
            while k<col1:
                sum += (mat1[i][k]*mat2[k][j])
                k += 1
            list.append(sum)
        c.append(list)
    print(c)
