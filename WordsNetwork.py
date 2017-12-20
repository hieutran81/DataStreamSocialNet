import json
from math import sqrt

adjMatrix = []
arr = []
word2index = {}
link = []
head = []
adj = []
ex = []
ey = []
visited = []
degree = []
n = 0
m = 0
heavyHitter = []

def hasConnect(s1,s2):
    count = 0
    for i in range(len(s1)):
        if (s1[i] != s2[i]):
            count+=1
    if (count == 1):
        return True
    return False

def initGraph():
    global link, head, adj,degree, heavyHitter
    degree = [0] * n
    head = [0] * n
    link = [0] * (2*m)
    adj = [0] * (2*m)
    for i in range(m):
        u = ex[i]
        v = ey[i]
        degree[u] += 1
        degree[v] += 1
        link[i] = head[u]
        head[u] = i
        adj[i] = v
        link[i+m] = head[v]
        head[v] = i+m
        adj[i+m] = u
    print(degree)
    print(n)
    print(m)
    for i in range(n):
        if (degree[i] >= sqrt(m)):
            print(i)
            heavyHitter.append(i)
    print("heavy hitter:")
    print(len(heavyHitter))
    print(heavyHitter)

    graph = {}
    graph['x'] = ex
    graph['y'] = ey
    graph['n'] = n
    graph['m'] = m
    graph['arr'] = arr
    graph['word2index'] = word2index
    graph['adjMatrix'] = adjMatrix
    graph['link'] = link
    graph['head'] = head
    graph['adj'] = adj
    graph['degree'] = degree
    graph['heavyHitter'] = heavyHitter
    with open("graphWords.txt","w") as f:
        json.dump(graph,f)

def initAdjacentMatrix():
    global m,n,arr,ex,ey,adjMatrix
    # init dictionary from word to index
    for i in range(n):
        if (len(arr[i]) != 5):
            del(arr[i])
    n = len(arr)
    for i in range(n):
        word2index[arr[i]] = i
    # init adjacent matrix
    for i in range(n):
        row = [0] * n
        adjMatrix.append(row)
    for i in range(n):
        for j in range(i+1,n):
            if (hasConnect(arr[i],arr[j])):
                ex.append(i)
                ey.append(j)
                adjMatrix[i][j] = 1
                adjMatrix[j][i] = 1
    m = len(ex)
    initGraph()

def loadGraph():
    global n,m,adj,adjMatrix,arr,link,word2index,head,heavyHitter,ex,ey
    with open("graphWords.txt","r") as f:
        graph = json.load(f)
    n = graph['n']
    m = graph['m']
    adj = graph['adj']
    arr = graph['arr']
    link = graph['link']
    word2index = graph['word2index']
    head = graph['head']
    heavyHitter = graph['heavyHitter']
    ex = graph['x']
    ey = graph['y']
    adjMatrix = graph['adjMatrix']

def init():
    global visited
    visited = [False] * n

def visit(start):
    global visited
    stack = []
    print(arr[start])
    stack.append(start)
    while (len(stack) > 0):
        u = stack.pop()
        visited[u] = True
        i = head[u]
        while (i != 0):
            v = adj[i]
            if (visited[v] == False):
                print(arr[v])
                stack.append(v)
                visited[v] = True
            i = link[i]

def bfs(start,finish):
    global visited
    queue = []
    trace = n * [0]
    queue.append(start)
    while (len(queue) > 0):
        u = queue.pop(0)
        visited[u] = True
        i = head[u]
        while (i != 0):
            v = adj[i]
            if (visited[v] == False):
                trace[v] = u
                queue.append(v)
                visited[v] = True
            i = link[i]
    v = finish
    path = []
    while (trace[v] != 0):
        # print(arr[v])
        path.append(v)
        v = trace[v]
    path.append(start)
    print(len(path))
    for i in range(len(path)-1,-1,-1):
        print(arr[path[i]])


def read_input():
    global n, arr
    with open("sgb-words.txt", "r") as f:
        string = f.read()
    string = string.replace('\n', ' ')
    arr = string.split(' ')
    n = len(arr)
    initAdjacentMatrix()

def cauA():
    init()
    sotplt = 0
    #visit(1)
    for i in range(n):
        if (visited[i]  == False):
            sotplt +=1
            visit(i)
    print("So thanh phan lien thong: %d" %(sotplt))

def cauB():
    init()
    startWord = input('Enter the start word: ')
    finishWord = input('Enter the start word: ')
    start = word2index[startWord]
    finish = word2index[finishWord]
    print(start)
    print(finish)
    bfs(start,finish)

def cauC():
    print("So tam giac heavy hitter: %d" %(len(heavyHitter)))
    numTri = 0
    for j in range(m):
        u = ex[j]
        w = ey[j]
        i = head[u]
        while (i != 0):
            v = adj[i]
            if (adjMatrix[v][w] == 1):
                numTri += 1
                #print("%s  %s  %s"%(arr[u],arr[v],arr[w]))
            i = link[i]
    print("SO tam giac thuong: %d "%(numTri/3))

def process():
    #cauA()
    #cauB()
    cauC()



loadGraph()
#read_input()
process()