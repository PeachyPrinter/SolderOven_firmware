#!/usr/bin/python

import matplotlib.pyplot as plt
import time

class PeachyGrapher():
    def __init__(self):
        self.graphData=[0]
        self.graphSetup()

    def addPoint(self,data):
        plt.xlim(0,len(self.graphData))
        plt.ylim(0,max(self.graphData))
        self.graphData.append(data)
        self.drawGraph()

    def graphSetup(self):
        plt.ion()
        self.fig, self.ax = plt.subplots()
        self.ln, = self.ax.plot([], [], 'go-')

    def drawGraph(self):
        x = self.graphData
        y = range(0,len(self.graphData))
        self.ln.set_data(x,y)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

if __name__ == '__main__':
    #test code:
    Grapher=PeachyGrapher()
    for i in range(1,1000):
        Grapher.addPoint(i)

