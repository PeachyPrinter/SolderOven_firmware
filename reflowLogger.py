#!/usr/bin/python
import serial
import time
import os
import matplotlib.pyplot as plt


class ReflowLogger():
    def __init__(self):
       self.baud=57600
       self.tty='/dev/ttyUSB0'
       self.logFile='reflow'
       self.openFile()
       self.setupPyplot()

    def setupPyplot(self):
       self.temps=[]
       self.fig=plt.figure()
       plt.ion()
       self.fig.show()

    def connect(self):
        self.conn=serial.Serial(self.tty,self.baud)
        if self.conn:
            print "Connected to Arduino Successfully"
            return True
        else:
            print "Failed to connect to Arduino"
            return False

    def openFile(self):
        filename=self.logFile
        fileExists=os.path.isfile(filename)
        if fileExists:#No more overwriting files:
            for i in range(1,1000):
                filename=self.logFile+str(i)+".log" #tak a number on the end
                fileExists=os.path.isfile(filename)
                if ~fileExists:
                    break #good enough, use it
        else:
            filename=filename+".log"

        self.logFid=open(filename,'w')
        if self.logFid:
            print "Opened Log File Successfully"
            self.writeLog=True
        else:
            print "Failed to open Log, skipping logging"
            self.writeLog=False

    def readSerial(self):
        #msg = self.conn.readline(self.conn.inWaiting()).strip()
        msg = self.conn.readline().strip()
        split_msg = msg.split(' ')
        if self.writeLog & (len(split_msg)>3):
            self.logFid.write(msg+"\n")
            self.logFid.flush()
            try:
                self.temps.append(float(split_msg[2]))
            except:
                print "tried to graph not an int"
            plt.pause(0.001)
            plt.plot(self.temps)
            plt.pause(0.001)
        return msg

if __name__=="__main__":
    logger=ReflowLogger()
    connectionStatus=logger.connect()
    while(1):
        msg=logger.readSerial()
        if msg:
            print msg
        time.sleep(0.1)
