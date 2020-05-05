"""This program solves a system of equations using Cramer's rule"""

'''Takes the matrix, the constant and the row index and adds a multiple of
the first row to this new row'''
def adding_two_rows(a,m,s):
    for j in range(len(a[0])):
        a[s][j]+=m*a[0][j]
    return a

'''finding the minor matrix'''
def minor(a,i,j):
    a.pop(i)
    for l in range(len(a)):
        a[l].pop(j)
    return a

def cofactor_first_element(a):
    return cofactor(a[0][0],minor(a,0,0))

#Finding the cofactor by multiplying matrix a with the value b
def cofactor(b,a):
    l=[]
    for i in a:
        l.append(i)
    c=len(l)-1
    for i in range(len(l[c])):
        l[c][i]*=b
    return l

#Finding the determinant
def det(a,b):
    if len(a)==len(a[0])==1:
        return (-1)**b*a[0][0]
    c=len(a)
    if a[0][0]==0:
        for i in range(c):
            if a[i][0]:
                a[0],a[i]=a[i],a[0]
                b+=1
                break
        if a[0][0]==0:
            return 0
    for i in range(1,c):
        if a[i][0]:
            a=adding_two_rows(a,-a[i][0]/a[0][0],i)
    a=cofactor_first_element(a)
    return det(a,b)

'''putting b in the i'th coloumn of a'''
def move(a,b,i):
    for j in range(len(a)):
        a[j][i]=b[j]
    return a

'''copying a 2D array'''
def copy(a):
    b=[]
    for i in range(len(a)):
        b.append([])
        for j in range(len(a[0])):
            b[i].append(a[i][j])
    return b

'''copying a 1D array'''
def copy1d(a):
    b=[]
    for i in range(len(a)):
        b.append(a[i])
    return b

'''Applying Cramer's rule'''
def Cramer(a,b):
    a1= det(copy(a),0)
    ans=[]
    for i in range(n):
        ans.append(det(move(copy(a),copy1d(b),i),0)/a1)
    return ans

n=int(input('number of elements '))
l=[]
print("Enter the coefficients for each variable")
for i in range(n):
    l.append(list(map(int,input('row '+str(i+1)+'of the matrix ').split())))
b = list(map(int,input('answers to each equation  ').split()))
print(Cramer(copy(l),copy1d(b)))
