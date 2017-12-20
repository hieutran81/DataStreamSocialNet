import numpy as np
import matplotlib.pyplot as plt
import json

m = 9985
n = 563

def read_input():
    global n,rating,shows,alex
    with open("user-shows.txt", "r") as f:
        string = f.read()
    string = string.replace('\n', ' ')
    ls = string.split(' ')
    del(ls[-1])
    rating = np.asarray(ls,dtype=int)
    rating = rating.reshape((9985,563))
    with open("shows.txt", "r") as f:
        string = f.read()
    ls = string.split('\n')
    del (ls[-1])
    shows = ls
    with open("alex.txt", "r") as f:
        string = f.read()
    string = string.replace('\n', ' ')
    ls = string.split(' ')
    del(ls[-1])
    alex = np.asarray(ls,dtype=int)

def computeMatrixPQ():
    global P,Q
    P = np.sum(rating,axis=1)
    Q = np.sum(rating, axis=0)

def computeItemMatrix():
    global Si
    divItem = np.sqrt(Q)
    divItem = divItem.reshape((n,1))
    divItem = np.dot(divItem,divItem.T)
    ii = np.dot(rating.T,rating)
    Si = np.divide(ii,divItem)

def computeUserMatrix():
    global Su
    divItem = np.sqrt(P)
    divItem = divItem.reshape((m,1))
    divItem = np.dot(divItem,divItem.T)
    uu = np.dot(rating,rating.T)
    Su = np.divide(uu,divItem)

def collaborative(alex_rate):
    ls = []
    true_rate = alex[:100]
    shows_watch = np.sum(true_rate)
    print(shows_watch)
    for i in range(100):
        item = []
        item.append(alex_rate[i])
        item.append(i)
        ls.append(item)
    ls = sorted(ls)
    for item in ls[-5:]:
        print(shows[item[1]])
    truePos = []
    for k in range(1,20):
        rated = 0
        for item in ls[-k:]:
            if (true_rate[item[1]] == 1):
                rated += 1
        truePos.append(rated/shows_watch)
    return truePos

def process():
    # computeMatrixPQ()
    # computeUserMatrix()
    # computeItemMatrix()
    # global userColla, itemColla
    # userColla = np.dot(Su, rating)
    # itemColla = np.dot(rating, Si)
    # predict = {}
    # predict['user'] = userColla[499,:500].tolist()
    # predict['item'] = itemColla[499,:500].tolist()
    with open("recommendAlex.txt","r") as f:
        predict = json.load(f)

    userAlex = np.array(predict['user'])
    itemAlex = np.array(predict['item'])
    print("5 show recommend for alex using user colla: ")
    trueUser = collaborative(userAlex)
    plt.plot(trueUser)
    plt.title("user collaborative")
    plt.show()

    print("5 show recommend for alex using item colla: ")
    trueItem = collaborative(itemAlex)
    plt.plot(trueItem)
    plt.title("item collaborative")
    plt.show()

read_input()
process()
