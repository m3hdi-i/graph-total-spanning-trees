# -----------------------------
# Author : Mehdi I.
# -----------------------------

import numpy as np

def get_total_number_of_spanning_trees(matrix,nodes_count):
    # STEP 1: Replace all the diagonal elements with the degree of nodes.
    for i in range(nodes_count):
        sum_of_col =0
        for j in range(nodes_count):
            sum_of_col+=matrix[j][i]
        matrix[i][i]=sum_of_col

    # STEP 2: Replace all non-diagonal 1’s with -1.
    for i in range(nodes_count):
        for j in range(nodes_count):
            if i!=j and matrix[i][j]==1:
                matrix[i][j]=-1

    # STEP 3: final result is co-factor of any element ( like 0,0 )
    matrix=np.delete(matrix, 0, 0)
    matrix=np.delete(matrix, 0, 1)

    return abs(round(np.linalg.det(matrix)))


if __name__ == '__main__':

    adjacency_matrix=[]

    # Specifying adjacency matrix of graph
    nodes_count=int(input("Enter your graph's nodes count : "))
    for i in range(nodes_count):
        row=[]
        print('Enter values for row '+str(i+1)+' of adjacency matrix : ')
        for j in range(nodes_count):
            row.append(int(input()))

        adjacency_matrix.append(row)

    print('\n Your Adjacency Matrix : \n')
    for row in adjacency_matrix:
        print(" ".join(map(str,row)))
    
    print('\n Total number of spanning trees for given graph is:', get_total_number_of_spanning_trees(adjacency_matrix,nodes_count))
