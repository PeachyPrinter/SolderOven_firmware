#!/usr/bin/python

import matplotlib.pyplot as plt
import time
import random

class PeachyGrapher():
    def __init__(self,title='',xlabel='',ylabel='',graphsize=0,numlines=1):
        print "Initialized Grapher"
        self.graphsize=graphsize
        self.numlines=numlines
        self.axLabels=[title,xlabel,ylabel]
        self.graphData=[[] for i in range(self.numlines)]
        self.graphLimits={"min":0,"max":0}
        self.lines=[]
        self.graphSetup()

    def saveGraph(self,filename='savedGraph.png'):
        self.fig.savefig(filename)

    def addPoint(self,data):
        try:
            test=data[0]
        except:
            data=[data] #Everything in lists makes things easy
        if len(data)!=self.numlines:
            print "Expected {0} points, got {1}, Recieved: {2}".format(self.numlines,len(data),data)
            return

        graphMin=self.graphLimits['min']
        graphMax=self.graphLimits['max']
        for i in range(self.numlines):
            if self.graphsize!=0: #if static
                del self.graphData[i][0]
            self.graphData[i].append(data[i])
            tempMin=min(self.graphData[i])
            tempMax=max(self.graphData[i])
            if graphMin>tempMin:
                graphMin=tempMin
            elif graphMax<tempMax:
                graphMax=tempMax

        self.graphLimits['min']=graphMin
        self.graphLimits['max']=graphMax
        plt.xlim(0,len(self.graphData[0]))
        plt.ylim(self.graphLimits['min'],self.graphLimits['max'])
        plt.ylim(graphMin,graphMax)
        self.drawGraph()

    def graphSetup(self):
        plt.ion()
        self.fig=plt.figure()
        self.ax=plt.axes()
        self.ax.set_title(self.axLabels[0])
        self.ax.set_xlabel(self.axLabels[1])
        self.ax.set_ylabel(self.axLabels[2])
        for i in range(self.numlines):
            if self.graphsize!=0: #static sliding window
                self.graphData[i]=[0]*self.graphsize
            temp_ln, = self.ax.plot([], [])
            self.lines.append(temp_ln)

    def drawGraph(self):
        #for i,ydata in enumerate(self.graphData):
        for i in range(self.numlines):
            y = self.graphData[i]
            x = range(len(self.graphData[i]))
            self.lines[i].set_data(x,y)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

if __name__ == '__main__':

    test=True
    testLen=100
    if test:
        #test code for live graph that grows and shows all:
        grapher=PeachyGrapher("Title","xlabel","ylabel")
        for i in range(0,testLen):
            grapher.addPoint(i)
        grapher.saveGraph("50_point_dyamic.png")

        #test code for set size graph:
        grapher2=PeachyGrapher(graphsize=20)
        for i in range(0,testLen):
            grapher2.addPoint(random.randint(0,100))
        grapher2.saveGraph("20_point_static.png")

        #test code for multiLine static:
        grapher3=PeachyGrapher(graphsize=20,numlines=3)
        for i in range(0,testLen):
            rando=random.randint(0,10)
            grapher3.addPoint([rando,rando+2,rando+5])
        grapher3.saveGraph("3_line_static.png")

        #test code for multiLine dynamic:
        grapher4=PeachyGrapher(numlines=3)
        for i in range(0,testLen):
            rando=random.randint(0,10)
            grapher4.addPoint([rando,rando+2,rando+5])
        grapher4.saveGraph("3_line_dynamic.png")

        print "Done test, press enter after looking at graphs"
        raw_input()
