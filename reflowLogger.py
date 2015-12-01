#!/usr/bin/python
import serial
import time
import os
import atexit
from PeachyGrapher import PeachyGrapher


class ReflowLogger():
    def __init__(self):
       self.baud=57600
       self.tty='/dev/ttyUSB0'
       self.logFile='reflow'
       self.temps=[]
       self.openFile()

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
        return split_msg

def save_exit():
    print "Exiting Cleanly and saving graph"
    grapher.saveGraph("reflow.png")

if __name__=="__main__":
    logger=ReflowLogger()
    grapher=PeachyGrapher(title="Reflow Curve",xlabel="seconds (s)",ylabel="Temperature (C)")
    connectionStatus=logger.connect()
    atexit.register(save_exit)
    while(connectionStatus):
        msg=logger.readSerial()
        if (len(msg)==4):
            try:
                if float(msg[2])<500:
                    grapher.addPoint(float(msg[2]))
                    #grapher.saveGraph("reflow.png")
                else:
                    print "Got Bad result, Thermal Couple Die again?"
            except:
                print "Bad Graphing Line"
            print msg
        time.sleep(0.1)
