from pprint import pprint
from numpy import linalg as LA
import numpy as np
degr = []
adj = []
lapla = []
com = []
n = 0
m = 0

def init():
    for i in range(n):
        row = [0] * n
        row1 = [0] * n
        row2 = [0] * n
        degr.append(row)
        adj.append(row1)
        lapla.append(row2)



def read_input():
    with open("in.txt", "r") as f:
        string = f.read()
    string = string.replace('\n', ' ')
    arr = string.split(' ')
    global n,m
    n = int(arr[0])
    m = int(arr[1])
    init()
    for i in range(m):
        u = int(arr[2*i+2])
        v = int(arr[2*i+3])
        adj[u-1][v-1] += 1
        adj[v-1][u-1] += 1
        degr[u-1][u-1] += 1
        degr[v-1][v-1] += 1
    for i in range(n):
        for j in range(n):
            lapla[i][j] = degr[i][j] - adj[i][j]

def findCommunity():
    global com
    np_lap = np.array(lapla)
    w, v = LA.eig(np_lap)
    print(w)
    eigv = []
    for i in range(n):
        item = []
        item.append(w[i])
        item.append(v[:,i])
        eigv.append(item)
    eigv = sorted(eigv)
    com = n * [0]
    sepa = eigv[2][1]
    print(eigv[3][0])
    print(eigv[3][1])
    for i in range(n):
        if sepa[i] > 0:
            com[i] = 1
        else:
            com[i] = -1

def writeFile():
    global adj,com
    string = "graph  { "
    for i in range(n):
        for j in range(n):
            if (j <= i):
                continue
            if((com[i] == com[j]) & (adj[i][j] > 0)):
                string += str(i+1) + " -- " + str(j+1) + " ;"
    string += " } "
    with open("out.txt","w") as f:
        f.write(string)

read_input()
findCommunity()
writeFile()