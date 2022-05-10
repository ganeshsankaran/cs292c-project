# python3 graph.py [path to csv] [x_axis] [y_axis]
import matplotlib.pyplot as plt
import os.path
from os import path
import sys

def plot_graph(title,x_arr, y_arr, x_label, y_label): 
    plt.figure()
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.scatter(x_arr, y_arr, s = 5)
    plt.title(title)
    # print(x_arr)
    # print(y_arr)
    plt.savefig(f'../results/graphs/{title}')

if len(sys.argv) != 4:
    print('usage: python3 graph.py [path to csv] \'[x_axis]\' \'[y_axis]\'')
    exit()

csv_path = str(sys.argv[1])
x_axis = str(sys.argv[2])
y_axis = str(sys.argv[3])

if not path.exists(csv_path): 
    print(f'{csv_path} does not exist')
    exit()

indices = [-1, -1]
x_arr = []
y_arr = []
title = '{} vs {} from {}'.format(x_axis, y_axis, csv_path.split('/')[-1][:-4])

with open(csv_path, 'r') as f:
    firstLine = next(f).split(',')
    x_index = -1
    y_index = -1
    try: 
        x_index = firstLine.index(x_axis)
    except ValueError: 
        print(f'{x_axis} does not exist in {csv_path}')
        exit()
    
    try: 
        y_index = firstLine.index(y_axis)
    except ValueError: 
        print(f'{y_axis} does not exist in {csv_path}')
        exit() 

    for line in f: 
        arr = line.rstrip('\n').split(',')
        x_arr.append(float(arr[x_index]))
        y_arr.append(float(arr[y_index]))

plot_graph(title, x_arr, y_arr, x_axis, y_axis)
