#!/usr/bin/python

import matplotlib.pyplot as plt
import time

class PeachyGrapher():
    def __init__(self,title='',xlabel='',ylabel=''):
        print "Initialized Grapher"
        self.axLabels=[title,xlabel,ylabel]
        self.graphData=[]
        self.graphSetup()

    def saveGraph(self,filename='savedGraph.png'):
        self.fig.savefig(filename)

    def addPoint(self,data):
        self.graphData.append(data)
        plt.xlim(0,len(self.graphData))
        plt.ylim(min(self.graphData),max(self.graphData))
        self.drawGraph()

    def graphSetup(self):
        plt.ion()
        #self.fig, self.ax = plt.subplots()
        self.fig=plt.figure()
        self.ax=plt.subplot("111")
        self.ax.set_title(self.axLabels[0])
        self.ax.set_xlabel(self.axLabels[1])
        self.ax.set_ylabel(self.axLabels[2])
        self.ln, = self.ax.plot([], [], 'go-')

    def drawGraph(self):
        y = self.graphData
        x = range(0,len(self.graphData))
        self.ln.set_data(x,y)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

if __name__ == '__main__':
    #test code:
    grapher=PeachyGrapher("Title","xlabel","ylabel")
    for i in range(1,100):
        grapher.addPoint(float(i))
    grapher.saveGraph("IsavedTheGraph.png")

