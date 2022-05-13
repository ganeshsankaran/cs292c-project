import argparse as ap
import matplotlib.pyplot as plt
import os
import sys

def make_scatter_plot(title, xdata, ydata, xlabel, ylabel):
    plt.style.use('dark_background')
    plt.figure()
    plt.title(title)
    plt.scatter(xdata, ydata)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(f'../results/graphs/{title}', transparent=True)

parser = ap.ArgumentParser(description='Graph data from CSV')
parser.add_argument('-p', '--path', help='CSV file path', required=True)
parser.add_argument('-x', '--xcol', help='x column name', required=True)
parser.add_argument('-y', '--ycol', help='y column name', required=True)
parser.add_argument('-xl', '--xlabel', help='x label name', required=False)
parser.add_argument('-yl', '--ylabel', help='y label name', required=False)
parser.add_argument('-t', '--title', help='title', required=False)
args = parser.parse_args()

if not os.path.exists(args.path):
    print(f'{args.path} does not exist')
    exit()

xdata = []
ydata = []

if not args.xlabel:
    xlabel = args.xcol
else:
    xlabel = args.xlabel

if not args.ylabel:
    ylabel = args.ycol
else:
    ylabel = args.ylabel

if not args.title:
    title = f'{ylabel} vs {xlabel}'
else:
    title = args.title

with open(args.path, 'r') as f:
    first_line = next(f).rstrip('\n').split(',')
    xindex = -1
    yindex = -1

    try:
        xindex = first_line.index(args.xcol)
    except ValueError:
        print(f'{args.xcol} does not exist in {args.path}')
        exit()

    try:
        yindex = first_line.index(args.ycol)
    except ValueError:
        print(f'{args.ycol} does not exist in {args.path}')
        exit()

    for line in f:
        lst = line.rstrip('\n').split(',')
        xdata.append(float(lst[xindex]))
        ydata.append(float(lst[yindex]))

make_scatter_plot(title, xdata, ydata, xlabel, ylabel)
