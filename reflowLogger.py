#!/usr/bin/python
import serial
import time

class ReflowLogger():
    def __init__(self):
       self.baud=57600
       self.tty='/dev/ttyUSB0'
       self.logFile='reflow.log'
       self.writeLog=self.openFile()

    def connect(self):
        self.conn=serial.Serial(self.tty,self.baud)
        if self.conn:
            print "Connected to Arduino Successfully"
            return True
        else:
            print "Failed to connect to Arduino"
            return False

    def openFile(self):
        self.logFid=open(self.logFile,'w')
        if self.logFid:
            print "Opened Log File Successfully"
        else:
            print "Failed to open Log, skipping logging"

    def readSerial(self):
        msg = self.conn.read(self.conn.inWaiting()).strip()
        if self.writeLog:
            self.logFid.write(msg+"\n")
        return msg

if __name__=="__main__":
    logger=ReflowLogger()
    connectionStatus=logger.connect()
    while(1):
        msg=logger.readSerial()
        if msg:
            print msg
        time.sleep(1)
